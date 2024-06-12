import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame | None: The loaded DataFrame if successful, None otherwise.
    """
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except (FileNotFoundError,
            IsADirectoryError,
            PermissionError
            ) as e:
        print(f"{e.__class__.__name__}: {e}")
        return None


def main():
    """
    This is the test main function of the script.
    It loads the 'life_expectancy_years.csv' file and prints the result.
    """
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
