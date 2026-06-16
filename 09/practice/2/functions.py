from pathlib import Path

import pandas as pd


def add_year_month_columns(df):
    """date列からyear列とmonth列を作る。"""
    # TODO: dfをcopyする。
    # TODO: date列を日付型に変換する。
    # TODO: year列とmonth列を追加する。
    # TODO: 作成したDataFrameをreturnで返す。


def filter_month(df, month):
    """指定した月のデータだけを取り出す。"""
    # TODO: month列が指定した月と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。


def calc_temperature_summary(df):
    """DataFrame全体について、日数・平均・最大・最小を計算する。"""
    # TODO: days, mean_temp, max_temp, min_temp を計算する。
    # TODO: 結果を1行のDataFrameにしてreturnで返す。


def save_dataframe(df, out_file):
    """DataFrameをCSVファイルとして保存する。"""
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False, encoding="utf-8-sig")
