from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class CustomTransformer:
    def __init__(self, model_name="google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_response(self, context, question, max_len=2048):
        prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
        output = self.model.generate(
            **inputs,
            max_length=max_len,
            num_beams=6,
            no_repeat_ngram_size=3,
            early_stopping=True
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)