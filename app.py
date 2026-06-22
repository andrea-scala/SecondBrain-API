from fastapi import FastAPI
from api.routes import router
app = FastAPI()
app.include_router(router)
@app.get("/health")
def _():
    return {"status": "ok"}
