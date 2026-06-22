# SecondBrain-API
SecondBrain is a backend service that allows uploading documents and querying them in natural language. The LLM responds based exclusively on the uploaded documents, citing the exact sources. It uses a RAG pipeline with ChromaDB as the vector database and Groq as the free LLM.

## Stack
- **FastAPI** - Modern Python framework for API REST development
- **LangChain** - Python lib that provides the tools to build the RAG pipeline and orchestrate the agent
- **ChromaDB** - Vector database for storing and retrieving embeddings
- **Groq** - Free LLM

## Architecture
```
flowchart TD
    %% Nodi Principali
    Utente([Utente])
    
    Ingest[FastAPI <br> endpoint /ingest]
    Ask[FastAPI <br> endpoint /ask]
    
    PipeIngest[Pipeline RAG <br> chunking + embedding]
    PipeAsk[Pipeline RAG <br> retrieval per similarità]
    
    Chroma[(ChromaDB)]
    LLM[LLM <br> Groq]

    %% Connessioni Flusso di Ingestione
    Utente -->|carica documento| Ingest
    Ingest --> PipeIngest
    PipeIngest -->|salva vettori| Chroma

    %% Connessioni Flusso di Query
    Utente -->|invia prompt| Ask
    Ask --> PipeAsk
    PipeAsk -->|cerca vettori| Chroma
    PipeAsk --> LLM
    LLM -->|risposta| Utente

    %% Stile e Colori (opzionale, per abbinare l'immagine)
    style Utente fill:#f2ebe9,stroke:#bda7a1,stroke-width:1px
    style Ingest fill:#eee7fd,stroke:#b299e6,stroke-width:2px
    style Ask fill:#eee7fd,stroke:#b299e6,stroke-width:2px
    style PipeIngest fill:#eaf7f2,stroke:#a3dfc7,stroke-width:2px
    style PipeAsk fill:#eaf7f2,stroke:#a3dfc7,stroke-width:2px
    style Chroma fill:#fcf1e3,stroke:#eecfa8,stroke-width:2px
    style LLM fill:#fbf0ec,stroke:#e9cfc5,stroke-width:1px

```

## How to use

1. Install dependencies
   pip install -r requirements.txt

2. Start the service
   uvicorn main:app

3. Upload a document
   POST /ingest  →  { "file": "document.pdf" }

4. Ask a question
   POST /ask  →  { "question": "What does the contract say about deadlines?" }