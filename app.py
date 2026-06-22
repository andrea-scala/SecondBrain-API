from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def _():
    return {"status": "ok"}
