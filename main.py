from fastapi import FastAPI
from pydantic import BaseModel
import requests, os

app = FastAPI()

class TextIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: TextIn):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": data.text})
    summary = response.json()
    return {"summary": summary[0]["summary_text"]}
