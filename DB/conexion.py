import mysql.connector
from mysql.connector import Error


class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                # CAMBIAR LOS DATOS DE LA CONEXION SEGUN CORRESPONDA
                host='localhost',
                port=3306,
                user='root',
                password='mysqlutn',
                db='AbuelApp'
            )
        except Error as ex:
            print("Error al intentar conexión: {0}", format(ex))

    def recuperar_lista(self, sentencia):
        if not self.conexion.is_connected():
            self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()

    def recuperar_registro(self, sentencia):
        if not self.conexion.is_connected():
            self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()

    def insertar_o_actualizar(self, sentencia):
        if not self.conexion.is_connected():
            self.__init__()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sentencia)
            self.conexion.commit()
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.conexion.is_connected():
                self.conexion.close()
