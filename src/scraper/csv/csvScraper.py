import pandas as pd
from src.scraper.scraper import Scraper

class CsvScraper(Scraper):
    def scrape(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_string()