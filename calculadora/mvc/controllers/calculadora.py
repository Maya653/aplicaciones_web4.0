import web
from mvc.models.modelo_calculadora import Operaciones

OPERACIONES = Operaciones()

render = web.template.render('mvc/views/', base='layout_calculadora')

class Index:
    def GET(self):
        try:
            return render.calculadora(None)
        except Exception as e:
            print(f"Error en GET - Calculadora: {e}")
            return "Ocurrió algún error"

class Calcular:
    def POST(self):
        try:
            form = web.input()
            numero1 = float(form.numero1)
            numero2 = float(form.numero2)
            operacion = form.operacion

            resultado = None
            if operacion == 'suma':
                resultado = OPERACIONES.sumar(numero1, numero2)  
            

            return render.calculadora(resultado)
        except Exception as e:
            print(f"Error en POST - Calculadora: {e}")
            return "Ocurrió algún error"
