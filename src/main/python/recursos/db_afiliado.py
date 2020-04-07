from recursos.conexion import Conexion

class DBAfiliado(Conexion):

    def login(self, codigo):
        sql = """SELECT id_cliente, nombres, fecha_vencimiento, clave
        FROM USUARIO
        WHERE id_cliente = %s"""
        vals = (codigo, )
        self._cursor.execute(sql, vals)
        rst = self._cursor.fetchall()
        if len(rst):
            rst = rst[0]

        return rst


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

        sql = "SELECT fecha_vencimiento FROM USUARIO WHERE id_cliente = %s"
        cod = (codigo,)
        self._cursor.execute(sql,cod)
        rst = self._cursor.fetchall()

        return rst[0]
