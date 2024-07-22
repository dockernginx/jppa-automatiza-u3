from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

estudiantes = [
	{'numero_control': 1221100001, 'nombre': 'ALMENDARIZ RODRIGUEZ DANIEL ANDRES', 'edad': 21, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100121, 'nombre': 'CAMARILLO VELAZQUEZ DIEGO APOLINAR', 'edad': 22, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100200, 'nombre': 'CANCHOLA RAMÍREZ MARIANA', 'edad': 23, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100300, 'nombre': 'CASAS ESPINOLA JAHIR ARTEMIO', 'edad': 21, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100900, 'nombre': 'GOMEZ LUNA CINTHIA VALERIA', 'edad': 22, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100876, 'nombre': 'HERNANDEZ MENDEZ EDGAR FRANCISCO', 'edad': 23, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100546, 'nombre': 'LIRA MORALES CRISTIAN IVAN', 'edad': 24, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100259, 'nombre': 'PALMA APODERADO JUAN PABLO', 'edad': 21, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100698, 'nombre': 'RAMIREZ VAZQUEZ ANGEL ARMANDO', 'edad': 22, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'},
    {'numero_control': 1221100324, 'nombre': 'VENADO SORIA GERMAN EMILIANO', 'edad': 23, 'carrera': 'Ingeniería en Redes Inteligentes y Ciberseguridad'}
]

@app.get("/estudiantes")
def get_estudiantes(): 
 	return jsonify(estudiantes)


'''Agregar un estudiante'''
@app.post('/estudiantes')
def add_estudiante():
    if request.is_json:
        data = request.get_json()
        
        # Validar que data tenga 'numero_control' y 'nombre'
        if 'numero_control' not in data or 'nombre' not in data:
            return {'error': 'Datos incompletos, se requiere numero_control y nombre'}, 400
        
        # Validar que numero_control sea único
        for estudiante in estudiantes:
            if estudiante['numero_control'] == data['numero_control']:
                return {'error': 'El numero de control ya existe'}, 400
        
        estudiantes.append(data)
        return data, 201
    return {'error': 'La solicitud debe ser JSON'}, 415


'''Obtener un usuario en especifico'''
@app.get('/estudiantes/<num_control>')
def get_estudiante_id(num_control):
    for estudiante in estudiantes:
        if estudiante['numero_control'] == int(num_control):
            return jsonify(estudiante)
    return {'error': 'Estudiante no encontrado'}, 404
	

'''Borrar un usuario en especifico'''
@app.delete('/estudiantes/<num_control>')
def delete_estudiante_id(num_control):
    for estudiante in estudiantes:
        if estudiante['numero_control'] == int(num_control):
            estudiantes.remove(estudiante)
            return {'Status': 'Ok', 'mensaje': 'El estudiante ha sido removido'}, 200
    return {'error': 'Estudiante no encontrado'}, 404

'''Modificar un estudiante'''
@app.put('/estudiantes')
def update_estudiante():
    if request.is_json:
        data = request.get_json()
        
        # Validar que data tenga 'numero_control', 'nombre', 'edad' y 'carrera'
        if 'numero_control' not in data or 'nombre' not in data or 'edad' not in data or 'carrera' not in data:
            return {'error': 'Datos incompletos, se requiere numero_control, nombre, edad y carrera'}, 400
        
        for estudiante in estudiantes:
            if estudiante['numero_control'] == int(data['numero_control']):
                estudiante['nombre'] = data['nombre']
                estudiante['edad'] = data['edad']
                estudiante['carrera'] = data['carrera']
                return {'Status': 'Ok', 'mensaje': 'Se ha actualizado el registro'}, 200
        return {'status': 'error', 'mensaje': 'No se ha encontrado registro de estudiante'}, 404
    return {'error': 'La solicitud debe ser JSON'}, 415


if __name__ == '__main__':
    app.run(debug=True)