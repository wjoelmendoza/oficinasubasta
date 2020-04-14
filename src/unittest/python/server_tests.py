import unittest
from base import BaseTest
from recursos.db_afiliado import DBAfiliado
from recursos.db_pago import DBPago


class AfiliadoTest(BaseTest):

    def test_get_406(self):
        client = self.create_app().test_client()
        response = client.get('/afiliado?jwt=hola')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

        response = client.get('/afiliado?jwt=hola&password=123456')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

        response = client.get('/afiliado?jwt=hola&codigo=123456')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

    def test_get_404(self):
        client = self.create_app().test_client()
        response = client.get('/afiliado?jwt=hola&codigo=123456\
        &password=123456')
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_get_401(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        rsrc = f"/afiliado?jwt=hola&codigo={codigo}&password=123"
        response = client.get(rsrc)
        status = response.status
        self.assertTrue(status.count("401") >= 1)

    def test_get_sp(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        rsrc = f"/afiliado?jwt=hola&codigo={codigo}&password=123456"
        response = client.get(rsrc)

        rst = response.get_json()
        self.assertEqual(codigo, rst['codigo'])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(False, rst["vigente"])

    def test_get_vigente_str(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        self.crear_pago(codigo)
        rsrc = f"/afiliado?jwt=hola&codigo={codigo}&password=123456"
        response = client.get(rsrc)

        rst = response.get_json()
        self.assertEqual(codigo, rst['codigo'])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(True, rst["vigente"])

    def test_get_vigente(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        self.crear_pago(codigo)
        rsrc = f"/afiliado/hola/{codigo}/123456"
        response = client.get(rsrc)

        rst = response.get_json()
        self.assertEqual(codigo, rst['codigo'])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(True, rst["vigente"])

    def test_post_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": "hola",
            "nombre": "Test1"
        }

        response = client.post("/afiliado", data=datos)
        status = response.status

        self.assertTrue(status.count("406") >= 1)

    def test_post(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": "hola",
            "nombre": "Test1",
            "password": "123456"
        }

        response = client.post("/afiliado", data=datos)
        rst = response.get_json()

        self.assertEqual(datos["nombre"], rst["nombre"])
        self.assertNotEqual(0, rst["codigo"])
        self.assertFalse(rst["vigente"])

    def test_put_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": "jwt"
        }

        response = client.put("/afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("406"), 1)

    def test_put_406_b(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": "jwt",
            "codigo": 2
        }

        response = client.put("/afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("406"), 1)

    def test_put_404(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": "jwt",
            "nombre": "test2",
            "codigo": 666
        }

        response = client.put("/afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("404"), 1)

    def test_put(self):
        client = self.create_app().test_client()

        i = self.crear_afiliado()

        datos = {
            "jwt": "jwt",
            "password": "test2",
            "codigo": i
        }

        response = client.put("/afiliado", data=datos)

        rst = response.get_json()
        self.assertEqual(rst["codigo"], i)
        self.assertEqual(rst["nombre"], "test1")

    def test_put_vigente(self):
        client = self.create_app().test_client()

        i = self.crear_afiliado()

        self.crear_pago(i)

        datos = {
            "jwt": "jwt",
            "password": "test2",
            "codigo": i
        }

        response = client.put("/afiliado", data=datos)

        rst = response.get_json()
        self.assertEqual(rst["codigo"], i)
        self.assertEqual(rst["nombre"], "test1")

    def crear_afiliado(self):
        dba = DBAfiliado()
        i = dba.crear("test1", "123456")
        dba.cerrar()
        return i

    def crear_pago(self, cod):
        dbp = DBPago()
        idp, _ = dbp.crear_pago(cod, 1000.00)
        dbp.cerrar()
        return idp


