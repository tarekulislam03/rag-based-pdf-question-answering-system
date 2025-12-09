import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
# from text_cleaning import clean_question
from app_config import (
    EMBEDDING_MODEL_NAME,
    DEFAULT_TOP_K,
    BASE_INDEX_DIR
)

import json


# -----------------------------
# Load embedding model (SAME as ingestion)
# -----------------------------
model = SentenceTransformer(EMBEDDING_MODEL_NAME)



# -----------------------------
# Core retrieval function
# -----------------------------
def retrieve_context(query: str, paths: dict, top_k=DEFAULT_TOP_K):

    index = faiss.read_index(paths["faiss"])
    with open(paths["metadata"], "r", encoding="utf-8") as f:
        documents = json.load(f)



    """
    Input:
        question (str)
    Output:
        list of retrieved chunks with metadata
    """

    # 1️⃣ Clean question (light)
    question_cleaned = "What is this document about?"

    # 2️⃣ Embed question
    query_vec = model.encode(question_cleaned).astype("float32")
    faiss.normalize_L2(query_vec.reshape(1, -1))

    # 3️⃣ Search FAISS
    distances, indices = index.search(
        np.array([query_vec]),
        top_k
    )

    # 4️⃣ Fetch chunks + metadata
    results = []

    for rank, idx in enumerate(indices[0]):
        doc = documents[idx]

        results.append({
            "chunk_id": doc["id"],
            "text": doc["text"],
            "page": doc.get("page"),
            "pdf_name": doc.get("pdf_name", "unknown"),
            "score": float(distances[0][rank])
        })

    return results
