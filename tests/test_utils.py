import unittest
import os
from src.utils import ensure_dir, get_current_season, save_to_csv
import pandas as pd

class TestUtils(unittest.TestCase):
    def test_ensure_dir(self):
        test_dir = 'test_directory'
        ensure_dir(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)

    def test_get_current_season(self):
        season = get_current_season()
        self.assertIsInstance(season, int)
        self.assertTrue(2020 <= season <= 2030)  # Adjust years as needed

    def test_save_to_csv(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        filename = 'test_data.csv'
        save_to_csv(df, filename)
        self.assertTrue(os.path.exists(f'data/processed/{filename}'))
        os.remove(f'data/processed/{filename}')

if __name__ == '__main__':
    unittest.main()