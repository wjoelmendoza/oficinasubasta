from flask_restful import Resource, reqparse
from recursos.db_pago import DBPago
from recursos.db_afiliado import DBAfiliado
from datetime import datetime
from .misc import validar_jwt


class Pago(Resource):
    def __init__(self):
        location = ("args", "json", "values")
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('jwt', type=str, required=True, location=location)
        self.parser.add_argument('codigo', type=int, required=True, location=location)
        self.parser.add_argument('monto', type=float, required=False)

    def get(self):
        datos = self.parser.parse_args()
        jwt = datos['jwt']
        codigo = datos['codigo']

        # valido token jwt
        estado = validar_jwt(jwt, "pago.get")
        if estado != 200:  # pragma: no coverage
            return {}, estado

        dato = validar_usuario(codigo)
        if len(dato) == 0:
            return {"msg": "Not found"}, 404

        db_pago = DBPago()
        data = db_pago.codigo_pago(codigo)

        fecha = data[2]

        if type(fecha) == str:  # pragma: no coverage
            fecha = datetime.fromisoformat(fecha)

        respuesta = {
            "id": data[0],
            "monto": data[1],
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S")
        }

        return respuesta

    def post(self):
        datos = self.parser.parse_args()
        jwt = datos['jwt']
        cod = datos['codigo']
        monto = datos['monto']

        # validando jwt
        estado = validar_jwt(jwt, "afiliado.post")
        if estado != 200:  # pragma: no coverage
            return {}, estado

        if jwt is None or cod is None or monto is None:
            return {"msg": "Not accepted"}, 406

        if monto != 1000:
            return {"msg": "Not accepted"}, 406
        dato = validar_usuario(cod)
        if len(dato) == 0:
            return {"msg": "Not found"}, 404

        insertar = True
        fvigente = dato[0]

        if fvigente is not None:
            act = datetime.now()

            if type(fvigente) == str:  # pragma: no coverage
                fvigente = datetime.fromisoformat(fvigente)
            insertar = act > fvigente

        if not insertar:
            return {"msg": "Not accepted"}, 406

        db_pago = DBPago()
        id_pago, fechaP = db_pago.crear_pago(cod, monto)
        db_pago.cerrar()

        resp = {
            "id": id_pago,
            "monto": monto,
            "fecha": fechaP
        }
        return resp, 201


def validar_usuario(codigo):
    db_afiliado = DBAfiliado()
    dato = db_afiliado.get_fecha(codigo)
    db_afiliado.cerrar()
    return dato
