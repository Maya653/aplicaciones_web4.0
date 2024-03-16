import web 

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class List():
    
    def GET(self):
        try:
            productos = model_productos.select()
            return render.list(productos)
        except Exception as e:
            return "Error"