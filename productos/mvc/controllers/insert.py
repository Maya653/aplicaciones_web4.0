import web 

render = web.template.render("mvc/views/", base="template")

class Insert():
    
    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            return "Error"