import web 

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class Delete():
    
    def GET(self, id):
        try:
            productos = model_productos.view(id)[0]
            return render.delete(productos)
        except Exception as e:
            return "Error"
    
    def POST(self, id):
        try:
            form = web.input()
            id = form.id
            print(id)
            productos = model_productos.delete(id)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"