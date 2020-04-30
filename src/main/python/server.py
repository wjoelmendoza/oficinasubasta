#! /usr/bin/env python3
from flask import Flask
from flask_restful import Api
from recursos.afiliado import Afiliado
from recursos.pago import Pago
from recursos.empleado import Empleado
from recursos.misc import cargar_llave


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
        self.api.add_resource(Afiliado, '/Afiliado')
        self.api.add_resource(Pago, '/Pago')
        self.api.add_resource(Empleado, '/Empleado')

    def iniciar(self, host='0.0.0.0', port=8080, debug=True):  # pragma: no cover
        """
        Se encarga de inicias el servidor web
        """
        self.app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':  # pragma: no cover
    cargar_llave()
    server = Servidor()
    server.iniciar()
