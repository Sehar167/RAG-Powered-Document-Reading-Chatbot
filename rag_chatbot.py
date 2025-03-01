import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os

st.set_page_config(page_title="Doc Read", layout="wide")

st.markdown("""
## Doc Read: Get Insights from your Documents
## How it works
Follow these instrutions
            \n1) Enter your API ket
            \n2) Upload your documnet
            \n3) Ask the queation and Woolaa Doc read will answer your quations in seconds.""")

# api_key = st.text_input("Enter your API key", type="password", key="Api key input")

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extraxt.text()
    return text

def gen_text_chunk(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001", google_api_key = api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """ Answer the question as detailed as possible extracting information from the documnet attached, make sure you provide true details. If the answer is not present in the document donot make a answer instead say that information is not provided the asked topic in the document.
    context:\n (context)?\n
    Question: \n(question)\n

    Answer:
    """
    model = ChatGoogleGenerativeAI (model = "gemini-pro", temperature = 0.3, google_api_key = api_key)
    prompt = prompt_template( template = prompt_template, input_variable = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question, api_key):
    embeddings= GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key = api_key)
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_document": docs, "question": user_question}, return_only_outputs= True)
    st.write("Reply:", response["output_text"])


def main():
    st.header("Document Read App")

    user_question = st.text_input("Ask question you would like to get answer form the PDF file", key="user_question")

    if user_question and api_key:
        user_input(user_question, api_key)

    with st.sidebar:
        st.title("Menu:")
        api_key = st.text_input("Enter your API key", type="password", key="Api key input")
        pdf_docs = st.file_uploader("Upload your docs", accept_multiple_files = True, key = "pdf_uploader")
        if st.button("Submut & process", key="process_button") and api_key:
            with st.spinner("procesing......"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = gen_text_chunk(raw_text)
                get_vector_store(text_chunks, api_key)
                st.success("Done")

if __name__ == "__main__":
    main()