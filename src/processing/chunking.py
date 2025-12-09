import json

def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  

    return chunks

def clean_text(t):
    # collapse multiple newlines -> single space
    t = t.replace("\n", " ")
    t = t.replace("  ", " ")
    return " ".join(t.split())

