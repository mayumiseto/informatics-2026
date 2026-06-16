from pathlib import Path

from functions import celsius_to_fahrenheit, make_message


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    """摂氏温度を華氏温度に変換して、結果を表示・保存する。"""
    celsius = 25
    out_file = OUTPUT_DIR / "result.txt"

    # TODO: functions.py の関数を使って、華氏温度を計算する。
    fahrenheit = celsius_to_fahrenheit(celsius)

    # TODO: functions.py の関数を使って、保存する文字列を作る。
    message = make_message(celsius, fahrenheit)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(message)

    print(message)
    print("Saved:", out_file)


if __name__ == "__main__":
    main()
