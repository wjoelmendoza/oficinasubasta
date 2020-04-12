import unittest

from recursos.conexion import Conexion
from recursos.pago import PagoG
from recursos.db_pago import DBPago
from recursos.db_afiliado import DBAfiliado

class PagoGTest(unittest.TestCase):

    def test_get_error404(self):
        Conexion.base = "sqlite"

        pago = PagoG()
        rst, err = pago.get("12345", 100)

        self.assertEqual(err,404)

    def test_get(self):
        Conexion.base = "sqlite"

        dba = DBAfiliado()
        id_cliente= dba.crear("test1","123456")
        dba.cerrar()

        dbp = DBPago()
        id_pago = dbp.crear_pago(id_cliente, 1000)
        dbp.cerrar()

        pago = PagoG()
        rst = pago.get("12345", id_cliente)

        self.assertEqual(rst["id"], id_pago[0])