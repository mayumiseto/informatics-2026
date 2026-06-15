# lesson08_temperature_project

このフォルダには、Web APIから気温データを取得し、CSVファイルとグラフを作成するPythonプログラムが入っています。

第08回で学んだ内容を、1つの小さなプロジェクトとして実行する練習です。

## 1. このフォルダに入っているファイル

```text
lesson08_temperature_project/
├── functions.py
├── analysis.py
└── README.md
```

それぞれの役割は次の通りです。

| ファイル | 役割 |
|---|---|
| `functions.py` | 気温データの取得、CSV保存、月平均の計算、作図などの関数をまとめたファイル |
| `analysis.py` | `functions.py` の関数を組み合わせて、解析全体を実行するファイル |
| `README.md` | このプロジェクトの説明と実行方法を書いたファイル |

## 2. Google Colabで準備する

Google Colabで新しいノートブックを開きます。

### 方法A：授業用URLからzipを取得する場合

教員からzipファイルのURLが指定されている場合は、次のように取得して展開します。

```python
!wget -q -O lesson08_temperature_project.zip "ここにzipファイルのURLを入れる"
!unzip -o -q lesson08_temperature_project.zip
```

### 方法B：zipファイルをColabにアップロードする場合

Colab左側のファイル欄から、`lesson08_temperature_project.zip` をアップロードします。

アップロード後、次のセルを実行して展開します。

```python
!unzip -o lesson08_temperature_project.zip
```

展開できたか確認します。

```python
!find lesson08_temperature_project -maxdepth 2 -type f | sort
```

次のようなファイルが見えれば準備完了です。

```text
lesson08_temperature_project/README.md
lesson08_temperature_project/analysis.py
lesson08_temperature_project/functions.py
```

## 3. まずはそのまま実行する

次のセルを実行します。

```python
!python lesson08_temperature_project/analysis.py
```

この命令は、`analysis.py` をPythonプログラムとして実行する命令です。

うまくいくと、次のフォルダが作成されます。

```text
lesson08_temperature_project/data/
lesson08_temperature_project/figures/
```

`data` にはCSVファイル、`figures` にはグラフ画像が保存されます。

## 4. ノートブックから条件を変えて実行する

都市や月を変えたい場合は、次のように実行します。

```python
%cd /content/lesson08_temperature_project

from analysis import run_temperature_analysis

df_result = run_temperature_analysis("Tokyo", 8)
df_result.head()
```

たとえば、札幌の1月を調べたい場合は、次のように変更します。

```python
df_result = run_temperature_analysis("Sapporo", 1)
df_result.head()
```

那覇の8月を調べたい場合は、次のように変更します。

```python
df_result = run_temperature_analysis("Naha", 8)
df_result.head()
```

## 5. 使える都市名

このプログラムで使える都市名は、`functions.py` の中で登録されています。

```text
Tokyo
NewYork
Sapporo
Naha
```

都市名は大文字・小文字も含めて、上の通りに書いてください。

月は、1月なら `1`、8月なら `8`、12月なら `12` のように、1から12の整数で指定します。

## 6. 今回のポイント

今回のポイントは、長い解析を1つのセルに全部書くのではなく、役割ごとに関数へ分けることです。

```text
functions.py には、部品となる関数を書く
analysis.py には、解析全体の流れを書く
```

`analysis.py` の中では、次のような順番で処理しています。

```text
1. 都市名から緯度・経度を取得する
2. Web APIから日平均気温データを取得する
3. CSVファイルとして保存する
4. CSVファイルを読み込む
5. 指定した月だけを取り出して、年ごとの平均気温を計算する
6. グラフを作成して保存する
```

このように分けておくと、都市や月を変えても同じ処理を使い回しやすくなります。

## 7. よくあるエラー

### `No such file or directory` と出る場合

zipファイルがまだ展開されていない可能性があります。

```python
!unzip -o lesson08_temperature_project.zip
!ls
```

を実行して、`lesson08_temperature_project` フォルダがあるか確認してください。

### `ModuleNotFoundError` と出る場合

`analysis.py` や `functions.py` があるフォルダに移動できていない可能性があります。

```python
%cd /content/lesson08_temperature_project
```

を実行してから、もう一度試してください。

### API関連のエラーが出る場合

このプログラムは、Web APIにアクセスして気温データを取得します。そのため、インターネット接続やAPI側の状況によって、一時的にエラーになることがあります。

少し時間をおいて、もう一度実行してください。
