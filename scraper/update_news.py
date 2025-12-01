import os
import requests
import json
from datetime import datetime

API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    print("❌ No se encontró la API KEY.")
    exit(1)

# ✅ NUEVAS 17 CATEGORÍAS COMPLETAS
categorias = [
    "policiales", "espectaculos", "videojuegos", "peliculas", "series",
    "politica", "medioambiente", "salud", "finanzas",
    "tecnologia", "ciencia", "deportes", "cultura",
    "negocios", "economia", "educacion", "internacional"
]

noticias_totales = []

for categoria in categorias:
    print(f"🔍 Buscando noticias de: {categoria}")
    url = f"https://newsapi.org/v2/everything?q={categoria}&language=es&sortBy=publishedAt&pageSize=10&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"❌ Error en la conexión para {categoria}: {e}")
        continue

    if data.get("status") != "ok":
        print(f"❌ Error en categoría '{categoria}': {data.get('message')}")
        continue

    articulos = data.get("articles", [])
    noticias_categoria = []

    for article in articulos:
        noticia = {
            "categoria": categoria,
            "titulo": article.get("title"),
            "descripcion": article.get("description"),
            "url": article.get("url"),
            "imagen": article.get("urlToImage") or "https://via.placeholder.com/300x200?text=Sin+Imagen",
            "fecha": article.get("publishedAt")
        }
        noticias_categoria.append(noticia)
        noticias_totales.append(noticia)

    # Guardar noticias por categoría
    fecha = datetime.today().strftime("%Y-%m-%d")
    ruta_historial = f"scraper/historial/{categoria}_{fecha}.json"
    os.makedirs(os.path.dirname(ruta_historial), exist_ok=True)
    with open(ruta_historial, "w", encoding="utf-8") as f:
        json.dump(noticias_categoria, f, indent=2, ensure_ascii=False)

# Guardar mezcla general para la web
output_web = "public/data/noticias.json"
os.makedirs(os.path.dirname(output_web), exist_ok=True)
with open(output_web, "w", encoding="utf-8") as f:
    json.dump(noticias_totales, f, indent=2, ensure_ascii=False)

print(f"✅ {len(noticias_totales)} noticias guardadas en:")
print(f"   - {output_web}")
print(f"   - scraper/historial/{categoria}_YYYY-MM-DD.json por tema")
