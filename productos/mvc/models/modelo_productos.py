import web

class ModeloProducto:
    def __init__(self):
        self.db = web.database(
            dbn='postgres',
            host='127.0.0.1',
            port=5432,
            user='postgres',
            pw='Vasconcelos1',
            db='productosdb',
        )

    def obtener_productos(self):
        try:
            productos = self.db.select('productos')
            return productos
        except Exception as e:
            print(f"Error al obtener productos de la base de datos: {e}")
            return None
