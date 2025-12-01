fetch("../data/noticias.json")
  .then(response => response.json())
  .then(noticias => {
    const contenedor = document.getElementById("noticias");
    noticias.forEach(noticia => {
      const div = document.createElement("div");
      div.className = "noticia";
      div.innerHTML = `
        <img src="${noticia.imagen || ''}" alt="">
        <h3>${noticia.titulo}</h3>
        <p>${noticia.descripcion}</p>
        <a href="${noticia.url}" target="_blank">Leer más</a>
      `;
      contenedor.appendChild(div);
    });
  });
