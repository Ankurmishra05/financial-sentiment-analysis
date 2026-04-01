import os
import gdown
import zipfile
from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_PATH = "models/finbert_model"

# Download & extract if not exists
if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)

    url = "https://drive.google.com/uc?id=13WAsFFupP_Ju5JcqsPTZnMm9CaQt5exn"
    output = "models/model.zip"

    gdown.download(url, output, quiet=False)

    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("models")

    os.remove(output)

# 🔥 FIX: ensure correct path
if not os.path.exists(MODEL_PATH):
    raise Exception("Model folder not found after extraction")

# Load model
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