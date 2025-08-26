from ingestion import createEmbeddings
import chromadb
from langchain_groq import ChatGroq
import os
from tavily import TavilyClient
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model=os.environ.get("CHAT_GROQ_MODEL"),
    api_key=os.environ.get("GROQ_API_KEY")
)


def retrieveContext(query):
    client = chromadb.PersistentClient(path="ChromaDB")
    embeddings = createEmbeddings([query])
    
    collection = client.get_or_create_collection(name="IslamabadDocs")
    results = collection.query(
        query_embeddings=embeddings[0],
        n_results=5
    )
    return results["documents"][0]

def GetWeatherFromWeb(City):
    tavily_client = TavilyClient(api_key=os.environ.get('TAVILY_API_KEY'))
    response = tavily_client.search(f"Search the current weather in city: {City}")
    return response["results"]

tools = [
    {
         "type": "function",
        "function": {
            "name": "GetWeatherFromWeb",
            "description": "Getting weather details using web search",
            "parameters": {
                "type": "object",
                "properties": {
                    "City": {
                        "type": "string",
                        "description": "City name for fetching weather data",
                    }
                },
            
            },
        },
    },
        {
         "type": "function",
        "function": {
            "name": "retrieveContext",
            "description": "retrieve context from database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "query for searching docs through database",
                    }
                },
            "required": ["query"]
            },
        },
    }
]

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY')
)

MODEL_NAME = "llama3-70b-8192"

def CallLLM(query, tools=tools):
    response1 = client.chat.completions.create(
    model=MODEL_NAME,  # or llama3-8b, mixtral, etc.
    messages=[
        {"role": "system", "content": "Only call the weather tool if the user explicitly asks for weather information. If the word 'weather' is mentioned only then. Otherwise, call the retrieveContext tool. You can also call both."},
        {"role": "user", "content": f"{query}"}
    ],
    tools=tools,
    tool_choice="auto"
    )
    answer1 = response1.choices[0].message.content
    
    tool_call = response1.choices[0].message.tool_calls
    print(answer1)
    print(tool_call)
    
    functionsAvailable = {
        "retrieveContext": retrieveContext,
        "GetWeatherFromWeb": GetWeatherFromWeb
    }
    
    for i in range(len(tool_call)):
        args = json.loads(tool_call[i].function.arguments)
        functionName = tool_call[i].function.name
        function_to_call = functionsAvailable[functionName]
        functionResp = function_to_call(**args)
        print(functionResp)
    
    
    response2 = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "When u get the results from previous agent, you analyze them and give precise answer according to user query"},
            {"role": "user", "content": f"Query: {query}...results: {functionResp}"}
        ]
    )
    answer2 = response2.choices[0].message.content
    return answer2


#limitations: can only call one tool at a time