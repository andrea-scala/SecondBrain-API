from api.schemas import SBRequest, SBResponse, IngestResponse
from fastapi import APIRouter, UploadFile
from rag.pipeline import chunking, embedding, save_to_chromadb
from agent.agent import run_agent
router = APIRouter()

@router.post("/ask")
def ask(request: SBRequest):
    return SBResponse(response=run_agent(request.prompt))

@router.post("/ingest")
async def ingest(file: UploadFile):
    contents = await file.read()
    contents = contents.decode(encoding="utf-8")
    chunks = chunking(contents)
    embeddings = embedding(chunks)
    save_to_chromadb(chunks, embeddings)
    return IngestResponse(message=f"Ingested {len(chunks)} chunks")