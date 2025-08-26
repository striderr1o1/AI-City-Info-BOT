from fastapi import FastAPI, UploadFile, File
from ingestion import readPDF, SplitText, createEmbeddings, storeInChromaDB, clean_text
from retrieve import CallLLM
app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    text = readPDF(file.file)
    # cleantext = clean_text(text)
    print(text)
    splittedText = SplitText(text)
    embeddings = []
    for text in splittedText:
        embedded = createEmbeddings(text)
        embeddings.append(embedded[0])

    
    status = storeInChromaDB(embeddings, splittedText)
    
    return {
        "Texts": splittedText,
        "Ingestion in Chroma Status": status 
    }

@app.post("/query/")
async def queryDoc(query: str):
    response = CallLLM(query)
    return {
        "Answer": response
    }
