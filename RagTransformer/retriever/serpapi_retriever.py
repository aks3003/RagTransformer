from serpapi import GoogleSearch

def fetch_web_snippets(query, api_key, max_results=5):
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": max_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [r["snippet"] for r in results.get("organic_results", []) if "snippet" in r]
