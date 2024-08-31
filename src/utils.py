import os
from datetime import datetime

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_current_season():
    """Return the current NFL season year."""
    current_year = datetime.now().year
    current_month = datetime.now().month
    return current_year if current_month > 8 else current_year - 1

def save_to_csv(df, filename):
    """Save a DataFrame to a CSV file."""
    ensure_dir('data/processed')
    df.to_csv(f'data/processed/{filename}', index=False)
    print(f"Data saved to data/processed/{filename}")

if __name__ == "__main__":
    print(f"Current NFL season: {get_current_season()}")