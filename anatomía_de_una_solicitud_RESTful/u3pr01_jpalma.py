'''
	Autor: Juan Pablo Palma Apoderado 
	Fecha:  20 Julio 2024
	Descripción: Realziar una petición GET a un recuro. 
'''

import requests
api_url= "https://cat-fact.herokuapp.com/facts"
response = requests.get(api_url)
print(response.status_code)
print(response.headers['Content-Type'])
