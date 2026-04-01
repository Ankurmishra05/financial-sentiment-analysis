from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class NewsInput(BaseModel):
    headline: str

@app.get("/")
def home():
    return {"message": "Financial Sentiment API Running 🚀"}

@app.post("/predict")
def get_sentiment(data: NewsInput):
    sentiment = predict(data.headline)

    # Trading logic (BONUS 🔥)
    if sentiment == "positive":
        action = "BUY"
    elif sentiment == "negative":
        action = "SELL"
    else:
        action = "HOLD"

    return {
        "headline": data.headline,
        "sentiment": sentiment,
        "action": action
    }