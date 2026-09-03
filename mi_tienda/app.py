from flask import Flask, render_template, jsonify

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 25000, "descripcion": "Descripción del producto 1"},
    {"id": 2, "nombre": "Producto 2", "precio": 38000, "descripcion": "Descripción del producto 2"},
    {"id": 3, "nombre": "Producto 3", "precio": 15000, "descripcion": "Descripción del producto 3"},
]

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

@app.route('/api/productos')
def obtener_productos():
    return jsonify(productos)

@app.route('/api/productos/<int:id>')
def obtener_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)