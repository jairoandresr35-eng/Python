// ── Datos de los productos ──
const productos = [
    {
        id: 1,
        nombre: "Producto 1",
        precio: 25000,
        imagen: "https://via.placeholder.com/400",
        descripcion: "Descripción completa del producto 1.",
        caracteristicas: ["Característica 1", "Característica 2", "Característica 3"]
    },
    {
        id: 2,
        nombre: "Producto 2",
        precio: 38000,
        imagen: "https://via.placeholder.com/400",
        descripcion: "Descripción completa del producto 2.",
        caracteristicas: ["Característica 1", "Característica 2", "Característica 3"]
    },
    {
        id: 3,
        nombre: "Producto 3",
        precio: 15000,
        imagen: "https://via.placeholder.com/400",
        descripcion: "Descripción completa del producto 3.",
        caracteristicas: ["Característica 1", "Característica 2", "Característica 3"]
    }
];

// ── Leer el id del producto desde la URL ──
const params = new URLSearchParams(window.location.search);
const id = parseInt(params.get('id'));

// ── Buscar el producto ──
const producto = productos.find(p => p.id === id);

// ── Mostrar el producto ──
if (producto) {
    document.getElementById('detalle-nombre').textContent = producto.nombre;
    document.getElementById('detalle-precio').textContent = '$' + producto.precio.toLocaleString();
    document.getElementById('detalle-img').src = producto.imagen;

    document.getElementById('boton-detalle').addEventListener('click', function() {
        agregarAlCarrito(producto.nombre, producto.precio);
    });
}
