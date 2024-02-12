import web
from mvc.models.modelo_contactos import ModeloContactos

# Configuración del motor de plantillas
render = web.template.render('mvc/views/')

class Contactos:
    def GET(self):
        try:
            # Instanciamos la clase ModeloContactos
            m_contactos = ModeloContactos()
            # Obtenemos los datos de contactos
            contactos = m_contactos.obtener_contactos()
            # Renderizamos el template contactos.html pasando los datos de contactos
            return render.contactos(contactos)
        except Exception as e:
            print(f"Error en la obtención de contactos: {e}")
            return "Error al obtener los datos de contactos"
