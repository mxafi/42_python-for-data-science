import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def millions_formatter(x, pos):
    """
    Defines how to format a ticker for matplotlib.
    This function transforms a float or int to
    a millions format, e.g. 60M

    Arguments:
        x: value
        pos: tick position

    Returns:
        formatted value as a string
    """
    return f"{x * 1e-6:.0f}M"


def convert_to_numeric(s: str) -> float:
    """
    Converts a string value to its numeric equivalent.
    Handles endings:
    k: assumed to mean thousands
    M: assumed to mean millions
    B: assumed to mean billions
    """
    if s.endswith('k'):
        multiplier = 1e3
    elif s.endswith('M'):
        multiplier = 1e6
    elif s.endswith('B'):
        multiplier = 1e9
    else:
        multiplier = 1
    if not s[-1].isdigit():
        if multiplier == 1:
            raise ValueError(f"unknown character {s[-1]} in s: {s}")
        s = s[:-1]
    try:
        return float(s) * multiplier
    except ValueError:
        raise ValueError(f"could not convert string to numeric: {s}")


def displayCountryPlots(df: pd.DataFrame | None, country1: str, country2: str) -> None:
    """
    """
    try:
        assert df is not None, "Failed to load DataFrame."
        assert "country" in df.columns, \
            "Invalid DataFrame, missing country column."
        assert country1 in df["country"].values, "Invalid country1."
        assert country2 in df["country"].values, "Invalid country1."

        df.set_index("country", inplace=True)
        df = df.map(convert_to_numeric)
        c1 = df.loc[country1]
        c2 = df.loc[country2]
        print("Country 1", c1)
        print("Country 2", c2)
        print("C1 datatypes", c1.dtypes)
        print("C2 datatypes", c2.dtypes)
        c1.plot()
        c2.plot()
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def main():
    """
    """
    df = load("population_total.csv")
    displayCountryPlots(df, "Finland", "France")


if __name__ == "__main__":
    main()
