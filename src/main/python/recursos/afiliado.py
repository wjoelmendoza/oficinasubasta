from flask_restful import Resource, reqparse


class Afiliado(Resource):
    """
    Esta clase maneja los recursos del afiliado
    """

    def __ini__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('jwt', type=str)
        self.parser.add_argument('nombre', type=str)
        self.parser.add_argument('password', type=str)

    
    def post(self, jwt, codigo, clave):
        pass


    def get(self, jwt, codigo, clave):
        return {codigo: codigo}


    def put(self):
        pass


    def delete(self):
        pass
