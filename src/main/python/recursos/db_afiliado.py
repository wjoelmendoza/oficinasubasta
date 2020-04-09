from recursos.conexion import Conexion


class DBAfiliado(Conexion):

    def login(self, codigo):  # pragma: no cover
        sql = """SELECT nombres, fecha_vencimiento, clave
        FROM USUARIO
        WHERE id_cliente = """

        if self.base == "mysql":
            sql += "%s"
        else:
            sql += "?"

        vals = (codigo, )

        self._cursor.execute(sql, vals)
        rst = self._cursor.fetchall()

        if len(rst):
            rst = rst[0]

        return rst

    def crear(self, nombre, clave):  # pragma: no cover
        sql = """INSERT INTO USUARIO (nombres, clave, id_rol)
        VALUES """
        if self.base == "mysql":
            sql += "(%s, %s, %s)"
        else:
            sql += "(?, ?, ?)"

        vals = (nombre, clave, 1)
        self._cursor.execute(sql, vals)
        self._mydb.commit()
        return self._cursor.lastrowid

    def modificar(self, codigo, nombre, clave):  # pragma: no cover
        sql = "UPDATE USUARIO SET "
        valores = None

        if nombre is not None and clave is None:

            if self.base == "mysql":
                sql += "nombres = %s "
            else:
                sql += "nombres = ?"

            valores = (nombre, codigo)
        elif nombre is None and clave is not None:
            if self.base == "mysql":
                sql += "clave = %s "
            else:
                sql += "clave = ?"

            valores = (clave, codigo)
        else:
            if self.base == "mysql":
                sql += " nombres = %s, clave = %s "
            else:
                sql += " nombres = ?, clave = ?"

            valores = (nombre, clave, codigo)

        if self.base == "mysql":
            sql += "WHERE id_cliente = %s"
        else:
            sql += "WHERE id_cliente = ?"

        self._cursor.execute(sql, valores)
        self._mydb.commit()

        if self.base == "mysql":
            sql = "SELECT fecha_vencimiento FROM USUARIO WHERE id_cliente = %s"
        else:
            sql = "SELET fecha_vencimiento FROM USUARIO WHERE id_cliente = ?"

        cod = (codigo,)

        self._cursor.execute(sql, cod)
        rst = self._cursor.fetchall()

        return rst[0]


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod()
