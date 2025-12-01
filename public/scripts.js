document.addEventListener("DOMContentLoaded", () => {
  fetch("data/noticias.json")
    .then((res) => res.json())
    .then((noticias) => mostrarNoticiasAgrupadas(noticias))
    .catch((error) => console.error("Error al cargar noticias:", error));
});

function mostrarNoticiasAgrupadas(noticias) {
  const contenedor = document.getElementById("noticias");
  contenedor.innerHTML = "";

  const categoriasAgrupadas = agruparPorCategoria(noticias);

  for (const categoria in categoriasAgrupadas) {
    // Crear título de categoría
    const titulo = document.createElement("h2");
    titulo.textContent = capitalizar(categoria);
    contenedor.appendChild(titulo);

    // Renderizar noticias de la categoría
    categoriasAgrupadas[categoria].forEach((noticia) => {
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
}

function agruparPorCategoria(lista) {
  return lista.reduce((acc, noticia) => {
    const cat = noticia.categoria || "otras";
    if (!acc[cat]) acc[cat] = [];
    acc[cat].push(noticia);
    return acc;
  }, {});
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
