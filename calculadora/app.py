
import web
from mvc.controllers.calculadora import Index, Calcular

urls = (
    '/', 'Index',
    '/calcular', 'Calcular'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()