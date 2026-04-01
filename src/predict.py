from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

device = torch.device("cpu")
model.to(device)
model.eval()

labels = ["positive", "negative", "neutral"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    predicted_class = torch.argmax(probs, dim=1).item()
    sentiment = labels[predicted_class]

    if sentiment == "positive":
        action = "BUY"
    elif sentiment == "negative":
        action = "SELL"
    else:
        action = "HOLD"

    return sentiment, action