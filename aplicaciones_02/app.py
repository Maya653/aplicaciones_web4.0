import web

# Importación de las rutas de los controladores
from mvc.controllers.index import Index

# Definición de las URL y asignación de los controladores a las rutas
urls = (
    '/', 'Index'
)

# Creación de la aplicación web
app = web.application(urls, globals())

# Punto de entrada para la aplicación web
if __name__ == "__main__":
    app.run()
