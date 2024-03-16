import web

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class Update():
    
    def GET(self, id):
        try:
            productos = model_productos.view(id)[0]
            return render.update(productos)
        except Exception as e:
            return "Error"
    
    def POST(self,id):
        try: 
            form =web.input()
            id =form.id
            nombre = form.nombre
            descripcion = form.descripcion
            precio = form.precio
            existencia =form.existencias
            productos = model_productos.update(id, nombre, descripcion, precio, existencia)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"