'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición DELETE a un recurso. 
'''

import requests
api_url= "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

response = requests.delete(api_url)
print(response.json())
