# 第09回 retry課題：ヒントを見ながら再挑戦する

この課題は、第09回で詰まった人がもう一度確認するためのヒント入り版です。

元の `09/` フォルダは触りません。  
このフォルダ `09_retry/` の中で作業してください。

---


## 困ったときに見返す回

この `09_retry` では、第02回〜第08回で扱った内容を組み合わせています。
全部を見返す必要はありません。詰まった場所に応じて、次の回を確認してください。

- 計算式・変数・文字列：第02回
- リスト・`for`文・`len()`：第03回
- CSV・DataFrame・平均/最大/最小：第04回
- 日付列・月の抽出・年ごとの集計：第05回
- 図の作成・保存：第06回
- パス・フォルダ・Google Drive上の作業場所：第07回
- 関数・`return`・`main()`・ファイル分割：第08回
- `.py` ファイルを `!python` で実行する流れ：第09回

---

## 作業場所

Colabでは、最初に次の場所へ移動します。

```python
%cd /content/drive/MyDrive/informatics-2026
```

以降は、次のように `09_retry/...` から始まるパスで実行します。

```python
!python 09_retry/practice/1/analysis.py
```

---

## 今回の目的

今回の目的は、次の流れを確認することです。

```text
functions.py に関数を書く
↓
analysis.py から関数を使う
↓
!python analysis.py で実行する
↓
output フォルダに結果ができる
```

細かい文法を全部覚えることよりも、

- どのファイルを編集するのか
- どのファイルを実行するのか
- エラーが出たらどこを見るのか

を確認してください。

---

# practice 1：摂氏温度を華氏温度に変換する

## 編集するファイル

```text
09_retry/practice/1/functions.py
```

## 実行するファイル

```python
!python 09_retry/practice/1/analysis.py
```

## 完成させる関数

```python
celsius_to_fahrenheit(celsius)
make_message(celsius, fahrenheit)
```

## 確認するとよい回

- 第02回：変数、計算式、文字列、f文字列
- 第08回：関数、引数、`return`

## ヒント

`celsius_to_fahrenheit(celsius)` では、次の式を使います。

```text
華氏温度 = 摂氏温度 * 9 / 5 + 32
```

`make_message(celsius, fahrenheit)` では、次のような文字列を作ります。

```text
25 deg C = 77.0 deg F
```

f文字列を使うと作りやすいです。

```python
f"{celsius} deg C = {fahrenheit:.1f} deg F"
```

`.1f` は、小数点以下1桁で表示する指定です。

## できるはずの出力

```text
09_retry/practice/1/output/result.txt
```

---

# practice 2：1か月分の気温データを集計する

## 編集するファイル

```text
09_retry/practice/2/functions.py
```

## 実行するファイル

```python
!python 09_retry/practice/2/analysis.py
```

## 完成させる関数

```python
add_year_month_columns(df)
filter_month(df, month)
calc_temperature_summary(df)
```

## 使うデータ

```text
09_retry/practice/2/data/tokyo_daily_mean_temperature_august_2025.csv
```

列名は次の通りです。

```text
date      日付
tmean_C   日平均気温
```

## 確認するとよい回

- 第04回：CSV、DataFrame、`mean()`、`max()`、`min()`
- 第05回：`pd.to_datetime()`、`.dt.year`、`.dt.month`、月の抽出
- 第08回：関数、`return`、DataFrameを返す関数

## ヒント

### add_year_month_columns(df)

```python
df = df.copy()
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
```

最後に、列を追加したDataFrameを `return` します。

### filter_month(df, month)

指定した月だけを取り出す条件は、次の形です。

```python
df["month"] == month
```

### calc_temperature_summary(df)

次のように計算できます。

```python
days = len(df)
mean_temp = df["tmean_C"].mean()
max_temp = df["tmean_C"].max()
min_temp = df["tmean_C"].min()
```

1行のDataFrameを作るには、次の形を使います。

```python
pd.DataFrame([{
    "days": days,
    "mean_temp": mean_temp,
    "max_temp": max_temp,
    "min_temp": min_temp,
}])
```

## できるはずの出力

```text
09_retry/practice/2/output/tokyo_august_2025_summary.csv
```

---

# practice 3：年ごとに集計する

## 編集するファイル

```text
09_retry/practice/3/functions.py
```

## 実行するファイル

```python
!python 09_retry/practice/3/analysis.py
```

## 完成させる関数

```python
add_year_month_columns(df)
filter_month(df, month)
calc_month_stats_by_year(df_month)
find_highest_mean_year(df_year)
```

## 使うデータ

```text
09_retry/practice/3/data/tokyo_daily_mean_temperature_1980_2025.csv
```

## 確認するとよい回

- 第03回：リスト、`for`文、1つずつ処理する考え方
- 第04回：DataFrame、平均・最大・最小
- 第05回：月の抽出、年ごとの集計
- 第08回 Appendix：辞書型、`pd.DataFrame([辞書])` の形
- 第08回：関数、`return`

## ヒント

### 年の一覧を作る

```python
years = sorted(df_month["year"].unique())
```

### 年ごとに処理する

```python
rows = []

for y in years:
    df_y = df_month[df_month["year"] == y]
    # ここで1年分の日数・平均・最大・最小を計算する
    # rows.append(...) で結果を追加する
```

### 1年分の結果を辞書型で作る

```python
{
    "year": int(y),
    "days": days,
    "mean_temp": mean_temp,
    "max_temp": max_temp,
    "min_temp": min_temp,
}
```

### 平均気温が最も高い年を探す

```python
max_value = df_year["mean_temp"].max()
df_highest = df_year[df_year["mean_temp"] == max_value]
```

## できるはずの出力

```text
09_retry/practice/3/output/tokyo_month8_stats_by_year.csv
09_retry/practice/3/output/tokyo_month8_highest_mean_year.csv
```

---

## 提出について

第09回の提出をすでに終えている人は、先生の指示に従ってください。

`09_retry` は、元の第09回を壊さずに確認するためのフォルダです。  
提出が必要な場合は、先生が指定したセルでzipを作成してください。
