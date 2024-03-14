import mysql.connector

class Productos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_agenda',
                password='1234',
                host='localhost',
                port = 3309,
                database='agenda_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e) 

objeto = Productos()
objeto.connect()