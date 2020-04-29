from base import BaseTest


class AfiliadoTest(BaseTest):

    def test_get_406(self):
        client = self.create_app().test_client()
        jwt = self.get_token()
        response = client.get(f'/Afiliado?jwt={jwt}')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

        response = client.get(f'/Afiliado?jwt={jwt}&password=123456')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

        response = client.get(f'/Afiliado?jwt={jwt}&codigo=123456')
        status = response.status
        self.assertTrue(status.count("406") >= 1)

    def test_get_404(self):
        client = self.create_app().test_client()
        jwt = self.get_token()
        response = client.get(f'/Afiliado?jwt={jwt}&codigo=123456\
        &password=123456')
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_get_401(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        jwt = self.get_token()
        rsrc = f"/Afiliado?jwt={jwt}&codigo={codigo}&password=123"
        response = client.get(rsrc)
        status = response.status
        self.assertTrue(status.count("401") >= 1)

    def test_get_sp(self):
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        codigo = str(codigo)
        jwt = self.get_token()
        rsrc = f"/Afiliado?jwt={jwt}&codigo={codigo}&password=123456"
        response = client.get(rsrc)

        rst = response.get_json()
        self.assertEqual(codigo, rst['codigo'])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(False, rst["vigente"])

    def test_get_vigente_str(self):
        jwt = self.get_token()
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        codigo = str(codigo)
        self.crear_pago(codigo)
        rsrc = f"/Afiliado?jwt={jwt}&codigo={codigo}&password=123456"
        response = client.get(rsrc)

        rst = response.get_json()
        print(rst["vigente"])
        self.assertEqual(codigo, rst['codigo'])
        self.assertEqual("test1", rst["nombre"])
        self.assertEqual(True, rst["vigente"])

    def test_post_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "nombre": "Test1"
        }

        response = client.post("/Afiliado", data=datos)
        status = response.status

        self.assertTrue(status.count("406") >= 1)

    def test_post(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "nombre": "Test1",
            "password": "123456"
        }

        response = client.post("/Afiliado", data=datos)
        rst = response.get_json()

        self.assertEqual(datos["nombre"], rst["nombre"])
        self.assertNotEqual(0, rst["codigo"])
        self.assertFalse(rst["vigente"])

    def test_put_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token()
        }

        response = client.put("/Afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("406"), 1)

    def test_put_406_b(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "codigo": 2
        }

        response = client.put("/Afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("406"), 1)

    def test_put_404(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "nombre": "test2",
            "codigo": 666
        }

        response = client.put("/Afiliado", data=datos)

        status = response.status

        self.assertGreaterEqual(status.count("404"), 1)

    def test_put(self):
        client = self.create_app().test_client()

        i = self.crear_afiliado()
        i = str(i)

        datos = {
            "jwt": self.get_token(),
            "password": "test2",
            "codigo": i
        }

        response = client.put("/Afiliado", data=datos)

        rst = response.get_json()
        self.assertEqual(rst["codigo"], i)
        self.assertEqual(rst["nombre"], "test1")

    def test_put_vigente(self):
        client = self.create_app().test_client()

        i = self.crear_afiliado()
        i = str(i)

        self.crear_pago(i)

        datos = {
            "jwt": self.get_token(),
            "password": "test2",
            "codigo": i
        }

        response = client.put("/Afiliado", data=datos)

        rst = response.get_json()
        self.assertEqual(rst["codigo"], i)
        self.assertEqual(rst["nombre"], "test1")

