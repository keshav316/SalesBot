# SalesBot Setup and Execution Guide

SalesBot is a hybrid RAG (Dense AstraDB + Sparse BM25 Keyword Search) AI Sales Assistant. It retrieves product data and streams responses to customers in real-time.

## Prerequisites

- **Python**: version 3.11
- **Conda** (recommended) or **pip**
- **AstraDB Account** (for vector storage)
- **Groq Cloud API Key** (for Llama 3.3 model execution)
- **Hugging Face Hub API Token** (for generating embeddings)

---

## 1. Environment Setup

### Using Conda (Recommended)

1. Create a Conda environment and install Python:
   ```bash
   conda create -n salesBot python=3.12 -y
   ```
2. Activate the environment:
   ```bash
   conda activate salesBot
   ```
3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Using pip and venv

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 2. Configuration (`.env`)

Create or update the `.env` file in the root directory and ensure the following keys are correctly configured:

```env
CHATBOT_DB_URL="<your_astradb_api_endpoint>"
CHATBOT_DB_TOKEN="<your_astradb_application_token>"
GROQ_API="<your_groq_api_key>"
HUGGINGFACEHUB_API_TOKEN="<your_huggingface_api_token>"
```

---

## 3. Knowledge Base Construction

To build the knowledge base hybrid retriever cache, make sure you have ingested the product catalog first:
```bash
python ingest.py
```
*(Ensure `bm25_corpus.pkl` is generated in the root directory)*.

---

## 4. Running the Chatbot

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

Once started, open your web browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 5. Streaming & Interface Design

- **Real-Time Streaming**: The bot streams answers directly to the user interface character-by-character.
- **Dynamic Loader**: When you ask a query, the loader displays and blurs the screen. The screen automatically unblurs and the loader disappears as soon as the first character/chunk is generated.
- **Stdout Flushing**: The backend logs are flushed in real-time with `flush=True` in the terminal output.
