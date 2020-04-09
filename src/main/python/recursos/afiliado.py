from flask_restful import Resource, reqparse
from recursos.db_afiliado import DBAfiliado


class AfiliadoG(Resource):
    """
    Esta clase maneja los recursos del afiliado
    """

    def get(self, jwt, codigo, clave):
        if codigo is None or clave is None or jwt is None:
            return {}, 406

        db_afiliado = DBAfiliado()
        rst = db_afiliado.login(codigo)

        if len(rst) == 0:
            return {}, 404

        if clave != rst[3]:
            return {}, 401

        vigente = rst[2]
        if vigente is None:
            vigente = False

        # TODO validar la fecha

        rst = {
            "codigo": codigo,
            "nombre": rst[1],
            "vigente": vigente
        }

        return rst


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
        return datos

    def post(self):
        datos = self.parser.parse_args()
        pw = datos["clave"]

        if pw is None:
            return {"msg": "Not acceptable"}, 406

        db_afiliado = DBAfiliado()
        id_af = db_afiliado.crear(datos['nombre'], datos['clave'])
        db_afiliado.cerrar()
        rst = {
            "codigo": id_af,
            "nombre": datos['nombre'],
            "vigente": False
        }

        return rst

    def put(self):
        datos = self.parser.parse_args()
        codigo = datos['codigo']

        if codigo is None:
            return {}, 406

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

        # TODO validar la fecha

        rst = {
            "codigo": codigo,
            "nombre": nombre,
            "vigente": vigente
        }

        return rst

    def delete(self):
        pass
