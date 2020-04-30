import unittest
from server import Servidor
from recursos.conexion import Conexion
from recursos.db_afiliado import DBAfiliado
from recursos.db_pago import DBPago
from datetime import datetime, timedelta
import math
import jwt


class BaseTest(unittest.TestCase):

    def get_token(self):
        llave_privada = """-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgHQqwPUM9iZq8LfcX8HxeeLMrq4Ji88Bgn0kEpeWu3FZTecfcvDh
hbSq1ucJeIPSzVpIMRVaQVITKCHYrGWJiuqajgsJrk3opdGfBqeaHJh+b+NkP9X1
soaI0shCi5UjqiJVAl286DXUmMvVnDsdyM+Vgw71ksfpXkKpi2R9/nilAgMBAAEC
gYAyInF8UMe69NRGxXkePpUX6LZKrhwEjuY+E99iRM9Ir/4LDWuRwgLuYfy1YUT9
v3CY0ic8y+L9BP+A+/4LJD0rRE2T/Yb06Eu2F00oAbnSIXkkmafUJfbxhEceOla4
GTDbTGgbSJr1isVyS3OMBeyzwuFmjQcv2pNag1dQG4zB0QJBAMjDG2iOLJy50plX
PC1nV0UDAVSqYc5hxi8j/+tU6gR87qjiqBbUAg9f73FtFfSeT9dSPVQX5SpoSkET
K1kvm68CQQCUIRl0D5ANUbVbBn89C/cVoDzxv2XougBwV0Ea0PwlyxWAuGv3e11j
u7q/322g2b+TIiSpSM6sQBtSHXbYlyHrAkA5myphLPKGIhfY4hwlVxLGfZ9DIQSh
iJKqciT77Midcw+0LB1ZN4pDyR5WqJt1LnvwZ+urFpQuP/CWjZ6Rn8SHAkBQytDY
NZjLOvKgiCWkBT+p4vD6pfsOeUy9+UlAOBYfAupif7QbkoS4Xe8YseNYZQuRU4EN
d/GJj5mXKwzkS2IrAkEAgGyp0q4uO9VLeCFUjl68rfGsomNvUoO33ZvTIf6bQjvH
zBMS8dZ2SdC/V54ORyXexw+5Hy8UkXZCco1i8umMIw==
-----END RSA PRIVATE KEY-----
"""

        scope = ["afiliado.get", "afiliado.post", "afiliado.put", "pago.post",
                 "pago.get"]
        fecha = datetime.now()
        iat = math.trunc(fecha.timestamp())
        fecha = fecha + timedelta(days=1)
        exp = math.trunc(fecha.timestamp())
        client_id = "test"
        payload = {
            "client_id": client_id,
            "scope": scope,
            "exp": exp,
            "iat": iat
        }
        token = jwt.encode(payload, llave_privada, algorithm='RS256')
        return token.decode("utf-8")

    def create_app(self):
        Conexion.base = "sqlite"
        server = Servidor()
        server.app.config['TESTING'] = True
        return server.app

    def crear_afiliado(self, tipo=1):
        dba = DBAfiliado()
        i = dba.crear("test1", "123456", tipo=tipo)
        dba.cerrar()
        return i

    def crear_pago(self, cod):
        dbp = DBPago()
        idp, fecha = dbp.crear_pago(cod, 1000.00)
        print(f"pago: {idp}")
        dbp.cerrar()
        return idp, fecha