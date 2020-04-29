from flask_restful import Resource, reqparse
from recursos.db_afiliado import DBAfiliado
from .misc import validar_jwt


class Empleado(Resource):
    def __init__(self):
        location = ("args", "json", "values")
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nombre', type=str,location=location)
        self.parser.add_argument('password', type=str, dest='clave',
                                 required=False, location=location)
        self.parser.add_argument('codigo', type=int, required=False,
                                 location=location)

    def get(self):
        datos = self.parser.parse_args()
        clave = datos['clave']
        codigo = datos['codigo']

        if clave  is None or codigo is None:
            return {}, 406

        db_afiliado = DBAfiliado()
        rst = db_afiliado.login(codigo, tipo=2)
        db_afiliado.cerrar()

        if len(rst) == 0:
            return {}, 404

        if clave != rst[2]:  # pragma: no cover=
            return {}, 401

        rst = {
            "codigo": codigo,
            "nombre": rst[0]
        }

        return rst

    def post(self):
        datos = self.parser.parse_args()
        clave = datos["clave"]
        nombre = datos["nombre"]

        if clave is None or nombre is None:
            return datos, 406

        db_afiliado = DBAfiliado()
        id_emp = db_afiliado.crear(nombre, clave, tipo=2)
        db_afiliado.cerrar()

        rst = {
            "codigo": id_emp,
            "nombre": nombre
        }

        return rst, 201

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

        if len(data) == 0:  # pragma: no cover
            return {}, 404

        rst = {
            "codigo": codigo,
            "nombre": data[1]
        }

        return rst, 201
