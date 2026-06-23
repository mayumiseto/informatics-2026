from pathlib import Path

from functions import (
    load_weather_data,
    select_place_month,
    calc_yearly_summary,
    save_csv,
    plot_yearly_summary,
    find_max_year,
    find_min_year,
    explain_aggregation,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
OUTPUT_DIR = BASE_DIR / "output"
FIG_DIR = BASE_DIR / "figures"


# =========================
# 発展課題では、ここを自分のテーマに合わせて変更する
# =========================
#
# まずは配布時点の設定のまま実行します。
# 最低限の提出では、このファイルの編集は必須ではありません。
# 発展課題では、下の設定を書き換えます。
# functions.py の関数はできるだけ再利用します。
#
# PLACEを変えたら、PLACE_JAとOUTPUT_NAMEも確認します。
# VALUE_COLUMNを変えたら、VALUE_LABELとVALUE_UNITも確認します。
# 降水量なら AGG_METHOD = "sum" が自然です。
# 気温なら AGG_METHOD = "mean" が自然です。

QUESTION = "東京の8月の日平均気温は、1980年以降どのように変化しているか？"

PLACE = "Tokyo"
PLACE_JA = "東京"
MONTH = 8

VALUE_COLUMN = "temp_mean_c"
VALUE_LABEL = "Mean temperature"
VALUE_UNIT = "deg C"

# mean, sum, max, min から選ぶ
AGG_METHOD = "mean"

START_YEAR = 1980
END_YEAR = 2025

OUTPUT_NAME = "tokyo_august_temp_mean"


# =========================
# ここから下は、基本的にはそのまま使う
# =========================


def main():
    csv_file = DATA_DIR / "weather_daily_1980_2025.csv"

    df = load_weather_data(csv_file)
    selected_df = select_place_month(df, PLACE, MONTH)

    summary_df = calc_yearly_summary(
        selected_df,
        VALUE_COLUMN,
        AGG_METHOD,
        START_YEAR,
        END_YEAR,
    )

    summary_df["place"] = PLACE
    summary_df["place_ja"] = PLACE_JA
    summary_df["month"] = MONTH
    summary_df["value_column"] = VALUE_COLUMN
    summary_df["aggregation"] = AGG_METHOD

    output_csv = OUTPUT_DIR / f"{OUTPUT_NAME}_yearly_summary.csv"
    save_csv(summary_df, output_csv)

    title = f"{PLACE}: month {MONTH} {VALUE_LABEL} ({START_YEAR}-{END_YEAR})"
    ylabel = f"{VALUE_LABEL} ({VALUE_UNIT})"
    output_png = FIG_DIR / f"{OUTPUT_NAME}_yearly_summary.png"
    plot_yearly_summary(summary_df, output_png, title, ylabel)

    max_year, max_value = find_max_year(summary_df)
    min_year, min_value = find_min_year(summary_df)
    aggregation_note = explain_aggregation(AGG_METHOD)

    print("問い:", QUESTION)
    print("地点:", PLACE_JA)
    print("月:", MONTH)
    print("変数:", VALUE_LABEL)
    print("集計方法:", AGG_METHOD)
    print("集計方法の説明:", aggregation_note)
    print("保存したCSV:", output_csv)
    print("保存した図:", output_png)
    print("最も値が大きい年:", max_year, max_value)
    print("最も値が小さい年:", min_year, min_value)


if __name__ == "__main__":
    main()
