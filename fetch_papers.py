import requests
import json

def fetch_research_papers(api_key, n):
    base_url = "https://api.crossref.org/works"
    params = {
        'query': ' ',
        'rows': n
    }

    headers = {
        'User-Agent': 'YourAppName/1.0 (your@email.com)',
        'Accept': 'application/json'
    }

    response = requests.get(base_url, params=params, headers=headers)
    data = response.json()

    papers = []
    for item in data.get('message', {}).get('items', []):
        title = item.get('title', [''])[0]
        title = title.strip()
        if len(title) > 0:
            papers.append({"doc": title})

    return papers

def save_to_json(filename, data):
    with open(filename, 'w') as json_file:
        for entry in data:
            json_file.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    api_key = 'YOUR_CROSSREF_API_KEY'  # Replace with your CrossRef API key
    num_papers = 20  # Replace with the desired number of papers

    papers_data = fetch_research_papers(api_key, num_papers)
    save_to_json('examples/data/pathway-docs/research_papers.jsonl', papers_data)