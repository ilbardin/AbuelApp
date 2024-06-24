from math import atan2, radians, cos, sin, sqrt
from geopy.geocoders import Nominatim
import getpass
import os
import bcrypt
import time


# CONFIRMA EL MENSAJE PASADO POR PARAMETRO
def menu_confirmacion(mensaje):
    opcion = input(mensaje + "\nPresione '1' para confirmar u otra tecla para cancelar.\n")

    if opcion == '1':
        return True
    else:
        os.system('clear')
        print("Cancelado por el usuario.")
        time.sleep(1)
        return False


# VERIFICA EL NOMBRE O APELLIDO
def verificar_nombre_apellido(nombre_apellido):
    ok = False
    while not ok:
        os.system('clear')
        nombre = input("Ingrese {}: ".format(nombre_apellido).title())

        # VERIFICAR LONGITUD
        if len(nombre) <= 0 or len(nombre) > 30:
            os.system('clear')
            print("{} demasiado corto o largo. Intente de nuevo".format(nombre_apellido).title())
            time.sleep(1)
            return verificar_nombre_apellido(nombre_apellido)

        # VERIFICAR QUE NO CONTENGA ESPACIOS VACIOS
        if nombre.isspace():
            os.system('clear')
            print("El {} no puede contener espacios vacíos. Intente de nuevo.".format(nombre_apellido).title())
            time.sleep(1)
            return verificar_nombre_apellido(nombre_apellido)

        os.system('clear')
        print("Usted ha ingresado ", nombre)

        if menu_confirmacion("¿Es correcto el nombre ingresado?"):
            return nombre
        else:
            return verificar_nombre_apellido(nombre_apellido)


# DA OPCIONES PARA QUE EL USUARIO ELIJA EL SEXO
def elegir_sexo():
    ok = False
    lista_sexos = ["MASCULINO", "FEMENINO", "INDEFINIDO"]

    while not ok:
        try:
            os.system('clear')
            print("SELECCIONE SU SEXO:")
            print("1: MASCULINO\n2: FEMENINO\n3: INDEFINIDO")
            opcion = int(input("\nIngrese el número correspondiente a su sexo: "))

            if opcion < 1 or opcion > 3:
                os.system('clear')
                return elegir_sexo()

            #  SE LE RESTA 1 A LA LISTA PARA QUE COINCIDA CON LO QUE INGRESA EL USUARIO
            sexo = lista_sexos[opcion - 1]
            os.system('clear')
            print("El sexo elegido es:", sexo)

            if menu_confirmacion("¿Es correcto el sexo ingresado?"):
                return sexo
            else:
                return elegir_sexo()
        except ValueError:
            pass
            # print("\nERROR. ESPACIO EN BLANCO\n")


# VERIFICA QUE EL USUARIO NO ESTE VACIO Y/O SOLO CON ESPACIOS
def verificar_usuario():
    os.system('clear')
    usr = input('Ingrese un nombre de usuario:')
    if usr == '' or usr.isspace():
        os.system('clear')
        print('El nombre de usuario no puede estar vacio. Intente de vuelta.')
        time.sleep(1)
        return verificar_usuario()
    else:
        os.system('clear')
        print('El usuario ingresado es: {}'.format(usr))
        if menu_confirmacion('¿Quiere continuar con ese nombre de usuario?'):
            return usr
        else:
            return verificar_usuario()


# ESTA FORMULA CALCULA LA DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA MEDIANTE LA LATITUD Y LONGITUD
def haversine(latlon1, latlon2):
    r = 6372.8  # RADIO DE LA TIERRA

    lat_d = radians(latlon2[0] - latlon1[0])
    lon_d = radians(latlon2[1] - latlon1[1])

    lat1 = radians(latlon1[0])
    lat2 = radians(latlon2[0])

    a = sin(lat_d / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lon_d / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    d = r * c

    return d


# RETORNA LA LATITUD Y LONGITUD DE LA DIRECCION INGRESADA
def latitud_longitud(direccion):
    geolocator = Nominatim(user_agent='AbuelApp')
    loc = geolocator.geocode(direccion)
    lista = [loc.latitude, loc.longitude]
    return lista


# VERIFICA QUE LA DIRECCION SEA CORRECTA
def verificar_direccion():
    # noinspection PyBroadException
    try:
        geolocator = Nominatim(user_agent='AbuelApp')
        os.system('clear')
        print(
            '*Siga el siguiente formato: Calle y numero, Barrio (opcional), Localidad (opcional), Departamento, '
            'Provincia')
        direccion = input('Ingrese dirección: ')
        loc = geolocator.geocode(direccion)
        loc = loc.address
        os.system('clear')
        print('La dirección ingresada es: {}'.format(direccion))
        if menu_confirmacion('¿Quiere continuar con esa dirección?'):
            return direccion
        else:
            return verificar_direccion()
    except Exception as e:
        os.system('clear')
        print(e)
        print('Dirección incorrecta. Verifique y vuelva a ingresarla.')
        time.sleep(1)
        return verificar_direccion()


# VERIFICA QUE LA CONTRASEÑA NO TENGA MENOS DE 8 CARACTERES
def analizar_password(contra):
    contra = str(contra)
    if contra.isspace() or len(contra) < 8:
        return False
    else:
        return True


# PIDE LA CONTRASEÑA
def ingreso_password():
    os.system('clear')
    contra = getpass.getpass('Ingrese una contraseña: ')
    if analizar_password(contra):
        repe_contra = getpass.getpass('\nVuela a ingresar la contraseña: ')
        if contra == repe_contra:
            return contra
        else:
            os.system('clear')
            print('Las contraseñas no coinciden. Intente de nuevo.')
            time.sleep(1)
            return ingreso_password()
    else:
        os.system('clear')
        print('La contraseña no puede tener menos de 8 caracteres ni tener solo espacios vacios. Intente de nuevo.')
        time.sleep(2)
        return ingreso_password()


# VERIFICA QUE EL CELULAR CONTENGA SOLO NUMEROS
def verificar_celular():
    os.system('clear')
    cel = input('Ingrese un numero de celular:')
    if cel.isnumeric():
        os.system('clear')
        print('El celular ingresado es: {}'.format(cel))
        if menu_confirmacion('¿Es correcto ese celular?'):
            return cel
        else:
            return verificar_celular()
    else:
        os.system('clear')
        print('El celular solo puede contener numeros. Intente de nuevo.')
        time.sleep(1)
        return verificar_celular()


def hashear_password(contra):
    contra_hash = bcrypt.hashpw(contra.encode('utf-8'), bcrypt.gensalt())
    return contra_hash


def verificar_contra(contra, contra_mysql):
    verif = bcrypt.checkpw(contra.encode('utf-8'), contra_mysql)
    return verif
