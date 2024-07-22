'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición POST a un recurso. 
'''

import requests
api_url= "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

data= {"userId":1, "title":"Automatiza" , "completed": False}
headers = {'Content-Type':'Application/json'}
response = requests.post(api_url, json=data)
print(response.json())
