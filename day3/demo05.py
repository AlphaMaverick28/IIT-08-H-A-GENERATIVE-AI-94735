import os
import requests
import json

api_key = "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"
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

user_prompt = input("Ask anything: ")
req_data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        { "role": "user", "content": user_prompt }
    ],
}

response = requests.post(url, data=json.dumps(req_data), headers=headers)
print("Status:", response.status_code)
print(response.json())