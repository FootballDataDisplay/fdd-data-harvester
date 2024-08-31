import requests
from bs4 import BeautifulSoup
from typing import Dict, Any, List
import logging

class VersatileScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetch a web page and return a BeautifulSoup object."""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None

    def extract_data(self, soup: BeautifulSoup, data_config: Dict[str, Any]) -> Dict[str, Any]:
        """Extract data from a BeautifulSoup object based on the provided configuration."""
        data = {}
        for key, selector in data_config.items():
            try:
                if isinstance(selector, dict):
                    # Handle nested data
                    element = soup.select_one(selector['selector'])
                    if element:
                        data[key] = self.extract_data(element, selector['data'])
                else:
                    element = soup.select_one(selector)
                    data[key] = element.text.strip() if element else None
            except Exception as e:
                self.logger.error(f"Error extracting {key}: {e}")
                data[key] = None
        return data

    def scrape(self, url_pattern: str, data_config: Dict[str, Any], pages: List[Any] = None) -> List[Dict[str, Any]]:
        """Scrape data from one or multiple pages."""
        all_data = []
        if pages is None:
            pages = [None]
        
        for page in pages:
            url = self.base_url + url_pattern.format(page=page) if page else self.base_url + url_pattern
            soup = self.fetch_page(url)
            if soup:
                data = self.extract_data(soup, data_config)
                all_data.append(data)
                self.logger.info(f"Scraped data from {url}")
            else:
                self.logger.warning(f"Failed to scrape data from {url}")
        
        return all_data

# Example usage:
if __name__ == "__main__":
    # Configuration for example1.com
    example1_config = {
        "base_url": "https://example1.com",
        "url_pattern": "/teams/{page}",
        "data_config": {
            "team_name": "h1.team-name",
            "wins": "span.wins",
            "losses": "span.losses",
            "coach": {
                "selector": "div.coach-info",
                "data": {
                    "name": "span.name",
                    "experience": "span.experience"
                }
            }
        },
        "pages": ["team1", "team2", "team3"]
    }

    # Scrape data from example1.com
    scraper = VersatileScraper(example1_config["base_url"])
    data = scraper.scrape(example1_config["url_pattern"], example1_config["data_config"], example1_config["pages"])
    print(data)

    # Configuration for example2.com
    example2_config = {
        "base_url": "https://example2.com",
        "url_pattern": "/standings",
        "data_config": {
            "league_name": "h1.league-name",
            "teams": {
                "selector": "table.standings",
                "data": {
                    "name": "td.team-name",
                    "position": "td.position"
                }
            }
        }
    }

    # Scrape data from example2.com
    scraper = VersatileScraper(example2_config["base_url"])
    data = scraper.scrape(example2_config["url_pattern"], example2_config["data_config"])
    print(data)