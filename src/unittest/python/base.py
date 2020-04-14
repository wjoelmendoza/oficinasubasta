import unittest
from server import Servidor
from recursos.conexion import Conexion
from recursos.db_afiliado import DBAfiliado

class BaseTest(unittest.TestCase):

    def create_app(self):
        server = Servidor()
        server.app.config['TESTING'] = True
        return server.app

