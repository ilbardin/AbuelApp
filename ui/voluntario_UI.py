from back_end.voluntario import Voluntario
from ui import funciones
import os
import time


# PIDE LOS DATOS PARA EL REGISTRO Y LO RETORNA EN UNA LISTA
def registro():
    usr = funciones.verificar_usuario()

    if Voluntario.verificar_usuario_disponible(usr):
        contra = funciones.ingreso_password()
        nombre = funciones.verificar_nombre_apellido('nombre')
        apellido = funciones.verificar_nombre_apellido('apellido')
        celular = funciones.verificar_celular()
        direccion = funciones.verificar_direccion()
        sexo = funciones.elegir_sexo()
    else:
        os.system('clear')
        print('Este nombre de usuario esta ocupado, elija otro.')
        time.sleep(1)
        return registro()
    lista_usr = [usr, contra, nombre, apellido, celular, direccion, sexo]
    return lista_usr


# VE LOS DATOS DEL VOLUNTARIO
def ver_mi_perfil(voluntario):
    print('Sus datos son los siguientes:\n')
    voluntario.mostrar_datos()
    input('\nOprima cualquier tecla para continuar...')


# MODIFICA LOS DATOS QUE QUIERA EL VOLUNTARIO
def modificar_perfil(voluntario):
    resp = ''
    while resp != '5':
        os.system('clear')
        print('Selecione que datos desea modificar:')
        print(
            'Opción 1:\tNombre\n' +
            'Opción 2:\tApellido\n' +
            'Opción 3:\tCelular\n' +
            'Opción 4:\tDirección\n' +
            'Opción 5:\tAtras'
        )
        resp = input()
        if resp == '1':
            nombre = funciones.verificar_nombre_apellido('Nombre')
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su nombre?'):
                voluntario.nombre = nombre
                voluntario.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombre_apellido('Apellido')
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su apellido?'):
                voluntario.apellido = apellido
                voluntario.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su celular?'):
                voluntario.celular = celular
                voluntario.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificar_direccion()
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su dirección?'):
                voluntario.direccion = direccion
                voluntario.guardar_cambios()


# RECARGA VERIFICANDO SI ALGUN ABUELO LE HA SOLICITADO AYUDA
def recargar(voluntario):
    voluntario.actualizar_notificacion()
    voluntario.ayuda_completada_o_rechazada()
    input('\nOprima cualquiera tecla para continuar...')


# ELIMINA EL USUARIO DE LA BASE DE DATOS
def eliminar_usuario(voluntario):
    if funciones.menu_confirmacion('¿Seguro que quiere eliminar su cuenta?'):
        voluntario.eliminar_voluntario()
        return True
    else:
        return False


# MUESTRA POR PANTALLA SI ESTA DISPONIBLE
def mensaje_disponibilidad(voluntario):
    if voluntario.mostrar_disponibilidad() == 'Disponible':
        return '*Su estado es: Disponible. Podria recibir peticiones de ayuda.'
    else:
        return '*Su estado es: No disponible. Cambielo si quiere recibir peticiones de ayuda'


# CAMBIA LA DISPONIBILIDAD DEL USUARIO
def cambiar_disponibilidad(voluntario):
    voluntario.cambiar_disponibilidad()
    print(f'Su disponibilidad cambio a: {voluntario.mostrar_disponibilidad()}')
    input('Oprima cualquier tecla para continuar...')
