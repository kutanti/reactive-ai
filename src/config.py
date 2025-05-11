"""Data class for workspace environment variables
"""
from dataclasses import dataclass
import os
from dotenv import load_dotenv
from src.enums.vector_store_provider_enum import VectorStoreProvider
from src.enums.scraper_type_enum import ScraperTypeEnum


@dataclass(frozen=True)
class AppConfig:
    """Loads all environment variables as predefined properties
    """
    # to load .env file into environment variables for local execution
    load_dotenv()

    openai_api_type: str = os.environ.get("OPENAI_API_TYPE")
    openai_api_version: str = os.environ.get("OPENAI_API_VERSION")
    openai_api_base: str = os.environ.get("OPENAI_API_BASE_URL")
    openai_api_key: str = os.environ.get("OPENAI_API_KEY")
    openai_embedding_model: str = os.environ.get("OPENAI_EMBEDDING_MODEL")
    vector_store_provider: VectorStoreProvider = (
        VectorStoreProvider.QDRANT_CLOUD if os.environ.get("VECTOR_STORE_PROVIDER") == "CLOUD" 
        else VectorStoreProvider.QDRANT_LOCAL
    )
    scraper_type: ScraperTypeEnum = (
        ScraperTypeEnum.PDF if os.environ.get("SCRAPER_TYPE") == "PDF" 
        else ScraperTypeEnum.CSV if os.environ.get("SCRAPER_TYPE") == "CSV" 
        else ScraperTypeEnum.HTML
    )
    collectionName=os.environ.get("COLLECTION_NAME", "indian-stocks")
    twillio_account_number=os.environ.get("TWILLIO_ACCOUNT_NUMBER")
    twillio_auth_token=os.environ.get("TWILLIO_AUTH_TOKEN")
    twillio_whatsapp_number=os.environ.get("TWILLIO_WHATSAPP_NUMBER")
    twillio_recipient_whatsapp_number=os.environ.get("TWILLIO_RECIPIENT_WHATSAPP_NUMBER")
