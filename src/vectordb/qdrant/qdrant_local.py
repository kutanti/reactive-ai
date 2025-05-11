from qdrant_client import QdrantClient
from src.vectordb.vectordb import VectorDB

class QdrantLocal(VectorDB):
    
    def __init__(self):
        self.client = QdrantClient(url="http://localhost:6333")  # Local Qdrant instance

    def create_collection(self, collection_name: str, vector_size: int):
        response = self.client.create_collection(
            collection_name=collection_name,
            vectors_config={
                "size": vector_size,
                "distance": "Cosine"  # Distance metric can be "Cosine", "Euclidean", or "Dot"
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
            limit=10  # Example: limit to 10 results
        )
        return response

    def delete_collection(self, collection_name: str):
        response = self.client.delete_collection(collection_name)
        return response
