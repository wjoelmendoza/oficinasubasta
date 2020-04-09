from flask_restful import Resource, reqparse
from recursos.db_pago import DBPago


class Pago(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('jwt', type=str, required=True)
        self.parser.add_argument('codigo', type=int, required=True)
        self.parser.add_argument('monto', type=float, required=True)
    

    def post(self):
        datos = self.parser.parse_args()

        cod = datos['codigo']

        if cod == None:
            return {"msg" : "Not acceptable"}, 406
        
        db_pago = DBPago()
        id_pago,fechaP = db_pago.crear_pago(datos['codigo'],datos['monto'])
        db_pago.cerrar()
        resp = {
            "id" : id_pago,
            "monto" : datos['monto'],
            "fecha" : fechaP
        }

        return resp

class PagoG(Resource):

    def get(self, jwt, codigo):
        
        db_pago = DBPago()
        respuesta = db_pago.codigo(codigo)

        if len(respuesta) == 0:
                return {}, 404

        respuesta = {
            "id" : codigo,
            "monto" : respuesta[1],
            "fecha" : str(respuesta[2])
        }

        return respuesta