# 第09回 retry：ヒント入り再挑戦用フォルダ

このフォルダは、第09回で詰まった人が再挑戦するための **ヒント入り版** です。

元の `09/` フォルダとは別物です。  
すでに作業した `09/` フォルダは削除・上書きしないでください。

```text
informatics-2026/
├── 09/          元の第09回フォルダ。すでに作業した内容を残す
├── 09_retry/    ヒント入りの再挑戦用フォルダ
└── 10/
```

## 何をすればよいか

第09回で途中までしかできなかった人は、`09_retry/practice/1`, `2`, `3` を使って再挑戦してください。

```text
09_retry/practice/1/
09_retry/practice/2/
09_retry/practice/3/
```

各フォルダには、次の2つのファイルがあります。

```text
functions.py  関数を書くファイル
analysis.py   functions.py の関数を使って実行するファイル
```

主に編集するのは `functions.py` です。  
`analysis.py` は、基本的には実行して確認するためのファイルです。


## どの回を見返すとよいか

詰まったときは、全部を見返す必要はありません。
自分が困っている内容に近い回だけ確認してください。

| 困っている内容 | 見返すとよい回 | 主なファイル |
|---|---|---|
| Colabのセル、`print()`、基本的な計算 | 第02回 | `02_1_Jupyter_notebook.ipynb`, `02-2_Programming_basics.ipynb` |
| リスト、`for`文、`len()` | 第03回 | `03_List_basics.ipynb` |
| CSV、`DataFrame`、`read_csv()`、`to_csv()`、平均・最大・最小 | 第04回 | `04_CSV_DataFrame_basics.ipynb` |
| 日付列、月の抽出、年ごとの集計 | 第05回 | `05_Time_Series_Filter_and_Aggregate.ipynb` |
| 図の作成や保存 | 第06回 | `06_lecture_visualization.ipynb` |
| フォルダ、パス、Google Drive上の作業場所 | 第07回 | `07_Paths_and_Directory_Structure.ipynb` |
| 関数、`return`、`main()`、`functions.py` と `analysis.py` の分離 | 第08回 | `08_Functions_and_Main.ipynb` |
| 辞書型、キーと値、`pd.DataFrame([辞書])` | 第08回 Appendix | `08_Appendix_Dictionary.ipynb` |
| `.py` ファイルを `!python` で実行すること | 第09回 | `09_Project_Run_on_Colab_Drive.ipynb`, `09_Followup.md` |

## 元の09と違うところ

`functions.py` の中に、TODOだけでなくヒントを追加しています。

例：

```python
# ヒント1: 元のDataFrameを直接変えないように、最初に df = df.copy() とします。
# ヒント2: date列は pd.to_datetime(df["date"]) で日付型にできます。
# ヒント3: 年は df["date"].dt.year で取り出せます。
```

ヒントを見ながら、TODO部分を完成させてください。

## 実行方法

Google Colabでは、まず作業場所に移動します。

```python
%cd /content/drive/MyDrive/informatics-2026
```

その後、次のように実行します。

```python
!python 09_retry/practice/1/analysis.py
!python 09_retry/practice/2/analysis.py
!python 09_retry/practice/3/analysis.py
```

エラーが出た場合は、まず対応する `functions.py` のTODOが残っていないか確認してください。

## よくあるエラー

### TypeError が出る

関数の中で `return` が書けていない可能性があります。

```python
return result
```

のように、計算した結果を返してください。

### ModuleNotFoundError が出る

実行場所が違う可能性があります。

```python
%cd /content/drive/MyDrive/informatics-2026
```

を実行してから、もう一度 `!python ...` を実行してください。

### FileNotFoundError が出る

ファイル名やフォルダ名が違う可能性があります。

- `09_retry/practice/2/data/` にCSVがあるか
- `09_retry/practice/3/data/` にCSVがあるか
- `09_retry` を `09` と間違えていないか

を確認してください。

### IndentationError が出る

字下げがずれている可能性があります。

`def` の中の処理は、同じ幅で字下げしてください。

## 注意

`09_retry` の作業を始めた後は、`09_retry` フォルダを上書きしないでください。  
上書きすると、自分で編集した `functions.py` が消えることがあります。
