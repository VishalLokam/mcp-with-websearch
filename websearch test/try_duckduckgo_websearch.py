from ddgs import DDGS

results = DDGS().text(
    query="python programming",
    region="us-en",
    safesearch="moderate",
    backend="duckduckgo",
    max_results=5,
)

for result in results:
    print(result["body"])
