document.addEventListener("DOMContentLoaded", () => {
  fetch("data/noticias.json")
    .then((res) => res.json())
    .then((noticias) => {
      window.todasLasNoticias = noticias;
      mostrarNoticiasPorCategoria("todas");
    })
    .catch((error) => console.error("Error al cargar noticias:", error));
});

function filtrarCategoria(categoriaSeleccionada) {
  mostrarNoticiasPorCategoria(categoriaSeleccionada);
}

function mostrarNoticiasPorCategoria(categoriaSeleccionada) {
  const contenedor = document.getElementById("noticias");
  contenedor.innerHTML = "";

  const noticiasFiltradas =
    categoriaSeleccionada === "todas"
      ? window.todasLasNoticias
      : window.todasLasNoticias.filter(
          (n) => (n.categoria || "otras") === categoriaSeleccionada
        );

  if (noticiasFiltradas.length === 0) {
    contenedor.innerHTML = `<p>No hay noticias para esta categoría.</p>`;
    return;
  }

  noticiasFiltradas.forEach((noticia) => {
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

function formatearFecha(fechaISO) {
  const fecha = new Date(fechaISO);
  return fecha.toLocaleDateString("es-ES", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}
