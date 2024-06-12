import pandas as pd
from load_csv import load


def displayCountryPlot(df: pd.DataFrame | None, country: str) -> None:
    try:
        assert df is not None, "Failed to load DataFrame."
        assert "country" in df.columns, "Invalid DataFrame, missing country."
        assert country in df["country"].values, "Invalid country."

        df.set_index("country", inplace=True)
        country_view = df.loc[country]
        print(country_view)
        country_view.plot(kind="line", title=f"Life expectancy in {country}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def main():
    df = load("life_expectancy_years.csv")
    displayCountryPlot(df, "France")


if __name__ == "__main__":
    main()
