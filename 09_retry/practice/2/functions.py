from pathlib import Path

import pandas as pd


def add_year_month_columns(df):
    """date列からyear列とmonth列を作る。"""
    # TODO: dfをcopyする。
    # TODO: date列を日付型に変換する。
    # TODO: year列とmonth列を追加する。
    # TODO: 作成したDataFrameをreturnで返す。
    #
    # 復習の目安: DataFrameは第04回、日付列の処理は第05回、関数とreturnは第08回です。
    # ヒント1: 元のDataFrameを直接変えないように、最初に df = df.copy() とします。
    # ヒント2: date列は pd.to_datetime(df["date"]) で日付型にできます。
    # ヒント3: 年は df["date"].dt.year で取り出せます。
    # ヒント4: 月は df["date"].dt.month で取り出せます。
    # ヒント5: 新しい列を作るときは、df["year"] = ... の形で書きます。
    # ヒント6: 最後に return df と書きます。


def filter_month(df, month):
    """指定した月のデータだけを取り出す。"""
    # TODO: month列が指定した月と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。
    #
    # 復習の目安: DataFrameの行抽出は第04回、月の抽出は第05回です。
    # ヒント1: 条件は df["month"] == month です。
    # ヒント2: 条件に合う行だけを取り出すには df[df["month"] == month] と書きます。
    # ヒント3: 取り出した結果を df_month という変数に入れると分かりやすいです。
    # ヒント4: 最後に return df_month と書きます。


def calc_temperature_summary(df):
    """DataFrame全体について、日数・平均・最大・最小を計算する。"""
    # TODO: days, mean_temp, max_temp, min_temp を計算する。
    # TODO: 結果を1行のDataFrameにしてreturnで返す。
    #
    # 復習の目安: len()は第03回、DataFrameの平均・最大・最小は第04回、関数は第08回です。
    # ヒント1: 日数は len(df) で計算できます。
    # ヒント2: 平均値は df["tmean_C"].mean() で計算できます。
    # ヒント3: 最大値は df["tmean_C"].max() で計算できます。
    # ヒント4: 最小値は df["tmean_C"].min() で計算できます。
    # ヒント5: 1行のDataFrameは pd.DataFrame([辞書]) の形で作れます。
    #
    # 例:
    # result = pd.DataFrame([{
    #     "days": days,
    #     "mean_temp": mean_temp,
    # }])
    #
    # ヒント6: 最後に return result と書きます。


def save_dataframe(df, out_file):
    """DataFrameをCSVファイルとして保存する。"""
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False, encoding="utf-8-sig")
