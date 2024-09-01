import requests
from bs4 import BeautifulSoup

class NFLDataScraper:
    def __init__(self):
        self.base_url = "https://www.pro-football-reference.com"  # Example URL

    def fetch_page(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def scrape_team_stats(self, year):  # This method should be indented to be part of the class
        url = f"{self.base_url}/years/{year}/"
        soup = self.fetch_page(url)
        
        teams_data = []
        
        # Find the table with team stats
        table = soup.find('table', {'id': 'teams'})
        
        if table:
            # Find all rows in the table body
            rows = table.find('tbody').find_all('tr')
            
            for row in rows:
                # Skip rows that don't contain team data
                if row.get('class') and 'thead' in row['class']:
                    continue
                
                team_data = {
                    'team': row.find('th', {'data-stat': 'team'}).text.strip(),
                    'wins': row.find('td', {'data-stat': 'wins'}).text,
                    'losses': row.find('td', {'data-stat': 'losses'}).text,
                    'points_for': row.find('td', {'data-stat': 'points'}).text,
                    'points_against': row.find('td', {'data-stat': 'points_opp'}).text,
                }
                teams_data.append(team_data)
        
        return {"year": year, "data": teams_data}

    def scrape_player_stats(self, year):
        # Placeholder for player stats scraping logic
        url = f"{self.base_url}/years/{year}/passing.htm"
        soup = self.fetch_page(url)
        # Add scraping logic here
        return {"year": year, "data": "placeholder"}

if __name__ == "__main__":
    scraper = NFLDataScraper()
    team_stats = scraper.scrape_team_stats(2022)  # Let's scrape data for 2022
    
    print(f"Team Stats for {team_stats['year']}:")
    for team in team_stats['data']:
        print(f"{team['team']}: {team['wins']}-{team['losses']}, PF: {team['points_for']}, PA: {team['points_against']}")