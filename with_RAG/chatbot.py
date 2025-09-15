from config import Config
from vector_store import VectorStore
from openai import OpenAI
from typing import List, Dict

class Chatbot:
    """Handles the conversation logic."""

    def __init__(self):
        self.config = Config()
        self.vector_store = VectorStore()
        self.llm_client = None
        self.SYSTEM_PROMPT = (
            "You are acting as a local guide for the Besigheimer Winzerfest. "
            "You are answering questions on the programm of the festival. "
            "You are given context that you can use to answer questions. "
            "Be friendly and engaging. Respond in a structured and easy to read way. If you don't know the answer, say so."
        )
    
    def initialize(self) -> None:
        """Initialize the chatbot."""
        self.vector_store.initialize()
        self.llm_client = OpenAI(api_key=self.config.OPENAI_API_KEY)

    def chat(self, message: str, history: List[Dict[str, str]]) -> str:
        """Process a chat message and return a response."""

        # Retrieve context
        context = self.vector_store.retrieve_context(message)

        # Construct final prompt
        final_prompt = f"{self.SYSTEM_PROMPT}\n\nContext: {context}\n\nUser question: {message}"

        # Construct messages
        messages = [{"role": "system", "content": self.SYSTEM_PROMPT}] + history + [{"role": "user", "content": final_prompt}]

        # Get response
        response = self.llm_client.chat.completions.create(
            model=self.config.LLM_MODEL,
            messages=messages,
            temperature=self.config.TEMPERATURE
        )

        return response.choices[0].message.content