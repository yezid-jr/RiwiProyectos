import { getProducts} from "./model.js";
import { showCard } from "./view.js";

const app = document.getElementById("card");

async function init() {
    const productos = await getProducts();
    showCard(app, productos);
}

init().catch(error => {
    console.error("Error al inicializar la aplicación:", error);
    app.innerHTML = "<p>Error al cargar los productos.</p>";
});