import web 
import json

class ModeloContactos:
    def __init__(self):
        pass
    
    def obtener_contactos(self):
        # En una aplicación real, aquí se realizaría la conexión con la base de datos
        # y se ejecutaría la consulta para obtener los datos de contactos
        # En este ejemplo, simplemente retornaremos los datos de ejemplo en formato JSON
        datos_contactos = [
            {
                "nombre": "Dejah",
                "email": "deja@email.com"
            },
            {
                "nombre": "John",
                "email": "john@email.com"
            }
        ]
        return datos_contactos
