from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os

MODEL_PATH = "models/finbert_model"

model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)

device = torch.device("cpu")
model.to(device)
model.eval()

labels = ["negative", "neutral", "positive"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    predicted_class = torch.argmax(probs, dim=1).item()

    return labels[predicted_class]