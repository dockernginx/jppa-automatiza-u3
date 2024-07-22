
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
    respuesta = requests.get(url).json()
    print("---------------------------------------------")
    print(json.dumps(respuesta, indent=4,ensure_ascii=False))

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
    respuesta = requests.delete(url).json()
    print("---------------------------------------------")
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

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