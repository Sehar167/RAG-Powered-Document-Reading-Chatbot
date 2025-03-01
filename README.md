# RAG-Powered Document Reading Chatbot with LangChain and Google Gemini Pro

## Overview
The **RAG-Powered Document Reading Chatbot** is an advanced AI-driven chatbot that enables users to upload documents (up to 200MB) and interactively extract relevant information. Using **Retrieval-Augmented Generation (RAG)**, the chatbot efficiently retrieves content from documents and vector databases, ensuring accurate and context-aware responses.

## Features
✅ **Upload & Read Documents** – Supports PDF uploads up to **200MB**.  
✅ **Extract Relevant Information** – Retrieves specific content from uploaded files.  
✅ **RAG-Based Enhanced Responses** – Uses vector search and **LLM reasoning** for precise answers.  
✅ **API Key Integration** – Users can input their **Google Generative AI API Key** for authentication.  
✅ **Real-Time Q&A** – Ask questions and receive intelligent responses based on document content.  

## Technologies Used
- **LangChain** – Implements **RAG** for improved document retrieval and reasoning.
- **Google Gemini Pro** – Enhances understanding and response generation.
- **Streamlit** – Provides an intuitive and interactive **web interface** for document uploads and Q&A.
- **FAISS (Facebook AI Similarity Search)** – Used as a **vector database** for efficient document retrieval.
- **PyPDF** – Extracts text from **PDF documents**.
- **Hugging Face Transformers** – Used for **embedding and document processing**.
- **Google Generative AI API** – Enables **integration with Gemini Pro** for response generation.

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed along with the required dependencies.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/RAG-Document-Chatbot.git
cd RAG-Document-Chatbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Google Gemini Pro API Key
Obtain your **Google Generative AI API Key** from [Google AI](https://ai.google.dev/) and set it up:
```bash
export GOOGLE_GEMINI_API_KEY='your-api-key-here'  # For Linux/Mac
set GOOGLE_GEMINI_API_KEY='your-api-key-here'      # For Windows (CMD)
```
Alternatively, store the API key in a **.env** file.

### 4️⃣ Run the Chatbot
```bash
streamlit run app.py
```

## Usage
1. **Upload a Document** – Click on the upload button and select a PDF.
2. **Ask Questions** – Enter your query in the chatbox.
3. **Get Context-Aware Answers** – The chatbot retrieves relevant information using RAG.

## Future Enhancements
🚀 **Support for More File Formats** (Word, Excel, TXT).  
🚀 **Improved Multi-Document Search** – Search across multiple uploaded documents.  
🚀 **Advanced NLP Features** – Summarization, entity recognition, and deeper semantic search.  

## Contribution
Feel free to **fork the repository**, submit pull requests, and suggest improvements!

## License
This project is licensed under the **MIT License**.

---
💡 **Developed with ❤️ using LangChain, Google Gemini Pro & Streamlit** 🚀

