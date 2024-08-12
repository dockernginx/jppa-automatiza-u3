from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = "https://fakestoreapi.com/products"
products = requests.get(URL).json()

@app.route("/products", methods=['GET'])
def get_products():
    return jsonify(products)

# Función para obtener un producto por id
def get_element(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_element(product_id)
    print(product)
    if product is None:
        return jsonify({"error": "Producto No encontrado"}), 404
    return jsonify(product)

def max_id():
    maximo = products[0]['id']
    for product in products:
        if maximo < product['id']:
            maximo = product['id']
    return maximo

#Agregar producto 
@app.route('/products', methods=['POST'])
def create_product(): 
    data = request.get_json()
    product_id = max_id() + 1
    data['id'] = product_id
    products.append(data)
    return jsonify(data), 201


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Producto eliminado exitosamente"}), 200



@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos de entrada no válidos"}), 400
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    # Actualizar el producto
    for key, value in data.items():
        if key != 'id':  # No se debe modificar el ID
            product[key] = value
    return jsonify(product), 200