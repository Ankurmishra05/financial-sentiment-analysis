import os
import gdown
import zipfile
import shutil
from transformers import BertTokenizer, BertForSequenceClassification
import torch

BASE_PATH = "models"

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH, exist_ok=True)

MODEL_PATH = os.path.join(BASE_PATH, "finbert_model")

# Download if not exists
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=13WAsFFupP_Ju5JcqsPTZnMm9CaQt5exn"
    output = os.path.join(BASE_PATH, "model.zip")

    gdown.download(url, output, quiet=False)

    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(BASE_PATH)

    os.remove(output)

    # 🔥 AUTO FIX: find correct folder
    for root, dirs, files in os.walk(BASE_PATH):
        if "config.json" in files:
            print("Found model at:", root)
            if root != MODEL_PATH:
                if os.path.exists(MODEL_PATH):
                    shutil.rmtree(MODEL_PATH)
                shutil.move(root, MODEL_PATH)
            break

# Final check
if not os.path.exists(os.path.join(MODEL_PATH, "config.json")):
    raise Exception("Model not properly loaded")

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