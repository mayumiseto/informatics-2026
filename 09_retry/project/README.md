# 第09回 retry project：ファイルを分けた気温解析プログラム

このフォルダには、Web APIから気温データを取得し、CSVファイルとグラフを作成するPythonプログラムが入っています。

第09回では、このプロジェクトを実行しながら、次の役割分担を確認します。

```text
functions.py  解析に使う部品となる関数を書くファイル
analysis.py   functions.py の関数を読み込み、解析全体の流れを書くファイル
```


## このprojectで見返すとよい回

このprojectは、第04回〜第08回の内容をまとめて使っています。
分からないところだけ、対応する回を見返してください。

| 処理 | 見返すとよい回 |
|---|---|
| CSVを保存・読み込みする | 第04回 |
| 日付列を扱い、月ごと・年ごとに集計する | 第05回 |
| グラフを作成して保存する | 第06回 |
| `data/` や `figures/` などのフォルダを扱う | 第07回 |
| `functions.py` と `analysis.py` に分ける | 第08回 |
| `.py` ファイルを `!python` で実行する | 第09回 |
| Web APIからデータを取得する | 第05回 Appendix API |

## フォルダ構成

```text
09_retry/project/
├── README.md
├── functions.py
└── analysis.py
```

実行後には、次のフォルダが自動で作成されます。

```text
09_retry/project/data/
09_retry/project/figures/
```

## 実行方法

Google Colabでは、まず次の作業場所に移動します。

```python
%cd /content/drive/MyDrive/informatics-2026
```

その後、リポジトリ直下から次のように実行します。

```python
!python 09_retry/project/analysis.py
```

うまく実行できると、`data/` にCSVファイル、`figures/` にグラフ画像が保存されます。

## `functions.py` の役割

`functions.py` には、解析に使う部品となる関数が入っています。

主な処理は次の通りです。

```text
都市名から緯度・経度を取り出す
Web APIから気温データを取得する
取得したデータをCSVファイルとして保存する
CSVファイルを読み込む
指定した月だけを取り出して、年ごとの平均気温を計算する
計算結果をグラフにする
```

## `analysis.py` の役割

`analysis.py` は、`functions.py` の関数を読み込み、解析全体の流れを組み立てるファイルです。

`analysis.py` の中では、おおまかに次の順番で処理が進みます。

```text
1. 解析したい都市と月を決める
2. 都市名から緯度・経度を取得する
3. Web APIから日平均気温データを取得する
4. データをCSVファイルとして保存する
5. CSVファイルを読み込む
6. 指定した月の年平均気温を計算する
7. グラフを作成して保存する
```

## 使える都市名

このプログラムで使える都市名は、`functions.py` の中で登録されています。

```text
Tokyo
NewYork
Sapporo
Naha
```

都市名は大文字・小文字も含めて、上の通りに書いてください。

## `__pycache__` について

Pythonファイルを実行したあと、`__pycache__` というフォルダができることがあります。
これはPythonが自動で作る補助的なフォルダです。エラーではありません。

今回の授業では、`__pycache__` は無視して構いません。
