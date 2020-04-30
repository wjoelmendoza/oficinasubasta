from flask_restful import Resource, reqparse
from recursos.db_afiliado import DBAfiliado
from datetime import datetime
from .misc import validar_jwt


def is_vigente(fecha):
    act = datetime.now()
    if type(fecha) == str:  # pragma: no coverage
        fecha = datetime.fromisoformat(fecha)

    return act < fecha


class Afiliado(Resource):

    def __init__(self):
        location = ("args", "json", "values")
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('jwt', type=str, required=True,
                                 location=location)
        self.parser.add_argument('nombre', type=str, required=False)
        self.parser.add_argument('password', type=str, dest='clave',
                                 required=False, location=location)
        self.parser.add_argument('codigo', type=int, required=False,
                                 location=location)

    def get(self):
        datos = self.parser.parse_args()
        jwt = datos['jwt']
        clave = datos['clave']
        codigo = datos['codigo']

        # validando token
        estado = validar_jwt(jwt, "afiliado.get")
        if estado != 200:  # pragma: no cover
            return {}, estado

        if clave is None or codigo is None:
            return {}, 406

        db_afiliado = DBAfiliado()
        rst = db_afiliado.login(codigo)

        if len(rst) == 0:
            return {}, 404

        if clave != rst[2]:
            return {}, 401

        vigente = rst[1]
        if vigente is None:
            vigente = False
        else:
            vigente = is_vigente(vigente)

        rst = {
            "codigo": codigo,
            "nombre": rst[0],
            "vigente": vigente
        }

        return rst

    def post(self):
        datos = self.parser.parse_args()
        pw = datos["clave"]
        nombre = datos["nombre"]

        # validando jwt
        jwt = datos["jwt"]
        estado = validar_jwt(jwt, "afiliado.post")
        if estado != 200:  # pragma: no cover
            return {}, estado

        if pw is None or nombre is None:
            return {"msg": "Not acceptable"}, 406

        db_afiliado = DBAfiliado()
        id_af = db_afiliado.crear(nombre, pw)
        db_afiliado.cerrar()
        rst = {
            "codigo": id_af,
            "nombre": datos['nombre'],
            "vigente": False
        }

        return rst, 201

    def put(self):
        datos = self.parser.parse_args()
        codigo = datos['codigo']

        if codigo is None:
            return {}, 406

        # validando jwt
        jwt = datos['jwt']
        estado = validar_jwt(jwt, "afiliado.put")
        if estado != 200:  # pragma: no cover
            return {}, estado

        nombre = datos['nombre']
        clave = datos['clave']

        if nombre is None and clave is None:
            return {}, 406

        db_afiliado = DBAfiliado()

        data = db_afiliado.modificar(codigo, nombre, clave)
        db_afiliado.cerrar()

        if len(data) == 0:
            return {}, 404

        vigente = data[0]

        if vigente is None:
            vigente = False
        else:
            vigente = is_vigente(vigente)

        rst = {
            "codigo": codigo,
            "nombre": data[1],
            "vigente": vigente
        }

        return rst, 201

    def delete(self):  # pragma: no cover
        pass
