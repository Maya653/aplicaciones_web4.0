import web
import psycopg2

class ModeloProducto:
    def __init__(self):
        self.db = None

    def connect(self):
        self.db = psycopg2.connect(
            dbname='productosdb',
            user='postgres',
            password='Vasconcelos1',
            host='127.0.0.1',
            port=5432
        )

    def select(self):
            try:
                self.connect()
                cursor = self.db.cursor()
                query = "SELECT * FROM productos"
                cursor.execute(query)
                productos = []
                for row in cursor.fetchall():
                    producto = {
                        'id': row[0],
                        'nombre': row[1],
                        'descripcion': row[2],
                        'precio': row[3],
                        'existencias': row[4]
                    }
                    productos.append(producto)
                cursor.close()
                return productos
            except Exception as e:
                print(f"Error al obtener productos de la base de datos: {e}")
                productos=[]
                return productos

    def view(self, id):
        try:
            self.connect()
            cursor = self.db.cursor()
            query = "SELECT * FROM productos WHERE id = %s"
            values = (id,)
            cursor.execute(query, values)
            productos = []
            for row in cursor.fetchall():  # Iterar sobre las filas devueltas por el cursor
                producto = {
                    'id': row[0],
                    'nombre': row[1],
                    'descripcion': row[2],
                    'precio': row[3],
                    'existencias': row[4]
                }
                productos.append(producto)
            cursor.close()
            self.db.close()
            return productos
        except Exception as e:
            print(f"Error al obtener el producto de la base de datos: {e}")
            return []

        
    def insert(self, nombre, descripcion, precio, existencias):
        try:
            self.connect()
            query = "INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (%s, %s, %s, %s)"
            values = (nombre, descripcion, precio, existencias)
            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()
            print("Producto insertado con éxito.")
            cursor.close()
            return True  # Retorna True si la inserción fue exitosa
        except Exception as e:
            print(f"Error al insertar producto en la base de datos: {e}")
            return False  # Retorna False si hubo un error durante la inserción


    def update(self, id, nombre, descripcion, precio, existencias):
        try:
            self.connect()
            query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, existencias = %s WHERE id = %s"
            values = (nombre, descripcion, precio, existencias, id)
            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()
            print("Producto actualizado correctamente.")
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al actualizar producto en la base de datos: {e}")
            return False
    
    def delete(self, id):
            try:
                self.connect()
                cursor = self.db.cursor()
                query = "DELETE FROM productos WHERE id = %s"
                values = (id,)
                cursor.execute(query, values)
                self.db.commit()
                cursor.close()
                self.db.close()
                print("Producto eliminado correctamente.")
                return True
            except Exception as e:
                print(f"Error al eliminar producto de la base de datos: {e}")
                return False

    
# Crear una instancia de ModeloProducto
modelo = ModeloProducto()

# Insertar un nuevo producto
if modelo.insert("coca", "rica cola", 20, 1):
    print("Producto insertado correctamente.")
else:
    print("Error al insertar producto.")

# Intentar actualizar un producto existente
if modelo.update(1, "ZUCARITAS", "CEREAL", 100, 100):
    print("Producto actualizado correctamente.")
else:
    print("Error al actualizar producto.")

#Borrar un producto 
if modelo.delete(3):
    print("Se borro el producto")
else:
    print("No se borro el producto")
# Intentar obtener productos
productos = modelo.select()

# Imprimir los productos obtenidos
if productos:
    print("Productos obtenidos:")
    for producto in productos:
        print(producto)
else:
    print("No se pudieron obtener productos.")



