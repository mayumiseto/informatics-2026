# 復習の目安:
# - CSVとDataFrame: 第04回
# - 日付・月別/年別集計: 第05回
# - 図の作成: 第06回
# - Pathとフォルダ: 第07回
# - 関数とファイル分割: 第08回
# - !pythonで.pyを実行する流れ: 第09回

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_city_location(city):
    cities = {
        "Tokyo": (35.6895, 139.6917),
        "NewYork": (40.7128, -74.0060),
        "Sapporo": (43.0618, 141.3545),
        "Naha": (26.2124, 127.6792),
    }

    if city not in cities:
        raise ValueError(f"登録されていない都市です: {city}")

    return cities[city]


def fetch_temperature_data(lat, lon, start, end):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start,
        "end_date": end,
        "daily": "temperature_2m_mean",
        "timezone": "Asia/Tokyo"
    }

    url = "https://archive-api.open-meteo.com/v1/archive"
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()

    if "daily" not in data:
        raise ValueError("APIの応答に daily データが含まれていません。")

    return data


def save_temperature_csv(data, out_file):
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temp": data["daily"]["temperature_2m_mean"]
    })

    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_file, index=False, encoding="utf-8-sig")
    print("Saved:", out_file)


def load_temperature_csv(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def calc_month_mean(df, month):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    df_month = df[df["date"].dt.month == month].copy()
    df_month["year"] = df_month["date"].dt.year

    years = sorted(df_month["year"].unique())
    rows = []

    for y in years:
        temps = df_month[df_month["year"] == y]["temp"]
        rows.append({
            "year": int(y),
            "ave_temp": temps.mean()
        })

    return pd.DataFrame(rows)


def plot_month_temperature(df_year, city, month, save_path=None):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df_year["year"], df_year["ave_temp"], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average temperature (deg C)")
    ax.set_title(f"{city}: yearly average temperature in month {month}")
    ax.grid(True)

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print("Saved:", save_path)

    plt.show()