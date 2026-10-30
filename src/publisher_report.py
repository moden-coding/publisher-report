import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "vgsales.csv"


def unknown_publisher_games(df):
    """After filling missing publishers with "Unknown", return a table of the games with an Unknown publisher."""
    return None


def nintendo_best_platform(df):
    """Return the Platform where Nintendo sold the most copies worldwide."""
    return None


def best_shooter_year(df):
    """Return the year when Shooter games sold the most copies worldwide."""
    return None


def sales_by_decade(df):
    """Return the total Global_Sales for each decade."""
    return None


def main():
    df = pd.read_csv(DATA_PATH)
    print("Games with an Unknown publisher:")
    print(unknown_publisher_games(df.copy()))
    print()
    print("Nintendo's best platform:", nintendo_best_platform(df))
    print("Best year for Shooter games:", best_shooter_year(df))
    print()
    print("Worldwide sales by decade:")
    print(sales_by_decade(df.copy()))


if __name__ == "__main__":
    main()
