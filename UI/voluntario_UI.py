from BACK_END.voluntario import Voluntario  # IMPORT DE LA CLASE VOLUNTARIO
from UI import funciones
import os
import time


# PIDE LOS DATOS PARA EL REGISTRO Y LO RETORNA EN UNA LISTA
def Registro():
    usr = funciones.verificar_usuario()
    if Voluntario.verificar_usuarioDisponible(usr):
        contra = funciones.ingresoContra()
        nombre = funciones.verificar_nombreApellido('nombre')
        apellido = funciones.verificar_nombreApellido('apellido')
        celular = funciones.verificar_celular()
        direccion = funciones.verificarDireccion()
        sexo = funciones.elegir_sexo()
    else:
        os.system('clear')
        print('Este nombre de usuario esta ocupado, elija otro.')
        time.sleep(1)
        return Registro()
    lista_usr = [usr, contra, nombre, apellido, celular, direccion, sexo]
    return lista_usr


# VE LOS DATOS DEL VOLUNTARIO
def verMiPerfil(voluntario):
    print('Sus datos son los siguientes:\n')
    voluntario.mostrarDatos()
    input('\nOprima cualquier tecla para continuar...')


# MODIFICA LOS DATOS QUE QUIERA EL VOLUNTARIO
def modificarPerfil(voluntario):
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
            nombre = funciones.verificar_nombreApellido('Nombre')
            os.system('clear')
            if funciones.menuConfirmacion('¿Seguro quiere modificar su nombre?'):
                voluntario.nombre = nombre
                voluntario.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombreApellido('Apellido')
            os.system('clear')
            if funciones.menuConfirmacion('¿Seguro quiere modificar su apellido?'):
                voluntario.apellido = apellido
                voluntario.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            os.system('clear')
            if funciones.menuConfirmacion('¿Seguro quiere modificar su celular?'):
                voluntario.celular = celular
                voluntario.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificarDireccion()
            os.system('clear')
            if funciones.menuConfirmacion('¿Seguro quiere modificar su dirección?'):
                voluntario.direccion = direccion
                voluntario.guardar_cambios()


# RECARGA VERIFICANDO SI ALGUN ABUELO LE HA SOLICITADO AYUDA
def recargar(voluntario):
    voluntario.actualizarNotificacion()
    voluntario.ayudaCompletadaORechazada()
    input('\nOprima cualquiera tecla para continuar...')


# ELIMINA EL USUARIO DE LA BASE DE DATOS
def eliminarUsuario(voluntario):
    if funciones.menuConfirmacion('¿Seguro que quiere eliminar su cuenta?'):
        voluntario.eliminarme()
        return True
    else:
        return False


# MUESTRA POR PANTALLA SI ESTA DISPONIBLE
def mensajeDisponibilidad(voluntario):
    if voluntario.mostrarDisponibilidad() == 'Disponible':
        return '*Su estado es: Disponible. Podria recibir peticiones de ayuda.'
    else:
        return '*Su estado es: No disponible. Cambielo si quiere recibir peticiones de ayuda'


# CAMBIA LA DISPONIBILIDAD DEL USUARIO
def cambiarDisponibilidad(voluntario):
    voluntario.cambiarDisponibilidad()
    print(f'Su disponibilidad cambio a: {voluntario.mostrarDisponibilidad()}')
    input('Oprima cualquier tecla para continuar...')
