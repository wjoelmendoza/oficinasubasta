import unittest

from recursos.conexion import Conexion
from recursos.db_pago import DBPago
from recursos.db_afiliado import DBAfiliado

class DBPagoTest(unittest.TestCase):

    def test_crear_pago(self):
        monto = 1000

        Conexion.base = "sqlite"
        dba = DBAfiliado()
        id_cliente = dba.crear("test1", "123456")
        dba.cerrar()

        db_pago = DBPago()
        resp = db_pago.crear_pago(id_cliente, monto)
        db_pago.cerrar()
        self.assertNotEqual(resp,0)

    def test_codigo_pago(self):
        Conexion.base = "sqlite"

        dba = DBAfiliado()
        id_cliente = dba.crear("test1", "123456")
        dba.cerrar()

        db_pago = DBPago()
        id_pago = db_pago.crear_pago(id_cliente, 1000)
        resp = db_pago.codigo_pago(id_cliente)
        db_pago.cerrar()
        self.assertEqual(resp[0], id_pago[0])

        
