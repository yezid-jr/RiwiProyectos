export function showCard(container, productos) {
    container.innerHTML = productos.map(product => `
        <div class="card">
            <div class="card-img">
                <div class="img">
                    <img src="${product.img}" alt="${product.nombre}">
                </div>
            </div>
            <div class="card-title">${product.nombre}</div>
            <div class="card-subtitle">${product.descripcion}</div>
            <hr class="card-divider">
            <div class="card-footer">
            <div class="card-price"><span>$</span>${product.precio}</div>
            <button class="card-btn">
            <!-- SVG botón -->
            </button>
            </div>
        </div>
  `).join('');
}
