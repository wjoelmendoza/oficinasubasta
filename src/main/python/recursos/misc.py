from datetime import datetime
import jwt

public = """-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHQqwPUM9iZq8LfcX8HxeeLMrq4J
i88Bgn0kEpeWu3FZTecfcvDhhbSq1ucJeIPSzVpIMRVaQVITKCHYrGWJiuqajgsJ
rk3opdGfBqeaHJh+b+NkP9X1soaI0shCi5UjqiJVAl286DXUmMvVnDsdyM+Vgw71
ksfpXkKpi2R9/nilAgMBAAE=
-----END PUBLIC KEY-----"""


def cargar_llave():  # pragma: no cover
    global public
    try:
        arc = open("/app/llave.txt", "r")
        public = arc.read()
        print("Usando la llave /app/llave.txt")
    except FileNotFoundError:
        print("Usando la llave por defecto")


def validar_jwt(token, funcion):
    global public
    payload = jwt.decode(token, public, algorithms='RS256')
    exp = datetime.fromtimestamp(payload["exp"])
    f_act = datetime.now()
    if exp < f_act:  # pragma: no cover
        return 403

    scope = payload["scope"]
    c = scope.count(funcion)

    if c == 0:  # pragma no cover
        return 401

    return 200
