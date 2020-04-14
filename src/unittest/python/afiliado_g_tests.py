import unittest

from recursos.conexion import Conexion
from recursos.afiliado import AfiliadoG
from recursos.db_afiliado import DBAfiliado

class AfiliadoGTest(unittest.TestCase):

    def test_get_error406(self):
        af = AfiliadoG()

        rst, err = af.get(None, 5, "123456")
        self.assertEqual(err, 406)

    def test_get_error_404(self):
        Conexion.base = "sqlite"

        af = AfiliadoG()

        rst, err = af.get("valor", 100, "123456")
        self.assertEqual(err, 404)

    def test_get_error_401(self):
        Conexion.base = "sqlite"

        dba = DBAfiliado()
        i = dba.crear("test1", "123456")
        dba.cerrar()

        af = AfiliadoG()
        rst, err = af.get("valor", i, "12")
        self.assertEqual(err, 401)

    def test_get(self):
        Conexion.base = "sqlite"
        nombre = "test1"
        clave = "123456"

        dba = DBAfiliado()
        i = dba.crear(nombre, clave)
        dba.cerrar()

        af = AfiliadoG()
        rst = af.get("jwt", i, clave)

        self.assertEqual(i, rst["codigo"])
        self.assertEqual(nombre, rst["nombre"])
        self.assertEqual(False, rst["vigente"])

