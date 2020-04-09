from datetime import datetime
from dateutil.relativedelta import relativedelta
from recursos.conexion import Conexion


class DBPago(Conexion):

   def crear_pago(self,idCliente,monto):
       sql = """INSERT INTO MEMBRESIA (fecha_pago,fecha_vencimiento,id_cliente,
       id_tipo_doc,monto) VALUES (%s,%s,%s,%s,%s)"""
       fechaP = datetime.now()
       fechaV = fechaP + relativedelta(years=1)
       fechaP = fechaP.strftime("%Y-%m-%d %H:%M:%S")
       fechaV = fechaV.strftime("%Y-%m-%d %H:%M:%S")
       valores = (fechaP,fechaV,idCliente,1,monto)
       self._cursor.execute(sql,valores)
       self._mydb.commit()
       return self._cursor.lastrowid,fechaP

   
   def codigo(self,codigo):
        sql = """SELECT id_cliente,monto,fecha_pago FROM MEMBRESIA WHERE 
        id_cliente = %s"""
        valores = (codigo,)
        self._cursor.execute(sql,valores)
        respuesta = self._cursor.fetchall()
        if len(respuesta):
             respuesta = respuesta[0]
        
        return respuesta
   
    