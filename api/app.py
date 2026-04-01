from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict
from news import get_news

app = FastAPI()

# ----------- REQUEST MODEL -----------
class NewsRequest(BaseModel):
    headline: str

# ----------- SINGLE PREDICTION -----------
@app.post("/predict")
def predict_sentiment(request: NewsRequest):
    sentiment, action = predict(request.headline)

    return {
        "headline": request.headline,
        "sentiment": sentiment,
        "action": action
    }

# ----------- LIVE NEWS -----------
@app.get("/live-news")
def live_news():
    headlines = get_news()
    results = []

    for headline in headlines:
        sentiment, action = predict(headline)

        results.append({
            "headline": headline,
            "sentiment": sentiment,
            "action": action
        })

    return results