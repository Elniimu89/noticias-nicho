import requests
import json
import os

API_KEY = os.getenv("NEWS_API_KEY") or "TU_API_KEY_AQUI"

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "category": "general",
    "pageSize": 10,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
news_data = response.json()

noticias = []
for article in news_data.get("articles", []):
    noticias.append({
        "titulo": article["title"],
        "descripcion": article["description"],
        "url": article["url"],
        "imagen": article["urlToImage"],
        "fecha": article["publishedAt"]
    })

with open("data/noticias.json", "w", encoding="utf-8") as f:
    json.dump(noticias, f, ensure_ascii=False, indent=2)

print(f"{len(noticias)} noticias guardadas correctamente.")
