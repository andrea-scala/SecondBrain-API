![Nome Alternativo dell'Immagine](assets/img.png)
# SecondBrain-API
SecondBrain is a backend service that allows uploading documents and querying them in natural language. The LLM responds based exclusively on the uploaded documents, citing the exact sources. It uses a RAG pipeline with ChromaDB as the vector database and Groq as the free LLM.

## Stack
- **FastAPI** - Modern Python framework for API REST development
- **LangChain** - Python lib that provides the tools to build the RAG pipeline and orchestrate the agent
- **ChromaDB** - Vector database for storing and retrieving embeddings
- **Groq** - Groq — Free LLM API (Llama 3)
- **sentence-transformers** - Python library for generating text embeddings locally, used for both document ingestion and query retrieval
## Architecture
```mermaid
flowchart TD
    Utente([User])
    
    Ingest[FastAPI /ingest endpoint]
    Ask[FastAPI /ask endpoint]
    
    PipeIngest[RAG Pipeline chunking + embedding]
    Agent[AI Agent tool selection]
    
    SearchTool[Tool: search_documents similarity retrieval]
    CountTool[Tool: count_documents count chunks]
    
    Chroma[(ChromaDB)]
    LLM[LLM Groq]

    Utente -->|upload document| Ingest
    Ingest --> PipeIngest
    PipeIngest -->|save vectors| Chroma

    Utente -->|send prompt| Ask
    Ask --> Agent
    Agent -->|needs document content| SearchTool
    Agent -->|needs document count| CountTool
    SearchTool -->|search vectors| Chroma
    SearchTool --> LLM
    CountTool --> LLM
    LLM -->|response| Utente

    style Utente fill:#ffffff,stroke:#000000,stroke-width:1px,color:#000000
    style Ingest fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style Ask fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style PipeIngest fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style Agent fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style SearchTool fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style CountTool fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style Chroma fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style LLM fill:#ffffff,stroke:#000000,stroke-width:1px,color:#000000
```

## How to use
0. Create a .env file with your Groq API key
   GROQ_API_KEY=your_key_here
   
1. Install dependencies
   pip install -r requirements.txt

2. Start the app
   1. Start with uvicorn (development)
      - `uvicorn app:app --reload`

   2. Start with Docker (recommended)
      - `docker build -t secondbrain-api .`
      - `docker run -p 8000:8000 --env-file .env secondbrain-api`

3. Upload a document
   POST /ingest  →  { "file": "document.txt" }

4. Ask a question
   POST /ask  →  { "prompt": "What does the contract say about deadlines?" }

## Notes
see [notes.md](notes.md)
