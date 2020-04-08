import mysql.connector

class Conexion(object):

    def __init__(self):
        """
        Inicia la conexion con la base de datos
        con sus respectivas credenciales
        """
        self._mydb = mysql.connector.connect(
            host='db_oficina',
            user='root',
            passwd='123456',
            database='oficina_subasta'
        )

        self._cursor = self._mydb.cursor()


    def cerrar(self):
        self._mydb.close()




