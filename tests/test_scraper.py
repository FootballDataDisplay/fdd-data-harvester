import unittest
from src.scraper import NFLDataScraper

class TestNFLDataScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = NFLDataScraper()

    def test_fetch_page(self):
        url = "https://www.pro-football-reference.com"
        soup = self.scraper.fetch_page(url)
        self.assertIsNotNone(soup)

    def test_scrape_team_stats(self):
        result = self.scraper.scrape_team_stats(2023)
        self.assertEqual(result['year'], 2023)
        self.assertIsNotNone(result['data'])

    def test_scrape_player_stats(self):
        result = self.scraper.scrape_player_stats(2023)
        self.assertEqual(result['year'], 2023)
        self.assertIsNotNone(result['data'])

if __name__ == '__main__':
    unittest.main()