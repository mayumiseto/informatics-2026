from pathlib import Path

import pandas as pd

from functions import (
    add_year_month_columns,
    filter_month,
    calc_temperature_summary,
    save_dataframe,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    """2025年8月の東京の日平均気温を読み込み、概要をCSVに保存する。"""
    csv_file = DATA_DIR / "tokyo_daily_mean_temperature_august_2025.csv"
    out_file = OUTPUT_DIR / "tokyo_august_2025_summary.csv"
    month = 8

    # CSVファイルを読み込み、DataFrameを作成するところまでは書いてあります。
    df = pd.read_csv(csv_file)
    print("読み込んだデータ")
    print(df.head())

    # TODO: date列からyear列とmonth列を作る。
    df = add_year_month_columns(df)

    # TODO: 8月のデータだけを取り出す。
    df_month = filter_month(df, month)

    # TODO: 日数・平均・最大・最小を計算する。
    df_summary = calc_temperature_summary(df_month)

    # TODO: 結果をCSVファイルに保存する。
    save_dataframe(df_summary, out_file)

    print("集計結果")
    print(df_summary)
    print("Saved:", out_file)


if __name__ == "__main__":
    main()
