from bs4 import BeautifulSoup
import requests
from src.scraper.scraper import Scraper

class HTMLScraper(Scraper):
    def scrape(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.prettify()
        else:
            return f"Failed to retrieve the web page. Status code: {response.status_code}"