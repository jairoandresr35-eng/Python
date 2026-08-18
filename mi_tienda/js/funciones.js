let contador = 0;

function agregarAlCarrito() {
    contador++;
    document.querySelector('.carrito span').textContent = contador;
}

const botones = document.querySelectorAll('.boton-agregar');
botones.forEach(boton => {
    boton.addEventListener('click', agregarAlCarrito);
});
document.querySelector('.boton-hero').addEventListener('click', function() {
    document.querySelector('#productos').scrollIntoView({ behavior: 'smooth' });
});