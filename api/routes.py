from api.schemas import SBRequest, SBResponse, IngestResponse
from fastapi import APIRouter, UploadFile, File
from groq import Groq
from core.config import GROQ_API_KEY

router = APIRouter()
client = Groq(api_key=GROQ_API_KEY)

@router.post("/ask")
def ask(request: SBRequest):
    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "user",
            "content": request.prompt,
        }
    ], model="llama-3.3-70b-versatile")
    response = chat_completion.choices[0].message.content
    return SBResponse(response=response)

@router.post("/ingest")
async def ingest(file: UploadFile):
    contents = await file.read()
    contents = contents.decode(encoding="utf-8")
    print(type(contents))
    return IngestResponse(message=contents)