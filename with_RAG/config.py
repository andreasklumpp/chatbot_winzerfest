"""Configuration module for the Winzerfest chatbot."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

class Config:
    """Configuration class for environment variables and settings."""
    
    # API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Model Configuration
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    LLM_MODEL = "gpt-5-mini"
    
    # Data paths
    DATA_DIR = "data"
    OFFERS_FILE = os.path.join(DATA_DIR, "scraped_offers.json")
    PROGRAM_FILE = os.path.join(DATA_DIR, "program.json")
    
    # ChromaDB Configuration
    COLLECTION_NAME = "winzerfest_knowledge_base"
    
    # Retrieval Configuration
    DEFAULT_N_RESULTS = 3
    
    # LLM Configuration
    TEMPERATURE = 1
    
 