import os
from DB.conexion import DAO
from BACK_END.voluntario import Voluntario
from UI import funciones


class Abuelo:

    def __init__(self, usuario, contra, nombre, apellido, celular, direccion, sexo):
        self.usuario = usuario
        contra = funciones.hashearContra(contra)
        contra = contra.decode('utf-8')
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.direccion = direccion
        self.sexo = sexo
        self.ayudante = None

    @staticmethod
    def iniciar_sesion(usuario):
        try:
            dao = DAO()
            sql = f'select contra, nombre, apellido, celular, direccion, sexo from abuelo where usuario=\'{usuario}\';'
            lista = dao.recuperarRegistro(sql)
            contra = bytes((lista[0]))
            contra = contra.decode('utf-8')
            return Abuelo(usuario, contra, lista[1], lista[2], lista[3], lista[4], lista[5])
        except Exception as e:
            print(e)

    #  UI PARA INGRESAR NUEVOS ABUELOS
    def resgistrarse(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO abuelo (usuario, contra, nombre, apellido, celular, direccion, sexo) VALUES ('{0}',\"{1}\",'{2}','{3}','{4}','{5}','{6}');"
            sql = sql.format(self.usuario, self.contra, self.nombre, self.apellido, self.celular, self.direccion,
                             self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE abuelo SET nombre = '{0}', apellido = '{1}', celular = '{2}', direccion = '{3}', sexo = '{4}' WHERE usuario = '{5}';"
            sql = sql.format(self.nombre, self.apellido, self.celular, self.direccion, self.sexo, self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def mostrarDatos(self):
        print('Nombre:', self.nombre)
        print('Apellido:', self.apellido)
        print('Celular:', self.celular)
        print('Dirección:', self.direccion)
        print('Sexo:', self.sexo)

    def eliminarme(self):
        try:
            dao = DAO()
            sql = "DELETE FROM abuelo WHERE usuario = '{0}'"
            sql = sql.format(self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def lista_volutariosDisponibles(self):
        miLatLong = funciones.latitudLongitud(self.direccion)
        loc = Voluntario.lista_voluntariosDisponibles()
        listaVolDisp = []
        for usr in loc:
            if (funciones.haversine(miLatLong, funciones.latitudLongitud(usr[1]))) <= 10:
                listaVolDisp = list(listaVolDisp) + [usr]
        return listaVolDisp

    def pedirAyuda(self, usr_voluntario):
        try:
            dao = DAO()
            sql = f"UPDATE voluntario SET peticionAyuda = '{self.usuario}' WHERE usuario = '{usr_voluntario}';"
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def mostrarDatosVoluntario(ayudante):
        try:
            dao = DAO()
            sql = f"SELECT nombre, apellido, celular FROM voluntario WHERE usuario = '{ayudante}'"
            datos = dao.recuperarRegistro(sql)
            print(
                '\nDatos del voluntario para que pueda comunicarse:\n'
                'Nombre:', datos[0], '\n'
                                     'Apellido:', datos[1], '\n'
                                                            'Celular:', datos[2],
            )
        except Exception as e:
            print(e)

    def actualizarPedido(self):
        try:
            dao = DAO()
            sql = f"SELECT ayudante FROM abuelo WHERE usuario = '{self.usuario}';"
            ayudante = dao.recuperarRegistro(sql)
            if ayudante[0] is not None and ayudante[0] != '0':
                os.system('clear')
                print(
                    '\n¡ATENCION! han respondido a su petición de ayuda:\n'
                    f'El usuario {ayudante[0]} ha aceptado su peticion de ayuda.'
                )
                self.mostrarDatosVoluntario(ayudante[0])
                return 'aceptado'
            elif ayudante[0] == '0':
                os.system('clear')
                print('\n¡ATENCION! han respondido a su petición de ayuda')
                print(f'\nEl voluntario a rechazado su pedido')
                return 'rechazado'
            else:
                return 'sigue'
        except Exception as e:
            print(e)

    # UNA VEZ HECHO Y COMPLETADO EL PEDIDO LIMPIA EL AYUDANTE
    def ayudaCompletadaORechazada(self):
        try:
            dato = 'NULL'
            dao = DAO()
            sql = "UPDATE abuelo SET ayudante = {0} WHERE usuario = '{1}';"
            sql = sql.format(str(dato), self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def verificar_login(usuario, contra):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = f"SELECT contra FROM abuelo WHERE usuario='{usuario}';"
            contraRecuperada = dao.recuperarRegistro(sql)
            contraMysql = bytes((contraRecuperada[0]))
            return funciones.verificarContra(contra, contraMysql)
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def verificar_usuarioDisponible(usuario):
        try:
            dao = DAO()
            sql = "SELECT usuario FROM abuelo;"
            lista_usr = dao.recuperarRegistro(sql)
            verif = True
            if lista_usr is not None:
                for usr in lista_usr:
                    if usr == usuario:
                        verif = False
                        return verif
            return verif
        except Exception as e:
            print(e)
