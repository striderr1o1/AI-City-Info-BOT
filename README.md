# AI-City-Information-Bot

A project for Generative Ai course. A document containing basic information about Islamabad is stored in chromaDB.Querying the LLM can perform RAG tool over chromaDB or search weather using tavily search tool.

## Project Structure
- `main.py`: Main fastapi entry point for the application.
- `ingestion.py`: Data ingestion logic.
- `tools.py`: LLM tool calling. Contains main callLLM function and other functions passed as tools.
- `requirements.txt`: Python dependencies.
- `ChromaDB/`: Contains ChromaDB database file.
- `input.wav`: Sample input audio file.
- `voicefunctions.py`: contains modules like speech-to-text, text-to-speech
- `strmlitMAIN.py`: contains voice message feature through streamlit.

## Project Insights
LLM tool calling implemented by creating functions and passing schema as tools to the LLM.
Limitation:
- can only call one tool at a time
- can ingest docs through FastAPI but not through streamlit
- LLM can call wrong tool based on its wrong understanding of query context

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
5. Run the streamlit application to use voice message:
   ```bash
   streamlit run strmlitMAIN.py
   ```
- Note: Some requirements are irrelevant and need to be removed.

## Features
- LLM integration and Multi-tool calling for RAG and weather search.
- voice text-to-speech and speech-to-text through streamlit
- document ingestion through FastAPI endpoint

## License
MIT

## References used for Development
- Code snippets from https://medium.com/@manojkotary/exploring-function-calling-capabilities-with-groq-a-step-by-step-guide-586ab7a165aa
- ChatGPT

## Main Technologies Used:
- FastAPI
- Groq
- streamlit
- ElevenLabs
- python
- ChromaDB
- tavily search tool

## Authors
Mustafa
