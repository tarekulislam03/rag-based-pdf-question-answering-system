from typing import List, Dict
import ollama

from src.rag.retriever import retrieve_context
TOP_K = 4

def build_context(chunks: List[Dict]) -> str:
    blocks = []
    for c in chunks:
        block = (
            f"[Source: {c.get('pdf_name', 'document')} | Page {c.get('page')}]\n"
            f"{c['text']}"
        )
        blocks.append(block)

    return "\n\n---\n\n".join(blocks)


def build_prompt(question: str, context: str) -> str:
    return f"""
You are a helpful assistant.

Answer the question using ONLY the context below.
If the answer is not present, say:
"I don't have enough information to answer that."

Context:
{context}

Question:
{question}

Answer:
""".strip()


def generate_answer(prompt: str) -> str:
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"].strip()


def answer_question(question: str, paths: dict, top_k: int = TOP_K):
    chunks = retrieve_context(question, paths, top_k=top_k)
    context = build_context(chunks)
    prompt = build_prompt(question, context)
    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": chunks
    }

