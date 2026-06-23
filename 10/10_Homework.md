# 第10回 課題

第10回は、第09回の作業様式をもう一度通す回です。  
課題は3段階に分かれます。

**第10回では `report.md` は使いません。**  
Google Drive上で `.md` や `.txt` を直接編集しようとすると混乱しやすいため、レポートファイルは提出物から外します。

## 1. 第10回の最低限

全員、まずここまで行います。

- `10_Project_Run_on_Colab_Drive.ipynb` を上から実行する
- Google Drive上で作業する
- 配布時点の `analysis.py` を一度実行する
- 出力されたCSVを確認する
- 出力されたPNGを確認する
- `analysis.py` の設定を1か所以上変更する
- `functions.py` を1か所変更する
- もう一度 `analysis.py` を実行する
- 提出用zipを作成する
- Google Classroomにzipを提出する

このzipを提出できれば、第10回の最低限の点が取れます。

## 2. 第09回の積み残し

第09回の課題が終わっていない人は、第10回の時間を使って続きを進めます。

- 第09回の `analysis.py` などを完成させる
- 第09回の提出用zipを作る
- 第09回の提出物もGoogle Classroomに提出する

第10回の最低限zipとは別に、第09回の提出も必要です。

## 3. 第10回の発展課題

第09回が終わっている人は、A/B/Cから1つ選びます。  
発展課題では、`functions.py` の関数をできるだけ再利用しながら `analysis.py` を書き換えます。

### 発展課題A：札幌の夏は暑くなっているか？

同じ日本でも、札幌の夏は暑くなっているかを調べます。

主な変更場所：

- `PLACE`
- `PLACE_JA`
- `OUTPUT_NAME`

### 発展課題B：東京の冬は暖かくなっているか？

東京の冬は暖かくなっているかを調べます。  
この教材では、冬の月として1月を使います。

主な変更場所：

- `MONTH`
- `QUESTION`
- `OUTPUT_NAME`

### 発展課題C：福岡の6月の降水量は変化しているか？

福岡の6月の降水量が変化しているかを調べます。  
A/Bより少し難しい発展課題です。

主な変更場所：

- `PLACE`
- `PLACE_JA`
- `MONTH`
- `VALUE_COLUMN`
- `VALUE_LABEL`
- `VALUE_UNIT`
- `AGG_METHOD`
- `OUTPUT_NAME`

降水量を扱う場合は、`AGG_METHOD = "sum"` が自然です。

## 提出物

提出するのは、指定セルで作成したzipファイルです。

```text
10_project_学籍番号_氏名.zip
```

zipコマンドを覚える必要はありません。  
Colabの最後のセルを実行して、できたzipをGoogle Classroomに添付してください。

## zipに含めるもの

- `10/project/functions.py`
- `10/project/analysis.py`
- `10/project/output/` のCSV
- `10/project/figures/` のPNG

Driveの共有リンクではなく、zipファイル本体を提出してください。

## Google Classroomのコメント欄

コメント欄には、余裕があれば次のどれかを書いてください。  
長く書く必要はありません。

- `analysis.py` で変更したこと
- `functions.py` で変更したこと
- 実行して分かったこと
- 困ったこと
