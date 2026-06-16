from pathlib import Path

from functions import (
    load_temperature_csv,
    add_year_month_columns,
    filter_month,
    calc_month_stats_by_year,
    find_highest_mean_year,
    save_dataframe,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def run_month_analysis(month):
    """指定した月について、年ごとの気温集計を行う。"""
    csv_file = DATA_DIR / "tokyo_daily_mean_temperature_1980_2025.csv"
    stats_file = OUTPUT_DIR / f"tokyo_month{month}_stats_by_year.csv"
    highest_file = OUTPUT_DIR / f"tokyo_month{month}_highest_mean_year.csv"

    # CSVファイルを読み込み、DataFrameを作成するところまでは書いてあります。
    df = load_temperature_csv(csv_file)
    print("読み込んだデータ")
    print(df.head())

    # TODO: date列からyear列とmonth列を作る。
    df = add_year_month_columns(df)

    # TODO: 指定した月だけを取り出す。
    df_month = filter_month(df, month)

    # TODO: 年ごとの日数・平均・最大・最小を計算する。
    df_year = calc_month_stats_by_year(df_month)

    # TODO: 平均気温が最も高い年を取り出す。
    df_highest = find_highest_mean_year(df_year)

    # TODO: 2つのCSVファイルとして保存する。
    save_dataframe(df_year, stats_file)
    save_dataframe(df_highest, highest_file)

    print("年ごとの集計結果")
    print(df_year.head())
    print("平均気温が最も高い年")
    print(df_highest)
    print("Saved:", stats_file)
    print("Saved:", highest_file)

    return df_year


def main():
    month = 8
    df_result = run_month_analysis(month)
    return df_result


if __name__ == "__main__":
    main()
