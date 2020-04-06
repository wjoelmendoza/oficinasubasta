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


class DBAfiliado(Conexion):

    def login(self, codigo, clave):
        pass

    
    def crear(self, nombre, clave):
        sql = "INSERT INTO USUARIO (nombres, clave, id_rol) VALUES (%s, %s, %i)"
        vals = (nombre, clave, 1)
        vl = self._cursor.execute(sql, vals)
        self._mydb.commit()
        return self._cursor.lastrowid

    
    def modificar(self, nombre, clave):
        pass
    

    def cerrar(self):
        self.mydb.close()

