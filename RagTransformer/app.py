import streamlit as st
import os
from dotenv import load_dotenv
from pipeline import RAGPipeline

# Load API key
load_dotenv("./RagTransformer/safe.env")
api_key = os.getenv("SERPAPI_KEY")

# Initialize RAG
rag = RAGPipeline(api_key)

# UI Layout
st.set_page_config(page_title="RAG Transformer", layout="centered")
st.title("🔍 RAG Transformer")
st.caption("Powered by SerpAPI + FLAN-T5")

query = st.text_input("Enter your question:", "What is latent diffusion?")

if st.button("Generate Answer") and query:
    with st.spinner("Generating answer..."):
        answer = rag.run(query)
        st.subheader("📢 Answer")
        st.write(answer)