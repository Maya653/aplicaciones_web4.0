import web 

class ModeloIndex:
    def __init__(self):
        pass
    
    def consultaProductos(self):
        #conexion con BD
        #ejecutar la consulta
        #generar una lista con los datos 
        datos = [
            "Laptod HP",
            "Mouse Logitech",
            "Tableta 7",
            "Hub USB c"
        ]
        return datos #regresa la lista