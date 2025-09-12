from config import Config
from data_loader import DataLoader
from sentence_transformers import SentenceTransformer
import chromadb


class VectorStore:
    """Handles the ChromaDB vector store and embedding."""

    def __init__(self):
        self.config = Config()
        self.model = None
        self.chroma_client = None
        self.collection = None
        self.data_loader = DataLoader()

    def initialize(self) -> None:
        """Initialize the vector store."""
        self.model = SentenceTransformer(self.config.EMBEDDING_MODEL)
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(self.config.COLLECTION_NAME)

        # Load and embed documents
        self._load_and_embed_documents()


    def _load_and_embed_documents(self) -> None:
        """Load and embed documents."""
        documents = self.data_loader.load_documents()
        documents_content, metadata, ids = self.data_loader.prepare_documents_for_embedding(documents)

        embeddings = self.model.encode(documents_content).tolist()

        self.collection.add(documents=documents_content, embeddings=embeddings, metadatas=metadata, ids=ids)

    def retrieve_context(self, user_query: str, n_results: int = 3) -> str:
        """Retrieve context from the vector store."""

        # Embed user query
        query_embedding = self.model.encode([user_query]).tolist()

        # Perform similarity search
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )

        # Combine relevant documents
        context_str = "\n\n".join(results["documents"][0])

        return context_str