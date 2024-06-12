import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def displayCountryPlot(df: pd.DataFrame | None, country: str) -> None:
    """
    Display a plot of life expectancy projections for a specific country.

    Args:
        df (pd.DataFrame | None): The df containing the life expectancy data.
        country (str): The name of the country to display the plot for.

    Raises:
        None

    Returns:
        None
    """
    try:
        assert df is not None, "Failed to load DataFrame."
        assert "country" in df.columns, \
            "Invalid DataFrame, missing country column."
        assert country in df["country"].values, "Invalid country."

        df.set_index("country", inplace=True)
        country_view = df.loc[country]
        country_view.plot()
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def main():
    """
    This program loads a CSV file containing life expectancy data
    and displays a plot for a specific country.
    """
    df = load("life_expectancy_years.csv")
    displayCountryPlot(df, "Finland")


if __name__ == "__main__":
    main()
