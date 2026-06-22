from api.schemas import SBRequest, SBResponse
from fastapi import APIRouter

router = APIRouter()

@router.post("/ask")
def ask(request: SBRequest):
    return SBResponse(response=request.prompt)