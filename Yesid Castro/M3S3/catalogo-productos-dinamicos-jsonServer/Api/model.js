export async function getProducts() {
    const response = await fetch(`http://localhost:3000/productos`);
    const products = await response.json();
    return products;
}