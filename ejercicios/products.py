
# Importar módulo requests
import json
import requests

def GetAllProducts():
    url = 'https://fakestoreapi.com/products'
    respuesta = requests.get(url).json()
    print("---------------------------------------------")
    print(json.dumps(respuesta, indent=4,ensure_ascii=False))

def GetProduct():
    print("Búsqueda de producto")
    producto = input("Ingrese el ID del producto que desea consultar: ")
    url = f'https://fakestoreapi.com/products/{producto}'
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        try:
            producto_data = respuesta.json()
            print("---------------------------------------------")
            print(json.dumps(producto_data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            print("No se pudo decodificar la respuesta del servidor.")
    else:
        print("Producto no encontrado o ID no válido.")

def AddProduct():
    print("Agregar producto")
    producto_agregar = {
        "title": input("Ingrese el título del producto: "),
        "price": float(input("Ingrese el precio del producto: ")),
        "description": input("Ingrese la descripción del producto: "),
        "image": input("Ingrese la URL de la imagen del producto: "),
        "category": input("Ingrese la categoría del producto: ")
    }
    url = 'https://fakestoreapi.com/products'
    respuesta = requests.post(url, json=producto_agregar).json()
    print("---------------------------------------------")
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def UpdateProduct():
    print("Modificar producto")
    producto = input("Ingrese el ID del producto que desea modificar: ")
    producto_act = {
        "title": input("Ingrese el nuevo título del producto: "),
        "price": float(input("Ingrese el nuevo precio del producto: ")),
        "description": input("Ingrese la nueva descripción del producto: "),
        "image": input("Ingrese la nueva URL de la imagen del producto: "),
        "category": input("Ingrese la nueva categoría del producto: ")
    }
    url = f'https://fakestoreapi.com/products/{producto}'
    respuesta = requests.put(url, json=producto_act).json()
    print("---------------------------------------------")
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def DeleteProduct():
    print("Eliminación de producto")
    producto = input("Ingrese el ID del producto que desea eliminar: ")
    url = f'https://fakestoreapi.com/products/{producto}'
    respuesta = requests.delete(url)

    # Verificamos si la respuesta es JSON y tiene contenido, asumiendo que el servidor envía datos.
    try:
        producto_data = respuesta.json()
        if producto_data:  # Si el JSON tiene contenido, el producto existía y fue eliminado.
            print("Producto eliminado exitosamente.")
        else:  # Si el JSON está vacío, asumimos que el producto no existía.
            print("El producto no se puede eliminar porque no existe.")
    except ValueError:  # Captura errores de JSONDecodeError y otros problemas de parsing
        # Cuando la respuesta no es un JSON válido, asumimos que es un éxito sin contenido.
        if respuesta.status_code == 200:
            print("Producto eliminado exitosamente.")
        else:
            print(f"Error: No se pudo eliminar el producto (código de estado: {respuesta.status_code}).")

def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        GetAllProducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")