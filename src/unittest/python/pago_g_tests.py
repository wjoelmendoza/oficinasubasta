from base import BaseTest
from recursos.pago import PagoG
from recursos.db_pago import DBPago

class PagoGTest(BaseTest):

    def test_get_error404(self):
        pago = PagoG()
        jwt = self.get_token()
        rst, err = pago.get(jwt, 100)
        self.assertEqual(err,404)

    def test_get(self):
        client = self.create_app().test_client()
        jwt = self.get_token()
        codigo = self.crear_afiliado()
        pago = self.crear_pago(codigo)
        rsp = f"/pago/{jwt}/{codigo}"
        response = client.get(rsp)
        rsp = response.get_json()

        self.assertEqual(rsp["id"], pago[0])
        