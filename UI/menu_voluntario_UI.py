from BACK_END.voluntario import Voluntario
from UI import voluntario_UI
import os


class MenuVoluntario:

    def __init__(self, usuario):
        self.voluntario = Voluntario.iniciar_sesion(usuario)
        self.opcion = 0

    def imprimirMenu(self):
        opciones = {1: self.opcion1, 2: self.opcion2, 3: self.opcion3, 4: self.opcion4, 5: self.opcion5}

        while self.opcion != '6':
            os.system('clear')
            print(f"==={self.voluntario.usuario}===================")
            print("Opción 1:\t Ver mi perfil")
            print("Opción 2:\t Modificar perfil")
            print("Opción 3:\t Cambiar disponibilidad")
            print("Opción 4:\t Recargar para verificar si hay peticiones de ayuda")
            print("Opción 5:\t Eliminar usuario")
            print("Opción 6:\t Salir\n")
            print(voluntario_UI.mensajeDisponibilidad(self.voluntario))
            self.opcion = input("\nSeleccione opción: ")

            if self.opcion.isnumeric():
                if 0 < int(self.opcion) < 6:
                    os.system('clear')
                    function = opciones[int(self.opcion)]
                    function()

    def opcion1(self):
        voluntario_UI.verMiPerfil(self.voluntario)

    def opcion2(self):
        voluntario_UI.modificarPerfil(self.voluntario)

    def opcion3(self):
        voluntario_UI.cambiarDisponibilidad(self.voluntario)

    def opcion4(self):
        voluntario_UI.recargar(self.voluntario)

    def opcion5(self):
        elim = voluntario_UI.eliminarUsuario(self.voluntario)
        if elim:
            self.opcion = '6'
