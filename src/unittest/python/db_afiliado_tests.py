import unittest


from recursos.db_afiliado import DBAfiliado
from recursos.conexion import Conexion

class DBAfiliadoTest(unittest.TestCase):

    def test_crear(self):
        nombre = "test1"
        clave = "123456"

        Conexion.base = "sqlite"

        db_afiliado = DBAfiliado()
        i = db_afiliado.crear(nombre, clave)
        db_afiliado.cerrar()
        self.assertNotEqual(i, 0)

    def test_login(self):
        nombre = "test1"
        clave = "123456"

        Conexion.base = "sqlite"

        db_afiliado = DBAfiliado()

        codigo = db_afiliado.crear(nombre, clave)

        rst = db_afiliado.login(codigo)
        db_afiliado.cerrar()

        self.assertNotEqual(len(rst), 0)
        self.assertEqual(rst[0], nombre)
        self.assertEqual(rst[2], clave)

    def test_modificar(self):
        nombre = "Carlos Mencos"
        clave = "545454"

        Conexion.base = "sqlite"

        db_afiliado = DBAfiliado()
        codigo = db_afiliado.crear(nombre, clave)
        rst = db_afiliado.modificar(codigo, nombre, clave)
        db_afiliado.cerrar()

        self.assertNotEqual(len(rst), 0)
