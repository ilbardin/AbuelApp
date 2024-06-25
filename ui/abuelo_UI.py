import threading
import time
from back_end.abuelo import Abuelo
from ui import funciones
import os


# PIDE LOS DATOS PARA REGISTRAR UN ABUELO Y RETORNA UNA LISTA CON LOS DATOS
def registro():
    usr = funciones.verificar_usuario()

    if Abuelo.verificar_usuario_disponible(usr):
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


# MUESTRA LOS DATOS DEL ABUELO
def ver_mi_perfil(abuelo):
    print('Sus datos son los siguientes:\n')
    abuelo.mostrar_datos()
    input('\nOprima cualquier tecla para ir atras')


# MODIFICA LOS DATOS QUE QUIERA CAMBIAR EL ABUELO
def modificar_perfil(abuelo):
    resp = ''
    while resp != '5':
        os.system('clear')
        print('Selecione que datos desee modificar:')
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
                abuelo.nombre = nombre
                abuelo.guardar_cambios()
        elif resp == '2':
            apellido = funciones.verificar_nombre_apellido('Apellido')
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su apellido?'):
                abuelo.apellido = apellido
                abuelo.guardar_cambios()
        elif resp == '3':
            celular = funciones.verificar_celular()
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su celular?'):
                abuelo.celular = celular
                abuelo.guardar_cambios()
        elif resp == '4':
            direccion = funciones.verificar_direccion()
            os.system('clear')
            if funciones.menu_confirmacion('¿Seguro quiere modificar su dirección?'):
                abuelo.direccion = direccion
                abuelo.guardar_cambios()


# PIDE AYUDA A LOS VOLUNTARIOS DISPONIBLES QUE ESTEN CERCA
def solicitar_ayuda(abuelo):
    lista = abuelo.lista_volutarios_disponibles()
    n = 0
    if len(list) > 0:
        print('   Usuario\tDirección')
        for volunt in lista:
            n = n + 1
            print(f'{n}. {volunt[0]}\t{volunt[1]}')
        resp = int(input('Elija un usuario de la lista de voluntarios disponibles: '))
        abuelo.pedir_ayuda((list[resp - 1][0]))
        print('Cuando el voluntario responda su peticion se le avisara.')
        # CON THREAD HACE EL USO DE LOS HILOS PARA EJECUTAR ESE METODO DE FORMA PARALELA
        segundo_plano = threading.Thread(target=notificacion, args=('sigue', abuelo))
        segundo_plano.start()
    else:
        print('No hay voluntarios disponibles, intente mas tarde.')
        input('Oprima cualquier tecla para ir atras...')


# ELIMINA SU USUARIO DE LA BASE DE DATOS
def eliminar_usuario(abuelo):
    if funciones.menu_confirmacion('¿Seguro que quiere eliminar su cuenta?'):
        abuelo.eliminar_voluntario()
        return True
    else:
        return False


# ESTE METODO MEDIANTE UN BUCLE ACTUALIZA PARA VER SI RESPONDIO EL VOLUNTARIO
def notificacion(msj, abuelo):
    while msj == 'sigue':
        msj = abuelo.actualizar_pedido()
        if msj == 'aceptado':
            print('\nGuarde los datos para que pueda comunicarse con el voluntario')
            input('Oprima cualquier tecla para salir:')
            abuelo.ayuda_completada_o_rechazada()
        elif msj == 'rechazado':
            print('\nVuelva a pedir ayuda y elija a otro usuario o intente mas tarde')
            input('Oprima cualquier tecla para continuar...')
            abuelo.ayuda_completada_o_rechazada()
