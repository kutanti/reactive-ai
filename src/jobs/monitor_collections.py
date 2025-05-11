from src.factory import get_vector_store_provider
from src.clients.openaiclient import OpenAiClient
from src.config import AppConfig
from src.notifications.notifications import publish
import json

class CollectionMonitor:
    def __init__(self):
        print("Initializing the collection monitor...")
        self.appConfig = AppConfig()
        self.openaiclient = OpenAiClient()
        print(self.appConfig.vector_store_provider)
        self.vector_db = get_vector_store_provider(self.appConfig.vector_store_provider)

    def query_by_tag(self, query, collection_name):
        print(f"quering the vector store.")
        query_vector = self.openaiclient.get_embedding(query)  # Example query vector
        response = self.vector_db.search_document(collection_name, query_vector)
        print(f"Search document response: {response}")
        publish(response[0].payload, 'reactive-topic')
    
    def get_tags_and_query(self, json_file_path, collection_name):
        # Add prompt flow to construct the query with the required variable.
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            tags = data.get('tags', [])
            for tag in tags:
                self.query_by_tag(tag, collection_name)