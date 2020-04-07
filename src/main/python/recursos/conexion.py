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
        sql = "INSERT INTO USUARIO (nombres, clave, id_rol) VALUES (%s, %s, %s)"
        vals = (nombre, clave, "1")
        self._cursor.execute(sql, vals)
        self._mydb.commit()
        return self._cursor.lastrowid

    
    def modificar(self, codigo, nombre, clave):
        sql = "UPDATE USUARIO SET "
        valores = None

        if nombre is not None and clave == None:
            sql += "nombres = %s "
            valores = (nombre, codigo)
        elif nombre == None and clave is not None:
            sql += "clave = %s "
            valores = (clave, codigo)
        else:
            sql += " nombres = %s, clave = %s "
            valores = ( nombre, clave, codigo)

        sql += "WHERE id_cliente = %s"
        self._cursor.execute(sql, valores)
        self._mydb.commit()

        sql = "SELECT * FROM USUARIO WHERE id_cliente = %s"
        self._cursor.execute(sql,codigo)
        rst = self._cursor.fetchall()

        return rst[0][2]

    

    def cerrar(self):
        self._mydb.close()

