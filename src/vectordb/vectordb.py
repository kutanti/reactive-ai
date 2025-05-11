from abc import ABC, abstractmethod

class VectorDB(ABC):
    
    @abstractmethod
    def create_collection(self, collection_name: str, vector_size: int):
        pass
    
    @abstractmethod
    def get_collection(self, collection_name: str):
        pass
    
    @abstractmethod
    def get_collections(self):
        pass

    @abstractmethod
    def save_document(self, collection_name: str, document: dict):
        pass

    @abstractmethod
    def search_document(self, collection_name: str, query_vector: list):
        pass

    @abstractmethod
    def delete_collection(self, collection_name: str):
        pass
