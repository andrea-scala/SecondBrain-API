# Technical Notes

## Phase 1 — FastAPI + Groq

### Why FastAPI over Flask/Bottle
I chose FastAPI over Flask/Bottle (which I already use in production) because I wanted to demonstrate proficiency with a modern framework and its built-in Pydantic validation. For a pure backend service returning JSON, FastAPI is also a natural fit.
### Why Groq over OpenAI
I chose Groq over OpenAI because it offers a free tier with no credit card required, making it ideal for portfolio projects. It exposes the same API interface as OpenAI, so switching to a paid provider in the future would require minimal code changes.
### What I learned about Pydantic
Pydantic models feel similar to Python dataclasses, but with automatic validation built in. In Flask I used to extract and check request data manually. With FastAPI and Pydantic, I just declare the expected structure and types — if the incoming data doesn't match, FastAPI returns a clear error automatically, without any extra code.


## Phase 2 - RAG Pipeline
The RAG pipeline is built on three steps: chunking, embedding, and retrieval. Chunking splits the document into smaller pieces because LLMs have a token limit and cannot process large documents in a single call. I chose sentence-transformers because the same model must be used for both saving and retrieving — if you use different models, the vectors are not comparable and similarity search breaks. The retrieval step was the most surprising: given a user question, the system automatically transforms it into a vector and finds the most semantically similar chunks in ChromaDB — without any keyword matching. The LLM never sees the full document, only the relevant pieces.

## Phase 3 — Docker
We use Docker to containerize the application, allowing anyone to build the image and run the service without manually installing Python, dependencies, or configuring the environment. The image contains everything needed to run the app.
.dockerignore acts as a blacklist — it tells Docker which files to exclude from the build context. Without it, Docker would copy unnecessary files like .venv, chroma_db, and __pycache__ into the image, increasing its size significantly.
.venv is not needed inside the container because Docker itself provides an isolated Python environment with all dependencies installed via pip install -r requirements.txt. The container is already isolated — a virtual environment would be redundant.