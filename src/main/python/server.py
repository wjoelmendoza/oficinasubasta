#! /usr/bin/env python3
from flask import Flask
from flask_restful import Api
from recursos.afiliado import AfiliadoG, Afiliado


class Servidor:  # pragma: no cover
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

    def iniciar(self, host='0.0.0.0', port=8083, debug=True):
        """
        Se encarga de inicias el servidor web
        """
        self.app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':  # pragma: no cover
    server = Servidor()
    server.iniciar()
