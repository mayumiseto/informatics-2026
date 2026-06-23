from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def load_weather_data(csv_file):
    """気象データのCSVファイルを読み込む。"""
    df = pd.read_csv(csv_file)
    return df


def select_place_month(df, place, month):
    """指定した地点と月のデータだけを取り出す。"""
    selected = df[(df["place"] == place) & (df["month"] == month)]
    return selected


def calc_value(values, method):
    """指定した方法で値を1つに集計する。"""
    if method == "mean":
        return values.mean()
    elif method == "sum":
        return values.sum()
    elif method == "max":
        return values.max()
    elif method == "min":
        return values.min()
    else:
        raise ValueError("method は mean, sum, max, min のいずれかにしてください。")


def explain_aggregation(agg_method):
    """mean や sum が何を意味するかを説明する。"""
    if agg_method == "mean":
        return "mean: 選んだ月の日ごとの値を平均します。"
    elif agg_method == "sum":
        return "sum: 選んだ月の日ごとの値を合計します。"
    elif agg_method == "max":
        return "max: 選んだ月の日ごとの最大値を使います。"
    elif agg_method == "min":
        return "min: 選んだ月の日ごとの最小値を使います。"
    else:
        return "集計方法の説明がありません。"


def calc_yearly_summary(df, value_column, method, start_year, end_year):
    """年ごとの集計値を計算する。

    groupby() は使わず、for文で年を1つずつ取り出して計算する。
    """
    rows = []

    for year in range(start_year, end_year + 1):
        year_df = df[df["year"] == year]

        if len(year_df) > 0:
            value = calc_value(year_df[value_column], method)
            row = {
                "year": year,
                "n_days": len(year_df),
                "value": value,
            }
            rows.append(row)

    summary_df = pd.DataFrame(rows)
    return summary_df


def save_csv(df, output_file):
    """DataFrameをCSVファイルとして保存する。"""
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


def plot_yearly_summary(summary_df, output_file, title, ylabel):
    """年ごとの集計値を折れ線グラフにして保存する。"""
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(summary_df["year"], summary_df["value"], marker="o")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def find_max_year(summary_df):
    """集計値が最も大きい年と値を返す。"""
    max_value = summary_df["value"].max()
    max_row = summary_df[summary_df["value"] == max_value]
    year = int(max_row["year"].iloc[0])
    return year, max_value


def find_min_year(summary_df):
    """集計値が最も小さい年と値を返す。"""
    min_value = summary_df["value"].min()
    min_row = summary_df[summary_df["value"] == min_value]
    year = int(min_row["year"].iloc[0])
    return year, min_value
