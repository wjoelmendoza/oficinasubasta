import unittest
from server import Servidor
from recursos.conexion import Conexion
from recursos.db_afiliado import DBAfiliado
from recursos.db_pago import DBPago

class BaseTest(unittest.TestCase):

    def create_app(self):
        server = Servidor()
        server.app.config['TESTING'] = True
        return server.app

    def crear_afiliado(self):
        dba = DBAfiliado()
        i = dba.crear("test1", "123456")
        dba.cerrar()
        return i

    def crear_pago(self, cod):
        dbp = DBPago()
        idp, fecha = dbp.crear_pago(cod, 1000.00)
        dbp.cerrar()
        return idp, fecha