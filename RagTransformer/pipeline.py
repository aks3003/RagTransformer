from retriever.serpapi_retriever import fetch_web_snippets
from preprocess import preprocess
from generator.custom_transformer import CustomTransformer

class RAGPipeline:
    def __init__(self, serpapi_key):
        self.api_key = serpapi_key
        self.generator = CustomTransformer()

    def run(self, query):
        snippets = fetch_web_snippets(query, self.api_key)
        chunks = preprocess(snippets)
        context = " ".join(chunks[:4])  
        return self.generator.generate_response(context, query)
