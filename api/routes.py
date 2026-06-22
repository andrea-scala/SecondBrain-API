from api.schemas import SBRequest, SBResponse
from fastapi import APIRouter
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