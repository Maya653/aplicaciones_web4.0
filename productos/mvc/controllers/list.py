import web 

render = web.template.render("mvc/views/", base="template")

class List():
    
    def GET(self):
        try:
            return render.list()
        except Exception as e:
            return "Error"