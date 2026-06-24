from pydantic import BaseModel

class SBRequest(BaseModel):
    prompt: str

class SBResponse(BaseModel):
    response: str
    
class IngestResponse(BaseModel):
    message: str