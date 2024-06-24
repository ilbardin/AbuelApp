from back_end.abuelo import Abuelo
from back_end.voluntario import Voluntario
from ui import menu_abuelo_UI, menu_voluntario_UI, voluntario_UI, abuelo_UI
import getpass
import os
import time


class MenuPrincipal:

    def __init__(self):
        self.opcion = 0

    def imprimir_menu(self):

        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3}

        while self.opcion != '3':
            os.system('clear')
            print("=== BIENVENIDO A ABUELAPP ===")
            print("Opción 1:\t INGRESAR")
            print("Opción 2:\t REGISTRARSE")
            print("Opción 3:\t SALIR")

            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if 0 < int(self.opcion) <= 4:
                    os.system('clear')
                    function = opciones[int(self.opcion)]
                    function()

    # INICIO DE SESION
    def opcion1(self):
        print('Como quiere ingresar:')
        print(
            'Opcion 1:\tComo abuelo\n' +
            'Opcion 2:\tComo voluntario\n' +
            'Opcion 3:\tAtras')
        resp = input('\nSeleccione opción: ')

        # PIDE EL USUARIO Y CONTRASEÑA Y VERIFICA QUE COINCIDAN PARA INICIAR SESIÓN
        if resp == '1':
            os.system('clear')
            print('Ingresar como abuelo.')
            usuario = input('\nIngrese su usuario: ')
            contra = getpass.getpass('\nIngrese su contraseña: ')
            if Abuelo.verificar_login(usuario, contra):
                menu_abuelo = menu_abuelo_UI.MenuAbuelo(usuario)
                menu_abuelo.imprimir_menu()
            else:
                os.system('clear')
                print('Usuario o contraseña incorrecta.')
                time.sleep(1)
                os.system('clear')
                return self.opcion1()
        elif resp == '2':
            os.system('clear')
            print('Ingresar como voluntario.')
            usuario = input('\nIngrese su usuario: ')
            contra = getpass.getpass('\nIngrese su contraseña: ')
            if Voluntario.verificar_login(usuario, contra):
                menu_voluntario = menu_voluntario_UI.MenuVoluntario(usuario)
                menu_voluntario.imprimir_menu()
            else:
                os.system('clear')
                print('Usuario o contraseña incorrecta.')
                time.sleep(1)
                os.system('clear')
                return self.opcion1()
        elif resp == '3':
            pass
        else:
            # print('\nOpción incorrecta')
            os.system('clear')
            return self.opcion1()

    # REGISTRO
    def opcion2(self):
        print('Como quiere registrarse:')
        print(
            'Opcion 1:\tComo abuelo\n' +
            'Opcion 2:\tComo voluntario\n'
            'Opcion 3:\tAtras'
        )
        resp = input('\nSeleccione opción: ')
        # MEDIANTE UNA LISTA RETORNADA CREA UN OBJETO Y SUBE LOS DATOS A LA BASE DE DATOS
        if resp == '1':
            lista = abuelo_UI.registro()
            abuelo = Abuelo(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
            abuelo.resgistrarse()
            abuelo = None
            menu_abuelo = menu_abuelo_UI.MenuAbuelo(lista[0])
            menu_abuelo.imprimir_menu()
        elif resp == '2':
            lista = voluntario_UI.registro()
            voluntario = Voluntario(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
            voluntario.resgistrarse()
            voluntario = None
            menu_voluntario = menu_voluntario_UI.MenuVoluntario(lista[0])
            menu_voluntario.imprimir_menu()
        elif resp == '3':
            pass
        else:
            os.system('clear')
            return self.opcion2()

    def opcion3(self):
        print("GRACIAS POR USAR ABUELAPP")
        time.sleep(1)
        self.opcion = '3'
