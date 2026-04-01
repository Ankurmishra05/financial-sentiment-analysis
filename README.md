# Financial Sentiment Analysis (Real-Time)

A production-style NLP system that analyzes financial news headlines and generates sentiment-driven trading signals in real time.

---

## Overview

Most sentiment analysis models fail in financial contexts because they are trained on general text.
This project uses **FinBERT**, a domain-specific transformer model trained on financial data, to improve prediction relevance.

The system fetches live headlines, processes them through the model, and exposes results via an API and dashboard.

---

## System Design

The project is structured as a simple end-to-end pipeline:

* **Data Source** → NewsAPI (live financial headlines)
* **Model Layer** → FinBERT (Hugging Face Transformers)
* **Inference Layer** → PyTorch (CPU inference)
* **Backend** → FastAPI (REST API)
* **Frontend** → Streamlit (dashboard UI)

---

## Features

* Real-time financial news ingestion
* Domain-specific sentiment classification
* Trading signal mapping (BUY / SELL / HOLD)
* REST API for inference
* Interactive dashboard for visualization

---

## API Endpoints

### `POST /predict`

Predict sentiment for a single headline

```json
{
  "headline": "Stock market rises after strong earnings"
}
```

---

### `GET /live-news`

Fetch latest headlines with sentiment + trading signals

---

## Running Locally

```bash
git clone https://github.com/Ankurmishra05/financial-sentiment-analysis.git
cd financial-sentiment-analysis

pip install -r requirements.txt
uvicorn api.app:app --reload
```

API docs:
http://127.0.0.1:8000/docs

---

## Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

## Key Decisions

* **FinBERT over BERT**
  General models underperform on financial text. FinBERT improves domain accuracy.

* **Inference over training**
  Avoided retraining to keep system lightweight and deployable on CPU.

* **Modular design**
  Separated data, model, and API layers for clarity and extensibility.

---

## Limitations

* NewsAPI has request limits (free tier)
* No aggregation across multiple headlines yet
* No historical sentiment tracking

---

## Future Work

* Aggregate sentiment across multiple sources
* Add time-series sentiment trends
* Integrate stock price correlation
* Replace Streamlit with React-based frontend

---

## Author

Ankur Mishra
