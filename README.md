#  Production-Ready RAG Assistant

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.5--Flash-orange.svg)](https://ai.google.dev)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-yellow.svg)](https://chromadb.dev)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade Retrieval-Augmented Generation (RAG) backend built with FastAPI, Google Gemini AI, and ChromaDB. Features secure OAuth2 JWT Authentication, multi-format document ingestion, semantic chunking, and grounded question answering.

---

##  Key Features

-**OAuth2 JWT Authentication** — Secure user registration, password hashing with bcrypt, and token-based access control.
-**Document Processing & Chunking** — Automated text extraction from PDF/Text documents with chunking and overlap for maximum context retention.
-**Gemini AI Integration** — Utilizes Google Gemini embeddings for vectorization and Gemini models for precise, hallucination-resistant answers.
- **Persistent Vector Database** — ChromaDB vector storage for cosine similarity and top-k semantic search.
- **Pydantic Validation** — Strict request and response validation with descriptive HTTP status codes.

---

##  Architecture Flow

```
┌─────────────────────────────────────────────────────────────┐
│                          CLIENT                             │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       FastAPI Backend                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────┐  │
│  │ /documents/upload│  │     /query/      │  │   /auth   │  │
│  └────────┬─────────┘  └────────┬─────────┘  └─────┬─────┘  │
└───────────┼─────────────────────┼──────────────────┼────────┘
            │ (Protected)         │ (Protected)      │ (JWT)
            ▼                     ▼                  ▼
┌──────────────────┐    ┌──────────────────┐  ┌───────────────┐
│ Ingestion Engine │    │ RAG Query Engine │  │ Core Security │
│  (PDF/Doc Parser)│    │  (Embedding &    │  │ (bcrypt/Jose) │
└───────────┬──────┘    │   LLM Synthesis) │  └───────────────┘
            │                   ▲        ▲
            ▼                   │        │
   ┌─────────────────┐          │        ▼
   │ Semantic Chunks │──────────┤   ┌────────────────┐
   └────────┬────────┘          │   │ Google Gemini  │
            ▼                   │   │   (LLM API)    │
   ┌─────────────────┐          │   └────────────────┘
   │    ChromaDB     │──────────┘
   │ (Vector Store)  │
   └─────────────────┘
```

---

##  Project Structure

```
production-rag-assistant/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── query.py          # Question answering
│   │       └── documents.py      # File upload & processing
│   ├── core/
│   │   └── auth.py               # JWT token & bcrypt
│   ├── models/
│   │   └── response.py           # Pydantic schemas
│   ├── services/
│   │   ├── chunking.py           # Document splitting
│   │   ├── embedding.py          # Gemini embeddings
│   │   ├── rag_pipeline.py       # LLM synthesis
│   │   └── vector_store.py       # ChromaDB client
│   └── main.py                   # FastAPI app
├── requirements.txt
├── .env.example
└── README.md
```

---

##  Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/production-rag-assistant.git
cd production-rag-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
SECRET_KEY=super-secret-rag-assistant-key-12345
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

Server will start at: `http://127.0.0.1:8000`

---

##  API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/register` | Register a new user |  No |
| POST | `/auth/login` | Login & get JWT token |  No |
| POST | `/documents/upload` | Upload and process document |  Yes |
| POST | `/query/` | Ask questions |  Yes |

---

##  Example Usage

### 1. Upload Document
```http
POST /documents/upload
Authorization: Bearer <your-token>
Content-Type: multipart/form-data
```

### 2. Query Assistant
**Request:**
```json
POST /query/
{
  "query": "What is python?",
  "top_k": 3
}
```

**Response:**
```json
{
  "query": "What is python?",
  "answer": "Python is a high-level, interpreted, general-purpose programming language known for its simplicity and readability.........",
  "model": "gemini-flash-latest"
}
```

---

##  Testing with Swagger UI

1. Open `http://127.0.0.1:8000/docs`
2. Register a user via `POST /auth/register`
3. Click **Authorize** () and login
4. Upload a document using `POST /documents/upload`
5. Query using `POST /query/`

---

##  License

Distributed under the MIT License. See `LICENSE` for more information.

---

> **Built with  using FastAPI, Gemini AI, and ChromaDB**