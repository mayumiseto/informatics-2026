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
    #
    # 復習の目安: DataFrameは第04回、日付から年・月を取り出す処理は第05回です。
    # ヒント1: 最初に df = df.copy() とします。
    # ヒント2: このpracticeでは load_temperature_csv() の中でdate列を日付型にしています。
    # ヒント3: 年は df["date"].dt.year で取り出せます。
    # ヒント4: 月は df["date"].dt.month で取り出せます。
    # ヒント5: 最後に return df と書きます。


def filter_month(df, month):
    """指定した月のデータだけを取り出す。"""
    # TODO: month列が指定した月と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。
    #
    # 復習の目安: DataFrameの行抽出は第04回、月の抽出は第05回です。
    # ヒント1: 条件は df["month"] == month です。
    # ヒント2: df[df["month"] == month] で指定した月だけを取り出せます。
    # ヒント3: 最後に取り出したDataFrameを return します。


def calc_month_stats_by_year(df_month):
    """指定した月について、年ごとの日数・平均・最大・最小を計算する。"""
    # TODO: 年の一覧を作る。
    # TODO: for文で1年ずつ、日数・平均・最大・最小を計算する。
    # TODO: rowsというリストに辞書型で結果を追加する。
    # TODO: pd.DataFrame(rows)をreturnで返す。
    #
    # 復習の目安: リストとfor文は第03回、DataFrame集計は第04回、年ごとの集計は第05回、辞書型は第08回Appendixです。
    # ヒント1: 年の一覧は df_month["year"].unique() で作れます。
    # ヒント2: sorted(...) を使うと、年を小さい順にできます。
    # ヒント3: rows = [] という空のリストを用意します。
    # ヒント4: for y in years: と書くと、1年ずつ処理できます。
    # ヒント5: 1年分のデータは df_month[df_month["year"] == y] で取り出せます。
    # ヒント6: 日数は len(df_y) で計算できます。
    # ヒント7: 平均・最大・最小は df_y["tmean_C"].mean(), .max(), .min() で計算できます。
    # ヒント8: 1年分の結果は辞書型で作り、rows.append(...) で追加します。
    #
    # 辞書型の例:
    # {
    #     "year": int(y),
    #     "days": days,
    #     "mean_temp": mean_temp,
    #     "max_temp": max_temp,
    #     "min_temp": min_temp,
    # }
    #
    # ヒント9: 最後に pd.DataFrame(rows) を return します。


def find_highest_mean_year(df_year):
    """平均気温が最も高い年の行を取り出す。"""
    # TODO: mean_tempの最大値を求める。
    # TODO: mean_tempが最大値と一致する行だけを取り出す。
    # TODO: 取り出したDataFrameをreturnで返す。
    #
    # 復習の目安: 最大値max()は第04回、条件で行を取り出す処理は第04回・第05回です。
    # ヒント1: 最大値は df_year["mean_temp"].max() で求められます。
    # ヒント2: 条件は df_year["mean_temp"] == max_value です。
    # ヒント3: 条件に合う行だけを取り出して、return します。


def save_dataframe(df, out_file):
    """DataFrameをCSVファイルとして保存する。"""
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False, encoding="utf-8-sig")
