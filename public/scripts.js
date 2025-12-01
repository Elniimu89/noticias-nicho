document.addEventListener("DOMContentLoaded", () => {
  const categorias = [
    "policiales", "espectaculos", "videojuegos", "peliculas", "series",
    "politica", "medio ambiente", "salud", "finanzas", "tecnologia",
    "ciencia", "deportes", "internacionales", "educacion", "cultura"
  ];

  const menu = document.getElementById("menu-categorias");
  categorias.forEach((cat) => {
    const li = document.createElement("li");
    li.innerHTML = `<a href="#" onclick="cargarCategoria('${cat}')">${capitalizar(cat)}</a>`;
    menu.appendChild(li);
  });

  // Cargar por defecto "tecnologia"
  cargarCategoria("tecnologia");
});

function cargarCategoria(cat) {
  fetch(`data/${cat}.json`)
    .then((res) => res.json())
    .then((noticias) => mostrarNoticias(noticias, cat))
    .catch((err) => {
      console.error("Error al cargar categoría:", err);
      document.getElementById("noticias").innerHTML = `<p>No se pudieron cargar noticias de ${cat}.</p>`;
    });
}

function mostrarNoticias(noticias, categoria) {
  const contenedor = document.getElementById("noticias");
  contenedor.innerHTML = "";

  noticias.forEach((noticia) => {
    const card = document.createElement("div");
    card.classList.add("noticia");

    card.innerHTML = `
      <img src="${noticia.imagen}" alt="Imagen de noticia">
      <h3>${noticia.titulo}</h3>
      <p>${noticia.descripcion || "Sin descripción disponible."}</p>
      <a href="${noticia.url}" target="_blank">Leer más</a>
      <p class="fecha">${formatearFecha(noticia.fecha)}</p>
    `;

    contenedor.appendChild(card);
  });
}

function capitalizar(texto) {
  return texto.charAt(0).toUpperCase() + texto.slice(1);
}

function formatearFecha(fechaISO) {
  const fecha = new Date(fechaISO);
  return fecha.toLocaleDateString("es-ES", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}
