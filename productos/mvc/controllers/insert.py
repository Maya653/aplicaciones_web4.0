import web 

import mvc.models.modelo_productos as modelo_productos

model_productos = modelo_productos.ModeloProducto()

render = web.template.render("mvc/views/", base="layout")

class Insert():
    
    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            return "Error"
    
    
    def POST(self):
        try:
            form = web.input()
            nombre = form.nombre
            descripcion = form.descripcion
            precio = form.precio
            existencias = form.existencias
            model_productos.insert(nombre,descripcion,precio,existencias)
            web.seeother('/list')
                  
        except Exception as e:
            return render.insert()