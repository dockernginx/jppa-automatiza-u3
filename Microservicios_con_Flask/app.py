from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de productos con identificadores únicos
products = [
    {'id': 1, 'description': 'Descripción GBR', 'image': 'Nueva Imagen', 'price': 40512, 'title': 'Nuevo Producto de GBR'}
]

@app.route("/", methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
