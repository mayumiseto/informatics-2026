# 第10回：第09回の作業様式の再確認

第10回は、新しい大きな文法を増やす回ではありません。  
第09回で導入した作業場所、`.py` ファイルの編集、`functions.py` / `analysis.py` の分離、実行、出力確認、zip提出をもう一度通します。

**第10回では `report.md` は使いません。**  
Google Drive上で `.md` や `.txt` を直接編集しようとすると混乱しやすいため、レポートファイルは提出物から外します。

## まず全員がやること

`10_Project_Run_on_Colab_Drive.ipynb` を上から実行します。

- Google Drive上で作業する
- 配布時点の `analysis.py` を一度実行する
- CSVとPNGが作成されることを確認する
- `analysis.py` の設定を変更する
- `functions.py` を1か所変更する
- もう一度 `analysis.py` を実行する
- CSVとPNGを確認する
- 提出用zipを作成する
- Google Classroomにzipを提出する

## 第09回が終わっていない人

第10回の時間を使って、第09回の続きを進めます。  
第09回の提出物も提出してください。

## 第09回が終わっている人

第10回の発展課題 A/B/C から1つ選びます。  
発展課題を行った場合は、その内容も含めてzipを作り直して提出します。

- A：札幌の夏は暑くなっているか？
- B：東京の冬は暖かくなっているか？
- C：福岡の6月の降水量は変化しているか？

発展課題では、`functions.py` の関数をできるだけ再利用しながら `analysis.py` を書き換えます。

## 主なファイル

- `10/10_Project_Run_on_Colab_Drive.ipynb`：作業を一気通貫で進める
- `10/10_Homework.md`：提出要件
- `10/project/analysis.py`：問いや地点、月、変数、出力名を設定する
- `10/project/functions.py`：`analysis.py` から呼び出される関数を書く
- `10/examples/README.md`：発展課題A/B/Cのヒント
