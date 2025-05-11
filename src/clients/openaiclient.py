from openai import AzureOpenAI
from src.config import AppConfig
class OpenAiClient:

    def __init__(self):
        self.appConfig = AppConfig()
        self.client = AzureOpenAI(
            api_key=self.appConfig.openai_api_key,
            azure_endpoint=self.appConfig.openai_api_base,
            api_version=self.appConfig.openai_api_version
        )
    
    def get_embedding(self, text: str):
        response = self.client.embeddings.create(
            input=text,
            model=self.appConfig.openai_embedding_model
        )
        return response.data[0].embedding