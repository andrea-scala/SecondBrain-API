from api.schemas import SBRequest, SBResponse, IngestResponse
from fastapi import APIRouter, UploadFile, File
from groq import Groq
from core.config import GROQ_API_KEY
from rag.pipeline import chunking, embedding, save_to_chromadb, retrieve
router = APIRouter()
client = Groq(api_key=GROQ_API_KEY)

@router.post("/ask")
def ask(request: SBRequest):
    context = retrieve(request.prompt)
    content = f"Given the context: ```{context}```, answer to the question: ```{request.prompt}```"
    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "user",
            "content": content,
        }
    ], model="llama-3.3-70b-versatile")
    response = chat_completion.choices[0].message.content
    return SBResponse(response=response)

@router.post("/ingest")
async def ingest(file: UploadFile):
    contents = await file.read()
    contents = contents.decode(encoding="utf-8")
    chunks = chunking(contents)
    embeddings = embedding(chunks)
    save_to_chromadb(chunks, embeddings)
    return IngestResponse(message=f"Ingested {len(chunks)} chunks")