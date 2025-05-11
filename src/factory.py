from src.enums.vector_store_provider_enum import VectorStoreProvider
from src.vectordb.qdrant.qdrant_local import QdrantLocal
from src.vectordb.qdrant.qdrant_cloud import QdrantCloud
from src.enums.scraper_type_enum import ScraperTypeEnum
from src.scraper.pdf.pdfScraper import PdfScraper
from src.scraper.csv.csvScraper import CsvScraper
from src.scraper.html.htmlScraper import HTMLScraper
from src.scraper.md.mdScrapper import MDScraper

    # Sample usage of the enum VectorStoreProvider
def get_vector_store_provider(provider: VectorStoreProvider):
    if provider == VectorStoreProvider.QDRANT_CLOUD:
        return QdrantCloud()
    elif provider == VectorStoreProvider.QDRANT_LOCAL:
        return QdrantLocal()
    else:
        return "Unknown vector store provider."

# Example usage
provider = VectorStoreProvider.QDRANT_LOCAL
print(get_vector_store_provider(provider))

def get_scraper(scraper_type: ScraperTypeEnum):
    if scraper_type == ScraperTypeEnum.PDF:
        return PdfScraper()
    elif scraper_type == ScraperTypeEnum.CSV:
        return CsvScraper()
    elif scraper_type == ScraperTypeEnum.HTML:
        return HTMLScraper()
    elif scraper_type == ScraperTypeEnum.MarkDown:
        return MDScraper()
    else:
        return "Unknown scraper type."

# Example usage
scraper_type = ScraperTypeEnum.MarkDown
print(get_scraper(scraper_type))