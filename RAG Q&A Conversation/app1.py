import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.core.prompts import ChatPromptTemplate
from langchain.chains import conversational_retrieval
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv  import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv['GROQ_API_KEY']
groq_api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.3-70b-versatile")
prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided ontext only.
    please provide the mostaccurate response based on th equestion
    <context>
    {context}
    Question:{input}
    """
)
def create_vector_embedding():
    #create the session state :session state acually hrlps you to remember your vectore
    #storeDB specifically for vector
    #session state variables will be able to access in their function and alsoo whenver it is required
    if "vectors" not in st.session_state:
        st.session_state.embeddings=OllamaEmbeddings()
        st.session_state.loader=PyPDFDirectoryLoader("")