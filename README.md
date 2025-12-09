# PDF Guru

A **RAG-based PDF reader and question-answering system** that retrieves relevant context from documents and generates grounded answers using a **local LLM**.

This system is designed to **retrieve first, then answer** — avoiding hallucinations by relying strictly on document content.


## Overview

PDf Guru allows users to:

- Select a PDF document
- Build a semantic vector index for that document
- Ask natural-language questions
- Receive answers grounded in retrieved document context
- See where information comes from (page-level metadata)

The system uses **local embeddings, FAISS for vector search, and a local LLM for answer generation**, making it suitable for offline or privacy-focused use cases.


## Architecture (High-Level)
User Question
->
Query Embedding
->
FAISS Vector Search
->
Top-K Relevant Chunks
->
Local LLM
->
Answer 


Each PDF is indexed **independently** and stored in its own vector index directory.


## Tech Stack

- **Python**
- **PyPDF** – PDF text extraction
- **SentenceTransformers** – text embeddings
- **FAISS** – vector similarity search
- **Local LLM** (via Ollama or compatible local runner)
- **NumPy**

No cloud LLM APIs are required.


## Key Design Decisions

- **Local LLM**:  
  All answers are generated using a locally hosted language model ( LLaMA).

- **Dynamic Indexing**:  
  Each PDF gets its own FAISS index and metadata store — no overwriting.

- **Strict Retrieval-Augmented Generation**:  
  The LLM only sees retrieved document chunks, not the full PDF or external data.

- **Explainability**:  
  Retrieved chunks include page numbers and source metadata.


## Project Structure
src/  
├── app\_config.py # Global policies & defaults  
├── run.py # Single entry point  
│  
├── utils/  
│ └── index\_paths.py # Dynamic index path resolution  
│  
├── pipeline/  
│ ├── build\_index.py # PDF → chunks → embeddings → FAISS  
│ └── query\_engine.py # Interactive Q&A loop  
│  
├── rag/  
│ ├── retriever.py # Vector search (FAISS)  
│ └── llm\_answer.py # Prompt + local LLM response  
│  
├── processing/  
│ ├── chunking.py  
│ └── embedding.py  
│  
└── ingestion/  
└── pdf\_reader.py


### Vector indexes are stored dynamically at:

data/vector\_store/<pdf\_name>/  
├── index.faiss  
└── metadata.json

## How It Works

### 1. Indexing
- PDF text is extracted and cleaned
- Text is chunked with overlap
- Each chunk is embedded
- FAISS index + metadata are saved per PDF

### 2. Retrieval
- User question is embedded
- FAISS retrieves top-k relevant chunks
- Chunk text + metadata are returned

### 3. Answer Generation
- Retrieved chunks are formatted as context
- A prompt is built
- A **local LLM** generates the final answer


## Usage (Please read this carefuuly)

### 1. Place PDFs
Put your PDFs in: data/pdfs/


### 2. Run the application
```
python run.py
```
### 3. Select a PDF

You will be prompted to choose a document to index.

### 4. Ask Questions

Once indexing completes, ask natural-language questions about the document.

Type ```exit``` to quit.

## Example Interaction
```
Welcome to PDF Guru

Select PDF:
[1] research_paper.pdf
[2] business_report.pdf

> What is the document about?

Answer:
The document outlines...

Sources:
- business_report.pdf | Page 3
- business_report.pdf | Page 5
```

## Local LLM Setup

This project assumes a local LLM runtime, such as:

* Ollama (recommended)

* llama.cpp-compatible models

Configure your local model in ```app_config.py```:
```
LLM_BACKEND = "local"
LLM_MODEL_NAME = "llama3"
```

You are free to swap models without changing the pipeline.

## Why This Project Exists

* To demonstrate proper RAG architecture

* To show retrieval-first design

* To avoid LLM hallucination

* To work offline and privately

* To be understandable, debuggable, and extensible

## Future Improvements

* Multi-PDF sessions

* Web UI (Streamlit / FastAPI)

* Index reuse detection

* Streaming LLM responses

* Citations in generated answers

## Disclaimer

This project is intended for educational and experimental purposes.
Accuracy depends entirely on document quality and retrieval performance.
