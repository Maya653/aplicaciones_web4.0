import web
from mvc.models.modelo_productos import ModeloProducto

render = web.template.render('mvc/views/', base = 'layout')
m_productos = ModeloProducto()

class Index():
    def GET(self):
        try:
            productos = m_productos.obtener_productos()
            return render.index(productos)
        except Exception as e:
            print(f'Error {e.args}')