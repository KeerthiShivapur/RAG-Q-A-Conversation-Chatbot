# Q-A-Conversation-Chatbot
# 📘 Conversational RAG With PDF Uploads & Chat History

This project is a Streamlit-based Conversational RAG (Retrieval-Augmented Generation) application that allows users to upload PDF files and chat with their content. It uses ChromaDB, HuggingFace Embeddings, and Groq Llama-3.3-70B to deliver fast, context-aware answers with full chat history memory.

🚀 Features

Upload one or multiple PDF files

Extract and chunk text for efficient retrieval

Generate embeddings using HuggingFace MiniLM

Store vectors in ChromaDB

Conversational RAG with chat history memory (Session-based)

Ultra-fast LLM responses using Groq Llama-3.3-70B

Simple and clean Streamlit UI
📂 Project Structure
app.py               # Main Streamlit RAG application
requirements.txt     # All Python dependencies
temp.pdf             # Temporary file used during PDF processing

# Installation
pip install -r requirements.txt

# ▶️ Running the Project
streamlit run app.py

📝 How to Use the App

Run the app

Enter your Groq API key

Enter a Session ID (example: session1)

Upload PDFs

Ask questions

Chat history is stored and used for answering future queries
