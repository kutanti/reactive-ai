import PyPDF2
from src.scraper.scraper import Scraper

class PdfScraper(Scraper):
    def scrape(self, file_path):
        text = self.scrape_pdf(file_path)
        return text
    
    def scrape_pdf(file_path):
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text