from DB.conexion import DAO
from UI import funciones


class Voluntario:

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
        self.disponibilidad = 0
        self.peticionAyuda = None

    @staticmethod
    def iniciar_sesion(usuario):
        try:
            dao = DAO()
            sql = f'select contra, nombre, apellido, celular, direccion, sexo, disponibilidad from voluntario where usuario=\'{usuario}\';'
            lista = dao.recuperarRegistro(sql)
            contra = bytes((lista[0]))
            contra = contra.decode('utf-8')
            return Voluntario(usuario, contra, lista[1], lista[2], lista[3], lista[4], lista[5])
        except Exception as e:
            print(e)

    def resgistrarse(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "INSERT INTO voluntario (usuario, contra, nombre, apellido, celular, direccion, sexo, disponibilidad) VALUES ('{0}',\"{1}\",'{2}','{3}','{4}','{5}','{6}','0');"
            sql = sql.format(self.usuario, self.contra, self.nombre, self.apellido, self.celular, self.direccion,
                             self.sexo)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def guardar_cambios(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            sql = "UPDATE voluntario SET nombre = '{0}', apellido = '{1}', celular = '{2}', direccion = '{3}', sexo = '{4}' WHERE usuario = '{5}';"
            sql = sql.format(self.nombre, self.apellido, self.celular, self.direccion, self.sexo, self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def cambiarDisponibilidad(self):
        # noinspection PyBroadException
        try:
            dao = DAO()
            disp = dao.recuperarRegistro(f"select disponibilidad from voluntario where usuario = '{self.usuario}';")
            if disp[0] == 0:
                sql = f"UPDATE voluntario SET disponibilidad = 1 WHERE usuario = '{self.usuario}';"
            else:
                sql = f"UPDATE voluntario SET disponibilidad = 0 WHERE usuario = '{self.usuario}';"
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    def mostrarDatos(self):
        print('Nombre:', self.nombre)
        print('Apellido:', self.apellido)
        print('Celular:', self.celular)
        print('Dirección:', self.direccion)
        print('Sexo:', self.sexo)

    def mostrarDisponibilidad(self):
        try:
            dao = DAO()
            disp = dao.recuperarRegistro(f"select disponibilidad from voluntario where usuario = '{self.usuario}';")
            if disp[0] == 0:
                return 'No disponible'
            else:
                return 'Disponible'
        except Exception as e:
            print(e)

    def eliminarme(self):
        try:
            dao = DAO()
            sql = "DELETE FROM voluntario WHERE usuario = '{0}';"
            sql = sql.format(self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def mostrarDatosAbuelo(abuelo):
        try:
            dao = DAO()
            sql = f"SELECT nombre, apellido, celular FROM abuelo WHERE usuario = '{abuelo}';"
            datos = dao.recuperarRegistro(sql)
            print(
                'Datos del abuelo para que pueda comunicarse:\n'
                'Nombre:', datos[0], '\n'
                                     'Apellido:', datos[1], '\n'
                                                            'Celular:', datos[2],
            )
        except Exception as e:
            print(e)

    def actualizarNotificacion(self):
        try:
            dao = DAO()
            resp = ''
            sql = f"SELECT peticionAyuda FROM voluntario WHERE usuario = '{self.usuario}';"
            peticion = dao.recuperarRegistro(sql)
            if peticion[0] is not None:
                print(f'El usuario {peticion[0]} solicita su ayuda')
                print('Opcion 1:\tAceptar\nOpcion 2:\tRechazar')
                resp = input()
                if resp == '1':
                    self.mostrarDatosAbuelo(peticion[0])
                    dao.insertarOActualizar(
                        f'UPDATE abuelo SET ayudante = \'{self.usuario}\' WHERE usuario = \'{peticion[0]}\';')
                elif resp == '2':
                    dao.insertarOActualizar(f'UPDATE abuelo SET ayudante = \'0\' WHERE usuario = \'{peticion[0]}\';')
            else:
                print('No tiene ninguna petición de ayuda.')
        except Exception as e:
            print(e)

    # UNA VEZ COMPLETADA LA ACCION DE LA AYUDA, LIMPIA LA PETICION DE AYUDA
    def ayudaCompletadaORechazada(self):
        try:
            dato = 'NULL'
            dao = DAO()
            sql = "UPDATE voluntario SET peticionAyuda = {0} WHERE usuario = '{1}';"
            sql = sql.format(str(dato), self.usuario)
            dao.insertarOActualizar(sql)
        except Exception as e:
            print(e)

    @staticmethod
    def verificar_login(usuario, contra):
        try:
            dao = DAO()
            sql = f"SELECT contra FROM voluntario WHERE usuario='{usuario}';"
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
            sql = "SELECT usuario FROM voluntario;"
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

    @staticmethod
    def lista_voluntariosDisponibles():
        try:
            dao = DAO()
            sql = "SELECT usuario, direccion FROM voluntario WHERE disponibilidad = 1;"
            lista = dao.recuperarLista(sql)
            return lista
        except Exception as e:
            print(e)
