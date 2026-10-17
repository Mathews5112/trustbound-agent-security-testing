import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",
    "prompt": "Explain a failed SSH login in one sentence.",
    "stream": False
}

response = requests.post(
    url,
    json=payload,
    timeout=120
)
response.raise_for_status()

print(response.json()["response"])