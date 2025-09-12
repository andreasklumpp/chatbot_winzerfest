# Winzerfest Chatbot

A RAG-based chatbot for the Besigheimer Winzerfest that helps visitors find information about the festival program, food stands, and events.

## Features

- **Retrieval-Augmented Generation (RAG)**: Uses ChromaDB vector store with sentence transformers for semantic search
- **Gemini Integration**: Powered by Google's Gemini LLM for natural language responses
- **Web Interface**: Clean Gradio interface for easy interaction
- **Modular Architecture**: Organized into separate modules for maintainability

## Setup

1. **Clone and navigate to the project:**
   ```bash
   cd with_RAG
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**

4. **Run the application:**
   ```bash
   uv run app.py
   ```

The chatbot will be available at `http://localhost:7860`

