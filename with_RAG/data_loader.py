from config import Config
import json
from typing import List, Dict, Any

class DataLoader:
    """Handles loading and processing the knowledge base documents."""

    def __init__(self):
        self.config = Config()
    
    def load_documents(self) -> List[Dict[str, Any]]:
        """Load documents from JSON files."""
        documents = []

        # Import documents
        with open(self.config.OFFERS_FILE, 'r', encoding='utf-8') as f:
            offers_document = json.load(f)
            documents.append(offers_document)

        with open(self.config.PROGRAM_FILE, 'r', encoding='utf-8') as f:
            program_document = json.load(f)     
            documents.append(program_document)

        return documents
    
    def prepare_documents_for_embedding(self, documents: List[Dict[str, Any]]) -> tuple:
        """
        Prepare documents for embedding and storage.
        """
        
        documents_content = [doc['content'] for doc in documents]
        metadata = [{"source": doc['source']} for doc in documents]
        ids = [f"doc_{i}" for i in range(len(documents))]
        
        return documents_content, metadata, ids