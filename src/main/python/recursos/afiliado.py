from flask_restful import Resource, reqparse


class Afiliado(Resource):
    """
    Esta clase maneja los recursos del afiliado
    """

    def __ini__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('', type=int)
