'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición GET a un recuro. 
'''

import requests
api_url= "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

# Obtener la respuesta en formato JSON
data = response.json()

# Imprimir la salida formateada
print("Respuesta formateada de la API:")
for key, value in data.items():
    print(f"{key}: {value}")
