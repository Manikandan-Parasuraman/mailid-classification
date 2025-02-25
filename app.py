from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load Hugging Face model and force CPU
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)

@app.get("/")
def home():
    return {"message": "Hugging Face API is running on CPU"}

@app.post("/classify/")
def classify_email(email: str):
    domain = email.split("@")[-1]
    labels = ["organization email", "public email"]
    result = classifier(domain, labels)

    return {
        "domain": domain,
        "label": result["labels"][0],
        "confidence": result["scores"][0]
    }
