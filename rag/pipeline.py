from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def chunking(text: str, cs:int=500, co:int=100) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cs, chunk_overlap=co, add_start_index=True)
    return text_splitter.split_text(text)

def embedding(sentences:list) -> np.ndarray:
    embeddings = model.encode(sentences)
    return embeddings

def save_to_chromadb(docs:list, embeddings:np.ndarray):
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="text_embeddings")
    embeddings = embeddings.tolist()
    collection.add(ids=[f"chunks_{i}" for i in range(len(docs))], embeddings=embeddings, documents=docs)
    