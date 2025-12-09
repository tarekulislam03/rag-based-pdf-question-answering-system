from app_config import BASE_INDEX_DIR
import os

def get_index_paths(pdf_path: str):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    index_dir = os.path.join(BASE_INDEX_DIR, pdf_name)
    os.makedirs(index_dir, exist_ok=True)

    return {
        "index_dir": index_dir,
        "faiss": os.path.join(index_dir, "index.faiss"),
        "metadata": os.path.join(index_dir, "metadata.json"),
    }
