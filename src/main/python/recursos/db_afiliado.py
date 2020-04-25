from recursos.conexion import Conexion


class DBAfiliado(Conexion):

    def login(self, codigo, tipo=1):
        sql = """SELECT nombres, fecha_vencimiento, clave
        FROM USUARIO
        WHERE id_cliente = """

        if self.base == "mysql":  # pragma: no cover
            sql += "%s AND id_rol = %s"
        else:
            sql += "? AND id_rol = ?"

        vals = (codigo, tipo)

        self._cursor.execute(sql, vals)
        rst = self._cursor.fetchall()

        if len(rst):
            rst = rst[0]

        return rst

    def crear(self, nombre, clave, tipo=1):
        sql = """INSERT INTO USUARIO (nombres, clave, id_rol)
        VALUES """
        if self.base == "mysql":  # pragma: no cover
            sql += "(%s, %s, %s)"
        else:
            sql += "(?, ?, ?)"

        vals = (nombre, clave, tipo)
        self._cursor.execute(sql, vals)
        self._mydb.commit()
        return self._cursor.lastrowid

    def modificar(self, codigo, nombre, clave):
        sql = "UPDATE USUARIO SET "
        valores = None

        if nombre is not None and clave is None:

            if self.base == "mysql":  # pragma: no cover
                sql += "nombres = %s "
            else:
                sql += "nombres = ?"

            valores = (nombre, codigo)
        elif nombre is None and clave is not None:
            if self.base == "mysql":  # pragma: no cover
                sql += "clave = %s "
            else:
                sql += "clave = ?"

            valores = (clave, codigo)
        else:
            if self.base == "mysql":  # pragma: no cover
                sql += " nombres = %s, clave = %s "
            else:
                sql += " nombres = ?, clave = ?"

            valores = (nombre, clave, codigo)

        if self.base == "mysql":  # pragma: no cover
            sql += "WHERE id_cliente = %s"
        else:
            sql += "WHERE id_cliente = ?"

        self._cursor.execute(sql, valores)
        self._mydb.commit()

        rst = self.get_fecha(codigo)

        return rst

    def get_fecha(self, id_cliente):
        if self.base == "mysql":  # pragma: no cover
            sql = """SELECT fecha_vencimiento, nombres
                     FROM USUARIO WHERE id_cliente = %s"""
        else:
            sql = """SELECT fecha_vencimiento, nombres FROM
                     USUARIO WHERE id_cliente = ?"""

        cod = (id_cliente, )

        self._cursor.execute(sql, cod)
        rst = self._cursor.fetchall()

        if len(rst):
            rst = rst[0]

        return rst


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod()
