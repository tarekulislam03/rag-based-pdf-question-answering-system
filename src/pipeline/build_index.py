import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from src.ingestion.pdf_reader import extract_text
from src.processing.chunking import clean_text, chunk_text




def build_index(pdf_path: str, paths: dict):
    """
    Full pipeline:
    PDF → text → clean → chunks → embeddings → FAISS index + metadata

    Args:
        pdf_path (str): path to PDF file
        paths (dict): {
            "index_dir": str,
            "faiss": str,
            "metadata": str
        }
    """

    print(f"\n[Indexing] Processing PDF: {os.path.basename(pdf_path)}")

    # -----------------------------
    # 1. Extract text from PDF
    # -----------------------------
    pages = extract_text(pdf_path)

    if not pages:
        raise ValueError("No text extracted from PDF.")

    # -----------------------------
    # 2. Clean + chunk text
    # -----------------------------
    documents = []
    texts_to_embed = []

    pdf_name = os.path.basename(pdf_path)

    chunk_id = 0
    for page_num, raw_text in enumerate(pages, start=1):
        cleaned = clean_text(raw_text)

        if not cleaned:
            continue

        chunks = chunk_text(cleaned)

        for chunk in chunks:
            documents.append({
                "id": chunk_id,
                "pdf_name": pdf_name,
                "page": page_num,
                "text": chunk
            })
            texts_to_embed.append(chunk)
            chunk_id += 1

    if not documents:
        raise ValueError("No chunks created from PDF.")

    print(f"[Indexing] Total chunks: {len(documents)}")

    # -----------------------------
    # 3. Embed chunks
    # -----------------------------
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(
        texts_to_embed,
        show_progress_bar=True
    )

    vectors = np.array(embeddings).astype("float32")
    faiss.normalize_L2(vectors)

    # -----------------------------
    # 4. Build FAISS index
    # -----------------------------
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    print(f"[Indexing] FAISS vectors stored: {index.ntotal}")

    # -----------------------------
    # 5. Persist index + metadata
    # -----------------------------
    os.makedirs(paths["index_dir"], exist_ok=True)

    faiss.write_index(index, paths["faiss"])

    with open(paths["metadata"], "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)

    print("[Indexing] Index build complete ✅")
    print(f"[Saved] {paths['faiss']}")
    print(f"[Saved] {paths['metadata']}")
