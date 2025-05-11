from src.factory import get_vector_store_provider, get_scraper
from src.clients.openaiclient import OpenAiClient
from src.utils.qdrant_util import get_all_collections
from src.config import AppConfig
from src.utils.commonutil import get_tokens_len
import re

class TrainDocsJob:
    def __init__(self):
        print("Initializing the training job...")
        self.openaiclient = OpenAiClient()
        self.appConfig = AppConfig()
        self.vector_db = get_vector_store_provider(self.appConfig.vector_store_provider)
        self.scraper = get_scraper(self.appConfig.scraper_type)

    def process(self, collectionName):
        print("Training the vector store.")
        print(f"Type of vector_db: {type(self.vector_db)}")
        
        collections = get_all_collections(self.vector_db)
        print(f"Existing collections: {collections}")
        for collection in collections:
            print(collection)
        # Create a collection
        vector_size = 1536  # Size of the embedding vector
        if collectionName not in collections:
            response = self.vector_db.create_collection(collectionName, vector_size)
        else:
            response = f"Collection '{collectionName}' already exists."
        print(f"Create collection response: {response}")
        
        # Save a document
        text = "RPPInfra is a good complany with bad returns"  # Example text to get embedding for
        embedding = self.openaiclient.get_embedding(text)  # Retrieve embedding from OpenAiClient
        document = {
            "points": [
                {
                    "id": 2,
                    "vector": embedding,  # Use the retrieved embedding
                    "payload": {"value": text}
                }
            ]
        }
        response = self.vector_db.save_document(collectionName, document)
        print(f"Save document response: {response}")
    
    def chunk_text(self, text, chunk_size=1536):
        delimiters = re.split(r'(\.|\s*,\s*)', text)
        chunks = []
        current_chunk = []

        for delimiter in delimiters:
            if delimiter.strip() == "":
                continue
            if get_tokens_len("".join(current_chunk + [delimiter])) <= chunk_size:
                current_chunk.append(delimiter)
            else:
                chunks.append("".join(current_chunk))
                current_chunk = [delimiter]

        if current_chunk:
            chunks.append("".join(current_chunk))

        return chunks
    
if __name__ == "__main__":
    job = TrainDocsJob()
    
    text = "This is a long text that needs to be chunked, into smaller pieces. based on the token size limit."
    chunks = job.chunk_text(text, 5)
    print(len(chunks))
    print("Text chunks:")
    for chunk in chunks:
        print(f'This is a chunk::::{chunk}')