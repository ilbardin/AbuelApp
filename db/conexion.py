import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


class DAO:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
        except Error as ex:
            print("Error al intentar conexión: {0}", format(ex))

    def recuperar_lista(self, sentencia):
        if not self.connection.is_connected():
            self.__init__()
        try:
            cursor = self.connection.cursor()
            cursor.execute(sentencia)
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def recuperar_registro(self, sentencia):
        if not self.connection.is_connected():
            self.__init__()
        try:
            cursor = self.connection.cursor()
            cursor.execute(sentencia)
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.connection.is_connected():
                self.connection.close()

    def insertar_o_actualizar(self, sentencia):
        if not self.connection.is_connected():
            self.__init__()
        try:
            cursor = self.connection.cursor()
            cursor.execute(sentencia)
            self.connection.commit()
        except Error as ex:
            print("Error en sentencia: {0}", format(ex))
        finally:
            if self.connection.is_connected():
                self.connection.close()
