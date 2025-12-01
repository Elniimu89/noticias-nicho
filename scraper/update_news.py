import os
import requests
import json
from datetime import datetime

# Leer clave desde variable de entorno
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    print("❌ No se encontró la API KEY. Asegúrate de tener NEWS_API_KEY definida.")
    exit(1)

# URL de noticias globales en español
URL = f"https://newsapi.org/v2/top-headlines?language=es&pageSize=8&apiKey={API_KEY}"

# Solicitar noticias
response = requests.get(URL)
data = response.json()

if data.get("status") != "ok":
    print("❌ Error al obtener noticias:", data.get("message"))
    exit(1)

articles = data.get("articles", [])
if not articles:
    print("⚠️ No se encontraron noticias.")
    exit(0)

# Procesar noticias
noticias = []
for article in articles:
    noticias.append({
        "titulo": article.get("title"),
        "descripcion": article.get("description"),
        "url": article.get("url"),
        "imagen": article.get("urlToImage"),
        "fecha": article.get("publishedAt")
    })

# Ruta para archivo web
output_web = "public/data/noticias.json"
os.makedirs(os.path.dirname(output_web), exist_ok=True)

# Guardar archivo web
with open(output_web, "w", encoding="utf-8") as f:
    json.dump(noticias, f, indent=2, ensure_ascii=False)

# Guardar archivo histórico con fecha
fecha_hoy = datetime.today().strftime("%Y-%m-%d")
output_historial = f"scraper/historial/noticias_{fecha_hoy}.json"
os.makedirs(os.path.dirname(output_historial), exist_ok=True)

with open(output_historial, "w", encoding="utf-8") as f:
    json.dump(noticias, f, indent=2, ensure_ascii=False)

print(f"✅ {len(noticias)} noticias guardadas en:")
print(f"   - {output_web}")
print(f"   - {output_historial}")
