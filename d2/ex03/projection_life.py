import pandas as pd
from matplotlib import pyplot as plt
from load_csv import load


def main():
    """
    This program loads data on income per person
    and life expectancy for the year 1900,
    and creates a scatter plot to visualize
    the relationship between gross domestic product
    and life expectancy in that year
    for every country in the input data.
    """
    try:
        df_income = \
            load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        df_lifespan = load('life_expectancy_years.csv')
        if df_income is None or df_lifespan is None:
            print("Error loading data")
            exit()
        df_income.set_index('country', inplace=True)
        df_lifespan.set_index('country', inplace=True)
        df_income_1900 = df_income.loc[:, '1900']
        df_lifespan_1900 = df_lifespan.loc[:, '1900']
        df = pd.concat([df_income_1900, df_lifespan_1900], axis='columns')
        df.columns = ['income', 'lifespan']
        df = df.dropna()
        plt.scatter(df['income'], df['lifespan'])
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.title('1900')
        plt.show()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
