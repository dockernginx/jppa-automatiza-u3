'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición PATCH a un recurso. 
'''

import requests
api_url= "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

data = {"title":"Automatiza con PATCH"}
response = requests.post(api_url, json=data)
print(response.json())
