'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición POST a un recurso. 
'''

import requests
api_url= "https://jsonplaceholder.typicode.com/todos"
data= {"userId":1, "title":"buy milk" , "completed": True}
response = requests.post(api_url, json=data)
print(response.json())
