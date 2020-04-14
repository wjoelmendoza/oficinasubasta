#! /usr/bin/env python3
from flask import Flask
from flask_restful import Api
from recursos.afiliado import AfiliadoG, Afiliado
from recursos.pago import Pago
from recursos.pago import PagoG


class Servidor:
    """
    Esta clase se encarga de manejar el servidor y ponerlo a funcionar
    """
    def __init__(self):
        """
        crea el servidor web junto con los recursos que van a estar disponibles
        """
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(Afiliado, '/afiliado')
        self.api.add_resource(AfiliadoG, '/afiliado/<string:jwt>/<int:codigo>/<string:clave>')
        self.api.add_resource(Pago, '/pago')
        self.api.add_resource(PagoG, '/pago/<string:jwt>/<int:codigo>')

    def iniciar(self, host='0.0.0.0', port=8083, debug=True):  # pragma: no cover
        """
        Se encarga de inicias el servidor web
        """
        self.app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':  # pragma: no cover
    server = Servidor()
    server.iniciar()
