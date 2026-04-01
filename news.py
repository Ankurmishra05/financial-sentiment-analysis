import requests

API_KEY = "0c4a2549afa349c8b277eea8176f83fb"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    headlines = []

    for article in data["articles"][:5]:
        headlines.append(article["title"])

    return headlines