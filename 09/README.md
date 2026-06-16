# 第09回：ファイルを分けてプログラムを作る

## この回の目的

第09回では、1つのプログラムを複数のファイルに分けて作る練習をします。

特に、次の役割分担を確認します。

```text
functions.py  処理の部品となる関数を書くファイル
analysis.py   functions.py の関数を組み合わせて、処理の流れを書くファイル
output/       実行結果を保存するフォルダ
```

## Colabでの作業場所

今回の課題では、`functions.py` や `analysis.py` を自分で編集します。
そのため、Colabの一時的な場所である `/content` ではなく、Google Drive上で作業してください。

推奨する作業場所は次の通りです。

```text
/content/drive/MyDrive/informatics_2026/
```

この中にGitHubから取得した教材フォルダが入ります。

```text
/content/drive/MyDrive/informatics_2026/informatics-2026/
```

## フォルダ構成

```text
09/
├── 09_Project_Run_on_Colab_Drive.ipynb
├── 09_Homework.md
├── README.md
├── project/
│   ├── README.md
│   ├── functions.py
│   └── analysis.py
└── practice/
    ├── 1/
    │   ├── functions.py
    │   └── analysis.py
    ├── 2/
    │   ├── data/
    │   ├── functions.py
    │   └── analysis.py
    └── 3/
        ├── data/
        ├── functions.py
        └── analysis.py
```

## 授業中に実行する順番

1. `09_Project_Run_on_Colab_Drive.ipynb` を開く
2. Google Driveをマウントする
3. GitHubから教材を取得する
4. `09/project/analysis.py` を実行する
5. `09_Homework.md` を読み、`09/practice/1`, `2`, `3` を完成させる

## 注意

`rm -rf informatics-2026` は、作業開始後には実行しないでください。
自分で編集した `functions.py` や `analysis.py` も一緒に削除されます。
