import mysql.connector
import sqlite3


class Conexion(object):
    creada = False
    base = "mysql"

    def __init__(self):
        """
        Inicia la conexion con la base de datos
        con sus respectivas credenciales
        """
        if Conexion.base == "mysql":  # pragma: no cover
            self._mydb = mysql.connector.connect(
                host='db_oficina',
                user='root',
                passwd='123456',
                database='oficina_subasta'
            )
            Conexion.creada = True
        else:
            self._mydb = sqlite3.connect("base_lite.db")
            if not self.creada:
                Conexion.creada = True
                self.__db_sqlite__()

        self._cursor = self._mydb.cursor()

    def cerrar(self):
        self._mydb.close()

    def __db_sqlite__(self):

        cursor = self._mydb.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ROL(
                id_rol INT UNSIGNED NOT NULL,
                descripcion VARCHAR(100) NOT NULL,
                PRIMARY KEY (id_rol)
            )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS USUARIO(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres VARCHAR(250) NOT NULL,
            fecha_vencimiento DATETIME NULL,
            clave VARCHAR(20) NOT NULL,
            id_rol INT UNSIGNED NOT NULL,
            CONSTRAINT fk_usuario_rol1
            FOREIGN KEY (id_rol)
                REFERENCES ROL (id_rol)
                ON DELETE CASCADE
                ON UPDATE NO ACTION)""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TIPO_DOCUMENTO(
                id_tipo_doc INT NOT NULL,
                descripcion VARCHAR(150) NOT NULL,
                PRIMARY KEY (id_tipo_doc) )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MEMBRESIA(
            id_membresia INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_pago DATETIME NOT NULL,
            fecha_vencimiento DATETIME NOT NULL,
            id_tipo_doc INT NOT NULL,
            id_cliente INTEGER NOT NULL,
            monto DOUBLE NOT NULL,
            CONSTRAINT fk_membresia_cliente
            FOREIGN KEY (id_cliente)
                REFERENCES USUARIO (id_cliente)
                ON DELETE CASCADE
                ON UPDATE NO ACTION,
            CONSTRAINT fk_membresia_tipo_doc1
            FOREIGN KEY (id_tipo_doc)
                REFERENCES TIPO_DOCUMENTO (id_tipo_doc)
                ON DELETE CASCADE
                ON UPDATE NO ACTION
            )""")

        try:
            cursor.execute("""
                CREATE TRIGGER  v_membresia_insert AFTER INSERT ON MEMBRESIA
                    BEGIN
                        UPDATE USUARIO
                        SET fecha_vencimiento = NEW.fecha_vencimiento
                        WHERE id_cliente = NEW.id_cliente;
                END""")
        except sqlite3.OperationalError as e:
            print(e)
