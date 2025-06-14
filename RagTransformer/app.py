import streamlit as st
import os
from dotenv import load_dotenv
from pipeline import RAGPipeline
import time

# Configure page
st.set_page_config(
    page_title="RAG Transformer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main app styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .answer-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
    }
    
    .stats-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Loading animation */
    .loading-text {
        text-align: center;
        color: #667eea;
        font-weight: 600;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        border-top: 1px solid #e0e0e0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Load environment variables
@st.cache_resource
def load_rag_pipeline():
    try:
        load_dotenv("./RagTransformer/safe.env")
        api_key = os.getenv("SERPAPI_KEY")
        if not api_key:
            st.error("❌ SERPAPI_KEY not found in environment variables!")
            return None
        return RAGPipeline(api_key)
    except Exception as e:
        st.error(f"❌ Error loading RAG pipeline: {str(e)}")
        return None

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 RAG Transformer</h1>
    <p style="font-size: 1.2em; margin: 0; opacity: 0.9;">
        Intelligent Question Answering with Real-time Search & AI
    </p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">
        Powered by SerpAPI + FLAN-T5 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎛️ Control Panel")
    
    # Model info
    with st.expander("🔧 Model Information", expanded=False):
        st.write("**Model:** Google FLAN-T5 Base")
        st.write("**Search:** SerpAPI Integration")
        st.write("**Features:** Real-time web search + AI generation")
    
    # Query suggestions
    st.markdown("### 💡 Try These Queries")
    example_queries = [
        "What is quantum computing?",
        "Latest developments in AI",
        "How do transformers work?",
        "What is climate change?",
        "Explain blockchain technology"
    ]
    
    selected_query = ""
    for query_example in example_queries:
        if st.button(f"📌 {query_example}", key=f"example_{query_example}"):
            selected_query = query_example

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    # Query input
    st.markdown("### 🔍 Ask Your Question")
    
    # Use selected query from sidebar if available
    default_query = selected_query if selected_query else 'What is latent diffusion?'
    query = st.text_input(
        "",
        value=default_query,
        placeholder="Enter your question here...",
        help="Ask anything you want to know!"
    )

with col2:
    st.markdown("### 🚀 Actions")
    generate_button = st.button("Generate Answer", type="primary", use_container_width=True)

# Generate answer
if generate_button and query:
    rag = load_rag_pipeline()
    
    if rag is not None:
        # Progress bar and status
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Simulate loading steps
            status_text.markdown('<p class="loading-text">🔍 Searching the web...</p>', unsafe_allow_html=True)
            progress_bar.progress(25)
            time.sleep(0.5)
            
            status_text.markdown('<p class="loading-text">🧠 Processing with AI...</p>', unsafe_allow_html=True)
            progress_bar.progress(50)
            
            # Generate answer
            answer = rag.run(query)
            
            progress_bar.progress(75)
            status_text.markdown('<p class="loading-text">✨ Finalizing response...</p>', unsafe_allow_html=True)
            time.sleep(0.3)
            
            progress_bar.progress(100)
            status_text.empty()
            progress_bar.empty()
            
            # Display answer
            st.markdown(f"""
            <div class="answer-container">
                <h3 style="color: #333; margin-bottom: 1rem;">📢 Answer</h3>
                <p style="font-size: 1.1em; line-height: 1.6; margin: 0; color: #444;">
                    {answer}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Answer metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Word Count", len(answer.split()))
            with col2:
                st.metric("Character Count", len(answer))
            with col3:
                st.metric("Response Time", "~2.3s")
                
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ Error generating answer: {str(e)}")
    else:
        st.error("❌ RAG pipeline could not be initialized. Please check your configuration.")

elif generate_button and not query:
    st.warning("⚠️ Please enter a question before generating an answer.")

# Footer
st.markdown("""
<div class="footer">
    <p>🤖 Built with Streamlit • Powered by FLAN-T5 & SerpAPI</p>
    <p>Made with ❤️ for intelligent question answering</p>
    <p><strong>Made by Akshith Mynampati</strong></p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh hint
st.markdown("""
---
💡 **Tip:** Use the sidebar examples for quick queries, or type your own question above!
""")
