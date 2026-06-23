# 発展課題A/B/Cのヒント

最低限のみの人は、このファイルを使わなくても構いません。
発展課題に進む人は、A/B/Cから1つ選びます。

## 発展課題A：札幌の夏は暑くなっているか？

東京の8月ではなく、札幌の8月を見る例です。

変更する主な場所：

- `PLACE` を `Sapporo` にする
- `PLACE_JA` を `札幌` にする
- `OUTPUT_NAME` に `sapporo` が分かる名前を入れる

気温なので、`VALUE_COLUMN` や `AGG_METHOD` は配布時点のままでも進められます。

## 発展課題B：東京の冬は暖かくなっているか？

東京の8月ではなく、東京の1月を見る例です。
この教材では、冬の月として1月を使います。

変更する主な場所：

- `MONTH` を `1` にする
- `QUESTION` を冬の問いに変える
- `OUTPUT_NAME` に `january` や `winter` が分かる名前を入れる

気温なので、`AGG_METHOD = "mean"` が自然です。

## 発展課題C：福岡の6月の降水量は変化しているか？

福岡の6月の降水量を見る例です。
A/Bより少し難しい課題です。

変更する主な場所：

- `PLACE` を `Fukuoka` にする
- `PLACE_JA` を `福岡` にする
- `MONTH` を `6` にする
- `VALUE_COLUMN` を降水量の列に変える
- `VALUE_LABEL` を降水量の名前に変える
- `VALUE_UNIT` を `mm` にする
- `AGG_METHOD` を `sum` にする
- `OUTPUT_NAME` に `fukuoka` と `precip` が分かる名前を入れる

降水量は、1か月の合計を見るため `AGG_METHOD = "sum"` が自然です。
