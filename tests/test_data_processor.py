import unittest
import pandas as pd
from src.data_processor import NFLDataProcessor

class TestNFLDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = NFLDataProcessor()

    def test_process_team_stats(self):
        sample_data = {"year": 2023, "data": [{"team": "Team A", "wins": 10}, {"team": "Team B", "wins": 8}]}
        result = self.processor.process_team_stats(sample_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)

    def test_process_player_stats(self):
        sample_data = {"year": 2023, "data": [{"player": "Player A", "yards": 1000}, {"player": "Player B", "yards": 800}]}
        result = self.processor.process_player_stats(sample_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()