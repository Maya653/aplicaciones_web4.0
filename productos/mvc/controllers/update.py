import web

render = web.template.render("mvc/views/", base="template")

class Update():
    
    def GET(self):
        try:
            return render.update()
        except Exception as e:
            return "Error"