import web 

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class View():
    
    def GET(self, id):
        try:
            productos = model_productos.view(id)[0]
            return render.view(productos)
        except Exception as e:
            return "Error"