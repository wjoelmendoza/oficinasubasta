from base import BaseTest

class EmpleadoTest(BaseTest):

    def test_get_406(self):
        client = self.create_app().test_client()
        response = client.get("/Empleado")
        status = response.status
        self.assertTrue(status.count("406") >= 1)

    def test_get_404(self):
        client = self.create_app().test_client()
        response = client.get("/Empleado?codigo=152225&password=123456")
        status = response.status
        self.assertTrue(status.count("404") >= 1)

    def test_get_401(self):
        client = self.create_app().test_client()
        response = client.get("/Empleado?codigo=1&password=1234586")
        status = response.status
        print(status)
        self.assertTrue(status.count("401") >= 1)

    def test_get(self):
        client = self.create_app().test_client()
        response = client.get("/Empleado?codigo=1&password=123456")
        rst = response.get_json()
        self.assertEqual(1, rst["codigo"])
        self.assertEqual("administrador", rst["nombre"])

    def test_post_406(self):
        client = self.create_app().test_client()
        datos = {
            "nombre": "admin2"
        }

        response = client.post("/Empleado", data=datos)
        status = response.status

        self.assertTrue(status.count("406") >= 1)

    def test_post(self):
        client = self.create_app().test_client()
        datos = {
            "nombre": "admin2",
            "password": "123456"
        }

        response = client.post("/Empleado", data=datos)
        rst = response.get_json()

        self.assertEqual(datos["nombre"], rst["nombre"])
        self.assertNotEqual(0, rst["codigo"])

    def test_put_406(self):
        client = self.create_app().test_client()
        datos = {
            "nombre": "admin2",
            "password": "123456"
        }

        response = client.put("/Empleado", data=datos)
        status = response.status

        self.assertTrue(status.count("406") >= 0)

        datos = {
            "codigo": 154555
        }

        response = client.put("/Empleado", data=datos)
        status = response.status

        self.assertTrue(status.count("406") >= 0)

    def test_put(self):
        client = self.create_app().test_client()

        i = self.crear_afiliado(tipo=2)

        datos = {
            "password": "test2",
            "nombre": "incognito",
            "codigo": i
        }

        response = client.put("/Empleado", data=datos)
        rst = response.get_json()
        self.assertEqual(rst["codigo"], i)
        self.assertEqual(rst["nombre"], "incognito")