# Football Data Display - Data Harvester

## Description
The Data Harvester is a crucial component of the Football Data Display Project. It is designed to collect and process NFL data from various online sources, providing a robust dataset for analysis and visualization.

## Features
- Web scraping of NFL statistics from multiple sources
- Data cleaning and preprocessing
- Export of data in various formats (CSV, JSON)
- Automated data update schedules

## Installation
To set up the FDD Data Harvester, follow these steps:

1. Clone the repository:
git clone https://github.com/FootballDataDisplay/fdd-data-harvester.git
cd fdd-data-harvester

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt

## Usage
To use the FDD Data Harvester:

1. Activate the virtual environment:
source venv/bin/activate  # On Windows use venv\Scripts\activate

2. Run the main scraper:
python src/scraper.py

3. Process the collected data:
python src/data_processor.py

## Contributing
We welcome contributions to the FDD Data Harvester! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/FootballDataDisplay/fdd-data-harvester](https://github.com/FootballDataDisplay/fdd-data-harvester)
