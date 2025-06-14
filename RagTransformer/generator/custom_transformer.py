from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class CustomTransformer:
    def __init__(self, model_name="google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_response(self, context, question, max_len=2048):
        prompt = f"Context: {context}\nQuestion: {question}\nProvide a detailed answer:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
        output = self.model.generate(
        **inputs,
        max_length=max_len,
        min_length=60,  # Force minimum 60 tokens
        num_beams=4,
        do_sample=True,  # Enable sampling
        temperature=0.7,  # Add randomness
        top_p=0.9,  # Nucleus sampling
        no_repeat_ngram_size=2,
        early_stopping=False,  # Don't stop early
        length_penalty=1.3,  # Encourage longer responses
        repetition_penalty=1.1
    )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
