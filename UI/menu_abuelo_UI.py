from UI import abuelo_UI
from BACK_END.abuelo import Abuelo
import os


class MenuAbuelo:

    def __init__(self, usuario):
        self.abuelo = Abuelo.iniciar_sesion(usuario)
        self.opcion = 0

    def imprimir_menu(self):
        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4}

        while self.opcion != '5':
            os.system('clear')
            print(f"=== {self.abuelo.usuario} =======================")
            print("Opción 1:\t Ver mi perfil")
            print("Opción 2:\t Modificar perfil")
            print("Opción 3:\t Solicitar ayuda")
            print("Opción 4:\t Eliminar usuario")
            print("Opción 5:\t Salir")
            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if 0 < int(self.opcion) <= 4:
                    os.system('clear')
                    function = opciones[int(self.opcion)]
                    function()

    def opcion1(self):
        abuelo_UI.ver_mi_perfil(self.abuelo)

    def opcion2(self):
        abuelo_UI.modificar_perfil(self.abuelo)

    def opcion3(self):
        abuelo_UI.solicitar_ayuda(self.abuelo)

    def opcion4(self):
        elim = abuelo_UI.eliminar_usuario(self.abuelo)
        if elim:
            self.opcion = '5'
