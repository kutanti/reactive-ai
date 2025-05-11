from qdrant_client import QdrantClient
from src.vectordb.vectordb import VectorDB
from src.config import AppConfig

class QdrantCloud(VectorDB):
    
    def __init__(self):
        self.appConfig = AppConfig()
        self.client = QdrantClient(
            url=self.appConfig.qdrant_cloud_url, 
            api_key=self.appConfig.qdrant_cloud_key,
        )

    def create_collection(self, collection_name: str, vector_size: int):
        response = self.client.create_collection(
            collection_name=collection_name,
            vectors_config={
                "size": vector_size,
                "distance": "Cosine"
            }
        )
        return response

    def get_collection(self, collection_name: str):
        response = self.client.get_collection(collection_name=collection_name)
        return response
    
    def get_collections(self):
        response = self.client.get_collections()
        return response
    
    def save_document(self, collection_name: str, document: dict):
        response = self.client.upsert(
            collection_name=collection_name,
            points=document["points"]
        )
        return response

    def search_document(self, collection_name: str, query_vector: list):
        response = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=10
        )
        return response

    def delete_collection(self, collection_name: str):
        response = self.client.delete_collection(collection_name)
        return response
