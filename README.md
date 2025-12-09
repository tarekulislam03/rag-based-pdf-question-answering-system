# PDF Question Answering System (RAG)

A Retrieval-Augmented Generation (RAG) based system that allows users to ask natural language questions over one or multiple PDF documents and receive accurate, source-grounded answers.

This project is designed to reflect **real-world, company-level architecture** used for document intelligence, internal knowledge bases, and enterprise search systems.


## 🚀 Project Overview

Large Language Models (LLMs) cannot answer questions about private or proprietary PDFs by default.  
This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

### Key Capabilities
- Upload and ingest PDF documents
- Extract and preprocess text
- Split documents into semantic chunks
- Generate vector embeddings
- Store embeddings in a vector database
- Retrieve relevant chunks for a given query
- Generate accurate answers grounded in document context
- (Optional) Show source pages for transparency



## 🧠 High-Level Architecture

**Indexing Phase (one-time per PDF)**

**Query Phase (per question)**

