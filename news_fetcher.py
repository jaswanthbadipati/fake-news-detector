import requests
import torch
import torch.nn.functional as F

def get_news(query, api_key="991ac0c2e1a54c91bd36d9f27b8ccb00"):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&sortBy=publishedAt&apiKey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("articles", [])
    except Exception as e:
        print("News fetch error:", e)
        return []

from transformers import pipeline

# Load the fine-tuned model
model_name = "jy46604790/Fake-News-Bert-Detect"
clf = pipeline("text-classification", model=model_name, tokenizer=model_name)

def predict_news(text):
    result = clf(text)[0]
    label = "Real" if result['label'] == 'LABEL_1' else "Fake"
    confidence = round(result['score'] * 100, 2)
    return label, confidence

