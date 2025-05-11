from src.scraper.scraper import Scraper
import markdown

class MDScraper(Scraper):
    
    def scrape(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return markdown.markdown(text)