from __future__ import annotations

import requests
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


def query_audio_knowledge(
    query: str,
    collection_name: str = "audio_docs",
    persist_dir: str = "db",
    model: str = "mistral",
    n_results: int = 3,
) -> str:
    client = chromadb.PersistentClient(path=persist_dir)
    embedder = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection(
        name=collection_name, embedding_function=embedder
    )

    results = collection.query(query_texts=[query], n_results=n_results)
    docs = results.get("documents", [[]])[0]
    context = "\n".join(docs)

    prompt = (
        "Answer the following based on the audio transcript context:\n"
        f"{context}\n\nQuestion: {query}"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()
