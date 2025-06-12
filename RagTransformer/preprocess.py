def preprocess(snippets, chunk_size=250):
    joined = " ".join(snippets)
    return [joined[i:i+chunk_size] for i in range(0, len(joined), chunk_size)]
