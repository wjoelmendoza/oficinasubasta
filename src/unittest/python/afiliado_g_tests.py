from base import BaseTest
from recursos.db_afiliado import DBAfiliado
from recursos.afiliado import AfiliadoG

class AfiliadoGTest(BaseTest):

    def test_get_error406(self):
        af = AfiliadoG()
        token = self.get_token()
        rst, err = af.get(token, None, "123456")
        self.assertEqual(err, 406)

    def test_get_error_404(self):
        client = self.create_app().test_client()
        jwt = self.get_token()
        response = client.get(f'/afiliado/{jwt}/10000/1235')
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_get_error_401(self):
        client = self.create_app().test_client()
        i = self.crear_afiliado()
        jwt = self.get_token()
        
        response = client.get(f'/afiliado/{jwt}/{i}/123')
        status = response.status
        self.assertTrue(status.count("401") >= 1)

    def test_get(self):
        client = self.create_app().test_client()
        i = self.crear_afiliado()
        jwt = self.get_token()
        response = client.get(f'/afiliado/{jwt}/{i}/123456')
        rst = response.get_json()

        self.assertEqual(i, rst["codigo"])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(False, rst["vigente"])

