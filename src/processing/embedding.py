# from sentence_transformers import SentenceTransformer
# import json
# import faiss
# import numpy as np

# model = SentenceTransformer("all-MiniLM-L6-v2")  # light + effective model

# def embed_chunk(text_chunk):
#     embedding = model.encode(text_chunk, show_progress_bar=False)
#     return embedding


# with open('data/chunks/chunks.json', 'r', encoding='utf-8') as f:
#     chunks = json.load(f)

# documents = []

# for i, chunk in enumerate(chunks):
#     vec = embed_chunk(chunk)# sentence-transformers embedding

#     documents.append({
#         "id": i,
#         "text": chunk,
#         "embedding": vec.tolist(),
#         "page": i  # or real page number if you tracked it
#     })

# with open("vector_store.json", "w", encoding="utf-8") as g:
#     json.dump(documents, g, indent=2)



# clean_vectors = []
# clean_documents = []

# for doc in documents:
#     vec = doc["embedding"]

#     # ensure it is a list AND has correct length
#     if isinstance(vec, list) and len(vec) > 0:
#         clean_vectors.append(vec)
#         clean_documents.append(doc)

# vectors = np.array(clean_vectors).astype("float32")
# documents = clean_documents  # update documents

# faiss.normalize_L2(vectors)

# index = faiss.IndexFlatIP(vectors.shape[1])
# index.add(vectors)

# # Retrival Function
# def search_faiss(query, k=5):
#     # Embed the query
#     q_vec = model.encode(query).astype("float32")
#     faiss.normalize_L2(q_vec.reshape(1, -1))
    
#     # Search
#     distances, indices = index.search(np.array([q_vec]), k)
    
#     # Retrieve the top chunks
#     results = []
#     for idx in indices[0]:
#         results.append(documents[idx])
    
#     return results

# faiss.write_index(index, "vector_index.faiss")


# # query = "What is the Predictive Insights for Collections Strategy?"
# # results = search_faiss(query, k=3)

# # for r in results:
# #     print("\n--- Chunk ---")
# #     print(r["text"][:200], "...")


