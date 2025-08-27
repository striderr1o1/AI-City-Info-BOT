# AI-City-Information-Bot

A project for Generative Ai course. Consists of LLM tool-calling for RAG and weather Search. Currently under Development.

## Project Structure
- `main.py`: Main fastapi entry point for the application.
- `ingestion.py`: Data ingestion logic.
- `tools.py`: LLM tool calling.
- `requirements.txt`: Python dependencies.
- `ChromaDB/`: Contains ChromaDB database file.
- `input.wav`: Sample input audio file (irrelevant at the moment).

## Project Insights
LLM tool calling implemented by creating functions and passing schema as tools to the LLM.
Limitation:
- can only call one tool at a time

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. create .env file and enter api keys. Also install Ollama embedding model prior to running app:
   ```bash
   GROQ_API_KEY=""
   OLLAMA_EMBEDDING_MODEL="mxbai-embed-large:latest"
   CHAT_GROQ_MODEL="llama-3.3-70b-versatile"
   ELEVEN_LAB_APIKEY = ""
   TAVILY_API_KEY=""
   ```
4. Run the main application:
   ```bash
   uvicorn main:app --reload
   ```
- Note: Some requirements are irrelevant and need to be removed.

## Features
- Retrieval-Augmented Generation (RAG)
- LLM integration and Multi-tool calling
- voice text-to-speech and speech-to-text (expected)

## License
MIT

## Authors
Mustafa

## References used for Development
- Code snippets from https://medium.com/@manojkotary/exploring-function-calling-capabilities-with-groq-a-step-by-step-guide-586ab7a165aa
- ChatGPT
