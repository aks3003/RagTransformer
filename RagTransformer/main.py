import os
from dotenv import load_dotenv
from pipeline import RAGPipeline

# ✅ Load env file
load_dotenv("./RagTransformer/safe.env")

serpapi_key = os.getenv("SERPAPI_KEY")

rag_model = RAGPipeline(serpapi_key)

if __name__ == "__main__":
    while True:
        user_input = input("Ask a question (or type 'exit'): ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = rag_model.run(user_input)
        print("\nAnswer:\n" + answer + "\n")