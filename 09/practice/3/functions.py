from pathlib import Path

import pandas as pd


def load_temperature_csv(path):
    """CSVファイルを読み込み、date列を日付型に変換する。"""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def add_year_month_columns(df):
    """date列からyear列とmonth列を作る。"""
    # TODO: dfをcopyする。
    # TODO: year列とmonth列を追加する。
    # TODO: 作成したDataFrameをreturnで返す。


def filter_month(df, month):
    """指定した月のデータだけを取り出す。"""
    # TODO: month列が指定した月と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。


def calc_month_stats_by_year(df_month):
    """指定した月について、年ごとの日数・平均・最大・最小を計算する。"""
    # TODO: 年の一覧を作る。
    # TODO: for文で1年ずつ、日数・平均・最大・最小を計算する。
    # TODO: rowsというリストに辞書型で結果を追加する。
    # TODO: pd.DataFrame(rows)をreturnで返す。


def find_highest_mean_year(df_year):
    """平均気温が最も高い年の行を取り出す。"""
    # TODO: mean_tempの最大値を求める。
    # TODO: mean_tempが最大値と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。


def save_dataframe(df, out_file):
    """DataFrameをCSVファイルとして保存する。"""
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False, encoding="utf-8-sig")
