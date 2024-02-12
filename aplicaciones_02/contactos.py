import web
from mvc.controllers.contactos import Contactos

# Definición de las URL y asignación de los controladores a las rutas
urls = (
    '/', 'Contactos'
)

# Creación de la aplicación web
app = web.application(urls, globals())

# Punto de entrada para la aplicación web
if __name__ == "__main__":
    app.run()
