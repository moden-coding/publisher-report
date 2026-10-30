import numbers
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
    import numpy as np
except ImportError:
    raise ImportError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the Anaconda (conda) interpreter in VS Code: Ctrl/Cmd+Shift+P → "
        "'Python: Select Interpreter' → pick the one that says 'anaconda3'."
    ) from None

from src.publisher_report import (unknown_publisher_games, nintendo_best_platform,
                                  best_shooter_year, sales_by_decade)

DATA_PATH = REPO_ROOT / "data" / "vgsales.csv"

COLUMNS = ["Rank", "Name", "Platform", "Year", "Genre", "Publisher",
           "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

practice = pd.DataFrame([
    [1, "N1", "X", 2001.0, "Shooter", "Nintendo", 0, 0, 0, 0, 0.6],
    [2, "N2", "X", 2001.0, "Shooter", "Nintendo", 0, 0, 0, 0, 0.6],
    [3, "N3", "X", 2002.0, "Puzzle",  "Nintendo", 0, 0, 0, 0, 0.5],
    [4, "N4", "Y", 2002.0, "Shooter", "Nintendo", 0, 0, 0, 0, 1.0],
    [5, "S1", "Y", 2002.0, "Sports",  "Sega",     0, 0, 0, 0, 5.0],
    [6, "S2", "X", np.nan, "Shooter", np.nan,     0, 0, 0, 0, 0.3],
    [7, "S3", "Y", 1985.0, "Sports",  "Unknown",  0, 0, 0, 0, 0.7],
    [8, "S4", "Y", 1995.0, "Racing",  "Sega",     0, 0, 0, 0, 0.9],
], columns=COLUMNS)

RETURNED_NONE = "Function returned None. Did you replace `return None`?"
UNKNOWN = ('Fill the blank Publishers with "Unknown" first, then keep every game whose '
           'Publisher is "Unknown". That includes games that already said "Unknown".')
NINTENDO = ("Keep only Nintendo's games first, then find the Platform with the biggest "
            "total (.sum()) Global_Sales.")
SHOOTER = ("Keep only Shooter games first, then find the Year with the biggest "
           "total (.sum()) Global_Sales.")
DECADE = ("Group by decade, not by year. Use // to drop the remainder: "
          "2006 // 10 * 10 is 2000.")


def run(function, df):
    """Call a student function. If it crashes, return the error as text so the test fails with a message."""
    try:
        return function(df)
    except Exception as error:
        return type(error).__name__ + ": " + str(error)


class VideoGameTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(DATA_PATH)

    def check_not_none(self, result):
        if result is None:
            self.fail(RETURNED_NONE)

    def check_table(self, result):
        self.check_not_none(result)
        if not isinstance(result, pd.DataFrame):
            self.fail("Should return a table (DataFrame). Got: " + repr(result)[:200])

    def check_year(self, result, expected, msg):
        self.check_not_none(result)
        if not isinstance(result, numbers.Real):
            self.fail(repr(result) + " is not a year : " + msg)
        self.assertEqual(int(result), expected, msg=msg)

    def check_decades(self, result, expected):
        self.check_not_none(result)
        if not isinstance(result, pd.Series):
            self.fail("Should return a Series. Got: " + repr(result)[:200])
        try:
            totals = {int(k): v for k, v in result.items()}
        except (TypeError, ValueError):
            self.fail("The index should be decades like 1990 or 2000. Got: " + repr(list(result.index))[:200])
        self.assertEqual(set(totals), set(expected), msg=DECADE)
        for decade, value in expected.items():
            self.assertAlmostEqual(totals[decade], value, places=2,
                                   msg="Total Global_Sales for the " + str(decade) + "s is wrong.")


class TestUnknownPublisherGames(VideoGameTestCase):
    def test_real_data(self):
        result = run(unknown_publisher_games, self.df.copy())
        self.check_table(result)
        self.assertEqual(len(result), 261, msg=UNKNOWN)
        self.assertTrue((result["Publisher"] == "Unknown").all(),
                        msg='Every Publisher in your table should be "Unknown".')

    def test_practice_table(self):
        result = run(unknown_publisher_games, practice.copy())
        self.check_table(result)
        self.assertEqual(list(result["Name"]), ["S2", "S3"], msg=UNKNOWN)


class TestNintendoBestPlatform(VideoGameTestCase):
    def test_real_data(self):
        result = run(nintendo_best_platform, self.df.copy())
        self.check_not_none(result)
        self.assertEqual(result, "Wii", msg=NINTENDO)

    def test_practice_table(self):
        result = run(nintendo_best_platform, practice.copy())
        self.check_not_none(result)
        self.assertEqual(result, "X", msg=NINTENDO)


class TestBestShooterYear(VideoGameTestCase):
    def test_real_data(self):
        self.check_year(run(best_shooter_year, self.df.copy()), 2011, SHOOTER)

    def test_practice_table(self):
        self.check_year(run(best_shooter_year, practice.copy()), 2001, SHOOTER)


class TestSalesByDecade(VideoGameTestCase):
    def test_real_data(self):
        self.check_decades(run(sales_by_decade, self.df.copy()),
                           {1980: 376.58, 1990: 1278.91, 2000: 4644.02, 2010: 2520.56, 2020: 0.29})

    def test_practice_table(self):
        self.check_decades(run(sales_by_decade, practice.copy()),
                           {1980: 0.7, 1990: 0.9, 2000: 7.7})


if __name__ == "__main__":
    unittest.main()
