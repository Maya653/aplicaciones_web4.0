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

# Prueba de conexión y obtención de productos
if __name__ == "__main__":
    # Crear una instancia de ModeloProducto
    modelo = ModeloProducto()

    # Intentar obtener productos
    productos = modelo.obtener_productos()

    # Imprimir los productos obtenidos
    if productos:
        print("Productos obtenidos:")
        for producto in productos:
            print(producto)
    else:
        print("No se pudieron obtener productos.")
