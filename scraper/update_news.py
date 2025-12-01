import os
import requests
import json
from datetime import datetime

# Leer API key desde variable de entorno
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    print("❌ No se encontró la API KEY. Asegúrate de tener NEWS_API_KEY definida.")
    exit(1)

# Consulta usando el endpoint 'everything'
query = "noticias"
URL = f"https://newsapi.org/v2/everything?q={query}&language=es&sortBy=publishedAt&pageSize=8&apiKey={API_KEY}"

response = requests.get(URL)
data = response.json()

# Validación de error
if data.get("status") != "ok":
    print("❌ Error al obtener noticias:", data.get("message"))
    exit(1)

articles = data.get("articles", [])
if not articles:
    print("⚠️ No se encontraron noticias.")
    exit(0)

# Procesar noticias reales
noticias = []
for article in articles:
    noticias.append({
        "titulo": article.get("title"),
        "descripcion": article.get("description"),
        "url": article.get("url"),
        "imagen": article.get("urlToImage") or "https://via.placeholder.com/300x200?text=Sin+Imagen",
        "fecha": article.get("publishedAt")
    })

# Crear carpeta si no existe y guardar archivo para la web
output_web = "public/data/noticias.json"
os.makedirs(os.path.dirname(output_web), exist_ok=True)
with open(output_web, "w", encoding="utf-8") as f:
    json.dump(noticias, f, indent=2, ensure_ascii=False)

# Guardar historial con fecha
fecha_hoy = datetime.today().strftime("%Y-%m-%d")
output_historial = f"scraper/historial/noticias_{fecha_hoy}.json"
os.makedirs(os.path.dirname(output_historial), exist_ok=True)
with open(output_historial, "w", encoding="utf-8") as f:
    json.dump(noticias, f, indent=2, ensure_ascii=False)

print(f"✅ {len(noticias)} noticias guardadas en:")
print(f"   - {output_web}")
print(f"   - {output_historial}")
