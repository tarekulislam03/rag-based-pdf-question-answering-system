from src.rag.retriever import retrieve_context
from src.rag.llm_answer import answer_question
from src.utils.index_path import get_index_paths

TOP_K = 4

def start_qa_loop(paths: dict):
    while True:
        question = input("\n> ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        result = answer_question(question, paths)

        print("\nAnswer:\n")
        print(result["answer"])

    