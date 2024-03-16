import web

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class Index():

    def GET(self):
        try:
            return render.index()
        except Exception as e:
            return "Error"