from base import BaseTest


class PagoTest(BaseTest):

    def test_get_404(self):
        jwt = self.get_token()
        client = self.create_app().test_client()
        response = client.get(f'/Pago?jwt={jwt}&codigo=100')
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_get(self):
        jwt = self.get_token()
        client = self.create_app().test_client()
        codigo = self.crear_afiliado()
        pago, fecha = self.crear_pago(codigo)
        rsp = f"/Pago?jwt={jwt}&codigo={codigo}"
        response = client.get(rsp)

        rsp = response.get_json()
        self.assertEqual(pago, rsp['id'])
        self.assertEqual(1000, rsp['monto'])
        self.assertEqual(fecha, rsp['fecha'])

    def test_post_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "codigo": "100"
        }

        response = client.post("/Pago", data=datos)
        status = response.status
        self.assertTrue(status.count("406") >= 1)

    def test_post_monto_406(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "codigo": "100",
            "monto": 400
        }

        response = client.post("/Pago", data=datos)
        status = response.status
        self.assertTrue(status.count("406") >= 1)

    def test_post_404(self):
        client = self.create_app().test_client()
        datos = {
            "jwt": self.get_token(),
            "codigo": "100",
            "monto": 1000
        }

        response = client.post("/Pago", data=datos)
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_post_fecha_406(self):
        client = self.create_app().test_client()
        idcliente = self.crear_afiliado()
        self.crear_pago(idcliente)
        idcliente = str(idcliente)

        datos = {
            "jwt": self.get_token(),
            "codigo": idcliente,
            "monto": 1000
        }

        response = client.post("/Pago", data=datos)
        status = response.status
        
        response = client.post("/Pago", data=datos)
        status = response.status
        
        self.assertTrue(status.count("406") >= 1)

    def test_post(self):
        client = self.create_app().test_client()
        idcliente = self.crear_afiliado()

        idcliente = str(idcliente)

        datos = {
            "jwt": self.get_token(),
            "codigo": idcliente,
            "monto": 1000
        }

        response = client.post("/Pago", data=datos)
        rst = response.get_json()

        self.assertNotEqual(rst["id"],0)
        self.assertEqual(rst["monto"],1000)
        self.assertIsNotNone(rst["fecha"])
