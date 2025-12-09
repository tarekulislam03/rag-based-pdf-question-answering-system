import os

from src.pipeline.build_index import build_index
from src.pipeline.query_engine import start_qa_loop
from src.utils.index_path import get_index_paths

def show_banner():
    print("""
┌───────────────────────────┐
│    Welcome to PDF Guru    │
└───────────────────────────┘
""")

def select_pdf(pdf_folder="data/pdfs"):
    pdfs = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdfs:
        print("No PDFs found.")
        exit(1)

    print("\nSelect a PDF to analyze:\n")
    for i, pdf in enumerate(pdfs, start=1):
        print(f"[{i}] {pdf}")

    choice = int(input("\nEnter choice: ")) - 1
    return os.path.join(pdf_folder, pdfs[choice])

def main():
    show_banner()

    pdf_path = select_pdf()
    paths = get_index_paths(pdf_path)

    print("\nIndexing document...")
    build_index(pdf_path, paths)

    print("\nDocument ready. Ask a question (type 'exit' to quit).")
    start_qa_loop(paths)

if __name__ == "__main__":
    main()

