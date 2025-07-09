---

### `README.md`

```markdown
# 🧪 SPA con Vanilla JavaScript

Este proyecto es una **Single Page Application (SPA)** simple construida sin frameworks (ni React, ni Vue, ni Angular). Utiliza solo HTML, CSS y JavaScript moderno (ES Modules) para gestionar rutas y vistas dinámicamente.

---

## Estructura del Proyecto

```

spa-vanilla/
│
├── index.html
├── main.js
├── router.js
└── views/
  ├── home.js
  ├── about.js
  └── notfound.js

├
├


````

---

## index.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SPA</title>
  <style>
    nav a {
      margin-right: 10px;
    }
  </style>
</head>
<body>
  <nav>
    <a href="/" data-link>Inicio</a>
    <a href="/about" data-link>Acerca de</a>
    <a href="/no-existe" data-link>404</a>
  </nav>

  <div id="app"></div>

  <script type="module" src="main.js"></script>
</body>
</html>
````

---

## main.js

```js
import { router } from './router.js';

// Interceptar clics en los links internos
document.addEventListener('click', (e) => {
  if (e.target.matches('[data-link]')) {
    e.preventDefault();
    history.pushState(null, null, e.target.href);
    router();
  }
});

// Manejo del botón "atrás" y "adelante"
window.addEventListener('popstate', router);

// Carga inicial
document.addEventListener('DOMContentLoaded', router);
```

---

## router.js

```js
import Home from './views/home.js';
import About from './views/about.js';
import NotFound from './views/notfound.js';

const routes = {
  '/': Home,
  '/about': About,
};

export function router() {
  const path = window.location.pathname;
  const view = routes[path] || NotFound;

  document.getElementById('app').innerHTML = view();
}
```

---

## views/home.js

```js
export default function Home() {
  return `
    <h1>Página de Inicio</h1>
    <p>Bienvenido a la SPA con Vanilla JS.</p>
  `;
}
```

---

## views/about.js

```js
export default function About() {
  return `
    <h1>Acerca de</h1>
    <p>Esta SPA fue construida sin frameworks.</p>
  `;
}
```

---

## views/notfound.js

```js
export default function NotFound() {
  return `
    <h1>404 - Página no encontrada</h1>
    <p>La ruta que estás buscando no existe.</p>
  `;
}
```

---

## Mejoras a implementar en la sesión

* Rutas con parámetros dinámicos (`/user/:id`)
* Fetch de datos externos desde APIs
* Componentes reutilizables
* Lazy loading de vistas
* Loader/Spinner al cargar rutas

---