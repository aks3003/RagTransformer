## 🧠 RAG ChatBot — Retrieval-Augmented Generation using SerpAPI + FLAN-T5

### 🔍 Ask real-world questions and get contextual, summarized answers — powered by **RAG**, **SerpAPI**, and **Transformers**.

---

### 📌 Overview

**RAG ChatBot** is a custom Retrieval-Augmented Generation system built with:

* 🔎 **SerpAPI** for real-time search-based retrieval
* 🧠 **FLAN-T5 (Seq2Seq Transformer)** for intelligent answer generation
* 🌐 **Streamlit** for an interactive UI
* 💪 Designed to help users ask open-ended questions and receive detailed, context-rich responses in natural language.

---

### 🧠 How It Works

```
        ┌──────────────┐      ┌──────────────┐      ┌─────────────────────────────┐
        │ User Query │ ──▶  │ SerpAPI Web  │ ──▶  │ Snippet Preprocessing  │
        └──────────────┘      └──────────────┘      └──────────────┌───────┘
                                                               ▼
                                                   ┌──────────────────────────┐
                                                   │  FLAN-T5 Transformer   │
                                                   │ (Context + Generation) │
                                                   └──────────────────────┘
                                                                ▼
                                                     📢 Final Answer Shown
```

---

### 🔧 Tech Stack

* **Retriever**: [SerpAPI](https://serpapi.com/)
* **Generator**: [FLAN-T5 Transformer](https://huggingface.co/google/flan-t5-base)
* **Frameworks**: `transformers`, `torch`, `streamlit`, `dotenv`
* **Environment**: Python 3.10+

---

### 📁 Project Structure

```
rag_transformer_project/
├── main.py                     # CLI chatbot interface
├── app.py                      # Streamlit-based UI
├── pipeline.py                 # End-to-end RAG controller
├── retriever/
│   └── serpapi_retriever.py    # Web search retriever using SerpAPI
├── generator/
│   └── custom_transformer.py   # FLAN-T5 based response generator
├── preprocess.py               # Snippet preprocessor
├── RagTransformer/
│   └── safe.env                # 🔐 SerpAPI key (not tracked)
├── requirements.txt
└── .gitignore
```

---

### 🚀 Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-transformer-chatbot.git
cd rag-transformer-chatbot
```

#### 2. Set Up the Environment

```bash
pip install -r requirements.txt
```

#### 3. Add Your SerpAPI Key

Create a file at: `./RagTransformer/safe.env`

```env
SERPAPI_KEY=your_serpapi_key_here
```

#### 4. Run the CLI Version

```bash
python main.py
```

#### 5. Run the Streamlit UI

```bash
streamlit run app.py
```

---

### 💡 Features

* ✅ Uses real-time data from Google Search
* ✅ Summarizes context from multiple sources
* ✅ FLAN-T5 answers in a coherent, human-like way
* ✅ Streamlit interface with nice styling
* ✅ Easy to extend with your own LLMs or retrieval sources

---

### 📛 Example Queries

> 🗪 What is latent diffusion?

> 🧑‍💻 How does federated learning work?

> 📈 What are the current trends in GenAI research?

---

### 🎓 Ideal For

* Final-year Machine Learning / NLP projects
* Research Prototypes for Knowledge-Augmented QA
* Personal knowledge assistants
* Showcasing skills in Transformers, APIs, and Full-Stack ML

---

### 🔐 Security Note

* API keys are loaded securely from `safe.env`
* `.gitignore` ensures `.env` files are not pushed

---

### 🛠 Future Enhancements

* [ ] Add reference links to responses
* [ ] Use vector databases (e.g., FAISS) for persistent retrieval
* [ ] Add model fine-tuning on QA datasets
* [ ] Add support for multi-turn dialogue (RAG Chat History)

---

### ❤️ Made by Akshith Mynampati

Feel free to fork, extend, or integrate with other RAG/LLM systems.
**Questions? Contributions?** Ping me on GitHub or LinkedIn!
