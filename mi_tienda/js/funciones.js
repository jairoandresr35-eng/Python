// ── Datos del carrito ──
let carrito = [];

// ── Abrir y cerrar el panel ──
function toggleCarrito() {
    const panel = document.getElementById('carrito-panel');
    if (panel.style.display === 'block') {
        panel.style.display = 'none';
    } else {
        panel.style.display = 'block';
    }
}

// ── Agregar producto al carrito ──
function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    actualizarCarrito();
}

// ── Actualizar visual del carrito ──
function actualizarCarrito() {
    const lista = document.getElementById('carrito-lista');
    const total = document.getElementById('carrito-total');
    const contador = document.getElementById('contador');

    lista.innerHTML = '';
    let suma = 0;

    carrito.forEach(function(producto) {
        const li = document.createElement('li');
        li.innerHTML = `<span>${producto.nombre}</span><span>$${producto.precio.toLocaleString()}</span>`;
        lista.appendChild(li);
        suma += producto.precio;
    });

    total.textContent = '$' + suma.toLocaleString();
    contador.textContent = carrito.length;
}

// ── Vaciar carrito ──
function vaciarCarrito() {
    carrito = [];
    actualizarCarrito();
}

// ── Conectar botones con productos ──
const botones = document.querySelectorAll('.boton-agregar');
botones.forEach(function(boton) {
    boton.addEventListener('click', function(e) {
        e.stopPropagation();
        const tarjeta = boton.closest('.tarjeta');
        const nombre = tarjeta.querySelector('h3').textContent;
        const precioTexto = tarjeta.querySelector('.precio').textContent;
        const precio = parseInt(precioTexto.replace(/\D/g, ''));
        agregarAlCarrito(nombre, precio);
    });
});

// ── Cerrar panel al hacer clic afuera ──
document.addEventListener('click', function(e) {
    const panel = document.getElementById('carrito-panel');
    const carrito_div = document.querySelector('.carrito');
    if (!carrito_div.contains(e.target)) {
        panel.style.display = 'none';
    }
});

// ── Scroll suave al hero ──
document.querySelector('.boton-hero').addEventListener('click', function() {
    document.querySelector('#productos').scrollIntoView({ behavior: 'smooth' });
});