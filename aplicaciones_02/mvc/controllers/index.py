import web
"""importamos la clase ModeloIndex del modelo_index.py"""
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layoult')

m_index = ModeloIndex() #se crea el objeto de la clase ModeloIndex

class Index:
    def GET(self):
        try:
            resultado = m_index.consultaProductos()
            return render.index(resultado)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "UPS algo salio mal"