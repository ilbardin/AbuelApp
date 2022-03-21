from math import atan2, radians, cos, sin, sqrt
from geopy.geocoders import Nominatim
import getpass
import os
import bcrypt
import time


# CONFIRMA EL MENSAJE PASADO POR PARAMETRO
def menuConfirmacion(mensaje):
    opcion = input(mensaje + "\nPresione '1' para confirmar u otra tecla para cancelar.\n")

    if opcion == '1':
        return True
    else:
        os.system('clear')
        print("Cancelado por el usuario.")
        time.sleep(1)
        return False


# VERIFICA EL NOMBRE O APELLIDO
def verificar_nombreApellido(nombre_apellido):
    ok = False
    while not ok:
        os.system('clear')
        nombre = input("Ingrese {}: ".format(nombre_apellido).title())

        # VERIFICAR LONGITUD
        if len(nombre) <= 0 or len(nombre) > 30:
            os.system('clear')
            print("{} demasiado corto o largo. Intente de nuevo".format(nombre_apellido).title())
            time.sleep(1)
            return verificar_nombreApellido(nombre_apellido)

        # VERIFICAR QUE NO CONTENGA ESPACIOS VACIOS
        if nombre.isspace():
            os.system('clear')
            print("El {} no puede contener espacios vacíos. Intente de nuevo.".format(nombre_apellido).title())
            time.sleep(1)
            return verificar_nombreApellido(nombre_apellido)

        os.system('clear')
        print("Usted ha ingresado ", nombre)

        if menuConfirmacion("¿Es correcto el nombre ingresado?"):
            return nombre
        else:
            return verificar_nombreApellido(nombre_apellido)


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

            if menuConfirmacion("¿Es correcto el sexo ingresado?"):
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
        if menuConfirmacion('¿Quiere continuar con ese nombre de usuario?'):
            return usr
        else:
            return verificar_usuario()


# ESTA FORMULA CALCULA LA DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA MEDIANTE LA LATITUD Y LONGITUD
def haversine(latlon1, latlon2):
    R = 6372.8  # RADIO DE LA TIERRA

    latD = radians(latlon2[0] - latlon1[0])
    lonD = radians(latlon2[1] - latlon1[1])

    lat1 = radians(latlon1[0])
    lat2 = radians(latlon2[0])

    a = sin(latD / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lonD / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    d = R * c

    return d


# RETORNA LA LATITUD Y LONGITUD DE LA DIRECCION INGRESADA
def latitudLongitud(direccion):
    geolocator = Nominatim(user_agent='AbuelApp')
    loc = geolocator.geocode(direccion)
    lista = [loc.latitude, loc.longitude]
    return lista


# VERIFICA QUE LA DIRECCION SEA CORRECTA
def verificarDireccion():
    # noinspection PyBroadException
    try:
        geolocator = Nominatim(user_agent='AbuelApp')
        os.system('clear')
        print(
            '*Siga el siguiente formato: Calle y numero, Barrio (opcional), Localidad (opcional), Departamento, Provincia')
        direccion = input('Ingrese dirección: ')
        loc = geolocator.geocode(direccion)
        loc = loc.address
        os.system('clear')
        print('La dirección ingresada es: {}'.format(direccion))
        if menuConfirmacion('¿Quiere continuar con esa dirección?'):
            return direccion
        else:
            return verificarDireccion()
    except Exception as e:
        os.system('clear')
        print(e)
        print('Dirección incorrecta. Verifique y vuelva a ingresarla.')
        time.sleep(1)
        return verificarDireccion()


# VERIFICA QUE LA CONTRASEÑA NO TENGA MENOS DE 8 CARACTERES
def analizar_contra(contra):
    contra = str(contra)
    if contra.isspace() or len(contra) < 8:
        return False
    else:
        return True


# PIDE LA CONTRASEÑA
def ingresoContra():
    os.system('clear')
    contra = getpass.getpass('Ingrese una contraseña: ')
    if analizar_contra(contra):
        repeContra = getpass.getpass('\nVuela a ingresar la contraseña: ')
        if contra == repeContra:
            return contra
        else:
            os.system('clear')
            print('Las contraseñas no coinciden. Intente de nuevo.')
            time.sleep(1)
            return ingresoContra()
    else:
        os.system('clear')
        print('La contraseña no puede tener menos de 8 caracteres ni tener solo espacios vacios. Intente de nuevo.')
        time.sleep(2)
        return ingresoContra()


# VERIFICA QUE EL CELULAR CONTENGA SOLO NUMEROS
def verificar_celular():
    os.system('clear')
    cel = input('Ingrese un numero de celular:')
    if cel.isnumeric():
        os.system('clear')
        print('El celular ingresado es: {}'.format(cel))
        if menuConfirmacion('¿Es correcto ese celular?'):
            return cel
        else:
            return verificar_celular()
    else:
        os.system('clear')
        print('El celular solo puede contener numeros. Intente de nuevo.')
        time.sleep(1)
        return verificar_celular()


def hashearContra(contra):
    contraHash = bcrypt.hashpw(contra.encode('utf-8'), bcrypt.gensalt())
    return contraHash


def verificarContra(contra, contraMysql):
    verif = bcrypt.checkpw(contra.encode('utf-8'), contraMysql)
    return verif
