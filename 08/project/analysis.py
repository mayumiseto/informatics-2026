from pathlib import Path

from functions import (
    get_city_location,
    fetch_temperature_data,
    save_temperature_csv,
    load_temperature_csv,
    calc_month_mean,
    plot_month_temperature,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FIG_DIR = BASE_DIR / "figures"

DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


def run_temperature_analysis(city, month, start_year=1980, end_year=2025):
    start = f"{start_year}-01-01"
    end = f"{end_year}-12-31"

    lat, lon = get_city_location(city)
    data = fetch_temperature_data(lat, lon, start, end)

    csv_path = DATA_DIR / f"{city.lower()}_daily_mean_temperature_{start_year}_{end_year}.csv"
    save_temperature_csv(data, csv_path)

    df = load_temperature_csv(csv_path)
    df_year = calc_month_mean(df, month)

    fig_path = FIG_DIR / f"{city.lower()}_month{month}_mean_temperature_{start_year}_{end_year}.png"
    plot_month_temperature(df_year, city, month, fig_path)

    return df_year


def main():
    city = "Tokyo"
    month = 8
    df_result = run_temperature_analysis(city, month)
    return df_result


if __name__ == "__main__":
    main()
