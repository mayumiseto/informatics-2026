# 第09回 総復習課題：ファイルを分けてプログラムを作る

## この課題の目的

今回の目的は、1つのプログラムを複数のファイルに分けて作る練習です。

特に、次の役割分担を意識してください。

```text
functions.py  処理の部品となる関数を書くファイル
analysis.py   functions.py の関数を読み込み、main() の中で処理の流れを書くファイル
output/       実行結果を保存するフォルダ
```

今回は図の作成・保存は行いません。計算結果を `txt` または `csv` として保存します。

---

## 重要：Google Drive上で作業してください

Colabの `/content` は一時的な作業場所です。
ランタイムが切れたり、ノートブックを開き直したりすると、作成したファイルが消えることがあります。

今回の課題では、`functions.py` や `analysis.py` を自分で作成・編集します。
そのため、必ずGoogle Drive上の次の場所で作業してください。

```text
/content/drive/MyDrive/informatics_2026/
```

GitHubから取得した教材は、次の場所に入っている想定です。

```text
/content/drive/MyDrive/informatics_2026/informatics-2026/
```

作業開始後に次の命令は実行しないでください。

```python
!rm -rf informatics-2026
```

この命令を実行すると、自分で編集した `functions.py` や `analysis.py` も消えてしまいます。

---

## 使用するフォルダ

今回は、次の3つのフォルダ内で作業します。

```text
09/practice/1/
09/practice/2/
09/practice/3/
```

各フォルダには、あらかじめ次の2つのファイルが用意されています。

```text
functions.py
analysis.py
```

`analysis.py` には、処理の流れの一部がすでに書かれています。
特にpractice 2とpractice 3では、CSVファイルを読み込むところまでは書いてあります。

みなさんは、主に `functions.py` の中の関数を完成させながら、`analysis.py` から関数を呼び出してプログラムを実行してください。

---

## 使ってよい主な内容

これまでの授業で扱った範囲を使ってください。

使ってよい主な内容の例：

- 関数の定義 `def`
- `return`
- `if __name__ == "__main__":`
- `main()`
- `from functions import ...`
- `Path`
- `mkdir()`
- `open()` と `write()`
- `pandas`
- `pd.read_csv()`
- `pd.to_datetime()`
- DataFrameの列追加
- 条件による行の抽出
- `len()`
- `.mean()`
- `.max()`
- `.min()`
- リスト
- 辞書型
- `for` 文
- `pd.DataFrame()`
- `.to_csv()`

今回の課題では、`groupby()` は使わずに書いてください。

---

# practice 1：関数を別ファイルに分ける最小例

## 目的

`functions.py` に関数を書き、`analysis.py` から読み込んで使う練習をします。

## 作成する場所

```text
09/practice/1/
```

## 課題

摂氏温度を華氏温度に変換し、結果を `output/result.txt` に保存してください。

摂氏温度から華氏温度への変換式は次の通りです。

```text
華氏温度 = 摂氏温度 * 9 / 5 + 32
```

今回は、摂氏温度 `25` 度を変換します。

## `functions.py` に作成する関数

次の2つの関数を完成させてください。

### `celsius_to_fahrenheit(celsius)`

引数 `celsius` を受け取り、華氏温度に変換して返す関数です。

### `make_message(celsius, fahrenheit)`

摂氏温度と華氏温度を受け取り、表示・保存しやすい文字列を返す関数です。

例えば、次のような文字列を返すようにしてください。

```text
25 deg C = 77.0 deg F
```

## `analysis.py` で確認すること

`analysis.py` では、次の流れで処理が進みます。

1. `functions.py` から関数を読み込む
2. `BASE_DIR` と `OUTPUT_DIR` を作る
3. `OUTPUT_DIR` を作成する
4. `main()` を定義する
5. 摂氏温度 `25` を華氏温度に変換する
6. 結果の文字列を作る
7. 結果を `output/result.txt` に保存する
8. 画面にも結果を表示する
9. 最後に `if __name__ == "__main__":` を使って `main()` を実行する

## 実行方法

```python
!python informatics-2026/09/practice/1/analysis.py
```

## 出力ファイル

```text
informatics-2026/09/practice/1/output/result.txt
```

---

# practice 2：DataFrameを入力として簡単な処理をする

## 目的

CSVファイルを読み込み、DataFrameを関数に渡して、簡単な集計を行う練習をします。

## 作成する場所

```text
09/practice/2/
```

## 使用するデータ

次のCSVファイルを使います。

```text
09/practice/2/data/tokyo_daily_mean_temperature_august_2025.csv
```

このCSVには、2025年8月の東京の日平均気温が入っています。

列は次の通りです。

```text
date      日付
tmean_C   日平均気温（℃）
```

## 課題

CSVファイルを読み込み、2025年8月について次の値を計算してください。

- データの日数
- 日平均気温の平均値
- 日平均気温の最大値
- 日平均気温の最小値

結果は、1行のDataFrameとして作成し、CSVファイルとして保存してください。

## `analysis.py` について

practice 2の `analysis.py` には、CSVファイルを読み込むところまでは書いてあります。

```python
df = pd.read_csv(csv_file)
```

そのあと、`functions.py` に書いた関数を呼び出して、集計と保存を行います。

## `functions.py` に作成する関数

次の関数を完成させてください。

### `add_year_month_columns(df)`

`date` 列を日付型に変換し、`year` 列と `month` 列を追加したDataFrameを返す関数です。

### `filter_month(df, month)`

DataFrameと月を受け取り、指定した月だけのDataFrameを返す関数です。

### `calc_temperature_summary(df)`

DataFrameを受け取り、次の列を持つ1行のDataFrameを返す関数です。

```text
days
mean_temp
max_temp
min_temp
```

### `save_dataframe(df, out_file)`

この関数は、あらかじめ書いてあります。
DataFrameをCSVファイルとして保存する関数です。

## 実行方法

```python
!python informatics-2026/09/practice/2/analysis.py
```

## 出力ファイル

```text
informatics-2026/09/practice/2/output/tokyo_august_2025_summary.csv
```

## 確認の目安

出力CSVには、次の列が含まれていればよいです。

```text
days, mean_temp, max_temp, min_temp
```

`days` は `31` になるはずです。

---

# practice 3：DataFrameを入力としてやや複雑な処理をする

## 目的

長期間のCSVファイルを読み込み、指定した月について年ごとの集計を行う練習をします。

今回は `groupby()` は使わず、`for` 文、リスト、辞書型、条件抽出を組み合わせて処理を書いてください。

## 作成する場所

```text
09/practice/3/
```

## 使用するデータ

次のCSVファイルを使います。

```text
09/practice/3/data/tokyo_daily_mean_temperature_1980_2025.csv
```

このCSVには、1980年から2025年までの東京の日平均気温が入っています。

列は次の通りです。

```text
date      日付
tmean_C   日平均気温（℃）
```

## 課題

CSVファイルを読み込み、8月だけを取り出し、年ごとに次の値を計算してください。

- 年
- その年の8月の日数
- その年の8月の日平均気温の平均値
- その年の8月の日平均気温の最大値
- その年の8月の日平均気温の最小値

さらに、年ごとの集計結果の中から、8月の平均気温が最も高い年を取り出してください。

結果は、次の2つのCSVファイルとして保存してください。

```text
09/practice/3/output/tokyo_month8_stats_by_year.csv
09/practice/3/output/tokyo_month8_highest_mean_year.csv
```

## `analysis.py` について

practice 3の `analysis.py` には、CSVファイルを読み込むところまでは書いてあります。

```python
df = load_temperature_csv(csv_file)
```

そのあと、`functions.py` に書いた関数を呼び出して、年ごとの集計と保存を行います。

## `functions.py` に作成する関数

次の関数を完成させてください。

### `load_temperature_csv(path)`

この関数は、あらかじめ書いてあります。
CSVファイルを読み込み、`date` 列を日付型に変換したDataFrameを返す関数です。

### `add_year_month_columns(df)`

`date` 列から `year` 列と `month` 列を追加したDataFrameを返す関数です。

### `filter_month(df, month)`

DataFrameと月を受け取り、指定した月だけのDataFrameを返す関数です。

### `calc_month_stats_by_year(df_month)`

指定した月だけのDataFrameを受け取り、年ごとの集計結果をDataFrameとして返す関数です。

返すDataFrameには、次の列を含めてください。

```text
year
days
mean_temp
max_temp
min_temp
```

ヒント：

1. `df_month["year"].unique()` で年の一覧を作る
2. `sorted()` で年を小さい順に並べる
3. `rows = []` という空のリストを作る
4. `for` 文で1年ずつ処理する
5. その年だけのDataFrameを条件抽出する
6. 辞書型で1年分の結果を作る
7. `rows.append(...)` でリストに追加する
8. 最後に `pd.DataFrame(rows)` でDataFrameにする

### `find_highest_mean_year(df_year)`

年ごとの集計結果を受け取り、`mean_temp` が最も高い年の行をDataFrameとして返す関数です。

### `save_dataframe(df, out_file)`

この関数は、あらかじめ書いてあります。
DataFrameをCSVファイルとして保存する関数です。

## 実行方法

```python
!python informatics-2026/09/practice/3/analysis.py
```

## 出力ファイル

```text
informatics-2026/09/practice/3/output/tokyo_month8_stats_by_year.csv
informatics-2026/09/practice/3/output/tokyo_month8_highest_mean_year.csv
```

## 確認の目安

`tokyo_month8_stats_by_year.csv` には、1980年から2025年までの各年の集計結果が入っていればよいです。

`tokyo_month8_highest_mean_year.csv` には、8月の平均気温が最も高い年の行が入っていればよいです。

---

# 提出方法

## 提出するもの

Google Classroomには、次のものを1つのzipファイルにまとめて提出してください。

```text
09/practice/1/functions.py
09/practice/1/analysis.py
09/practice/1/output/result.txt

09/practice/2/functions.py
09/practice/2/analysis.py
09/practice/2/output/tokyo_august_2025_summary.csv

09/practice/3/functions.py
09/practice/3/analysis.py
09/practice/3/output/tokyo_month8_stats_by_year.csv
09/practice/3/output/tokyo_month8_highest_mean_year.csv
```

`data/` フォルダは最初から配布されているため、提出してもしなくてもかまいません。ただし、フォルダごとzipにまとめる場合は、`data/` が含まれていても問題ありません。

## 提出ファイル名

zipファイル名は次の形式にしてください。

```text
09_practice_学籍番号_氏名.zip
```

例：

```text
09_practice_123456_情報太郎.zip
```

## zipファイルの作り方

3つのpracticeを実行したあと、Colabで次のセルを実行するとzipファイルを作成できます。

```python
%cd /content/drive/MyDrive/informatics_2026
!zip -r 09_practice_学籍番号_氏名.zip informatics-2026/09/practice -x "*/__pycache__/*" "*/.DS_Store"
```

`学籍番号` と `氏名` の部分は、自分のものに書き換えてください。

例：

```python
%cd /content/drive/MyDrive/informatics_2026
!zip -r 09_practice_123456_情報太郎.zip informatics-2026/09/practice -x "*/__pycache__/*" "*/.DS_Store"
```

作成されたzipファイルは、Google Driveの次の場所に保存されます。

```text
MyDrive/informatics_2026/
```

## Google Classroomでの提出

1. Google Classroomで第09回課題を開く
2. Google Drive上に作成したzipファイルを添付する
3. `提出` を押す

## 注意

- `functions.py` と `analysis.py` の両方を提出してください。
- 出力ファイルも提出してください。
- `__pycache__` フォルダは提出不要です。
- Colabの `/content` は一時的な作業場所です。今回の課題では、必ずGoogle Drive上で作業してください。
- 作業開始後に `rm -rf informatics-2026` は実行しないでください。
- 提出前に、practice 1, 2, 3 の `analysis.py` がすべて実行できることを確認してください。

---

# 提出前チェックリスト

提出前に、次の項目を確認してください。

- [ ] `practice/1/functions.py` を完成させた
- [ ] `practice/1/analysis.py` を確認した
- [ ] `practice/1/output/result.txt` ができた
- [ ] `practice/2/functions.py` を完成させた
- [ ] `practice/2/analysis.py` を確認した
- [ ] `practice/2/output/tokyo_august_2025_summary.csv` ができた
- [ ] `practice/3/functions.py` を完成させた
- [ ] `practice/3/analysis.py` を確認した
- [ ] `practice/3/output/tokyo_month8_stats_by_year.csv` ができた
- [ ] `practice/3/output/tokyo_month8_highest_mean_year.csv` ができた
- [ ] zipファイル名を `09_practice_学籍番号_氏名.zip` にした
- [ ] Google Classroomでzipファイルを添付して提出した
