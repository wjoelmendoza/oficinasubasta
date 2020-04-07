from flask_restful import Resource, reqparse
from recursos.db_afiliado import DBAfiliado


class AfiliadoG(Resource):
    """
    Esta clase maneja los recursos del afiliado
    """

    def get(self, jwt, codigo, clave):
        db_afiliado = DBAfiliado()
        db_afiliado.login(codigo, clave)
        return {codigo: codigo}


class Afiliado(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('jwt', type=str, required=True)
        self.parser.add_argument('nombre', type=str, required=True)
        self.parser.add_argument('password', type=str, dest='clave',
                                 required=False)
        self.parser.add_argument('codigo', type=int, required=False)

    
    def post(self):
        datos = self.parser.parse_args()
        pw = datos["clave"]

        if pw == None:
            return {"msg": "Not acceptable"},406
        
        db_afiliado = DBAfiliado()
        id_af =db_afiliado.crear(datos['nombre'], datos['clave'])
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

        if codigo == None:
            return {}, 406
        
        nombre = datos['nombre']
        clave = datos['clave']

        if nombre == None and clave == None:
            return {}, 406

        db_afiliado = DBAfiliado()

        data = db_afiliado.modificar(codigo, nombre, clave)
        db_afiliado.cerrar()

        if len(data) == 0:
            return {}, 404

        if vigente == None:
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
