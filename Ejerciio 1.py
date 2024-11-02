# /////////////////////////////////////////////////
#
# Apartado de funciones
#
#/////////////////////////////////////////////////

def bienvenida():
    """
    Muestra un mensaje en formato ASCII con el nombre del programa
    """
    cabera = """

     _               _        __            _   _             
    | |             | |      / _|          | | (_)            
    | |__   __ _ ___| |__   | |_ _   _  ___| |_ _  ___  _ __  
    | '_ \ / _` / __| '_ \  |  _| | | |/ __| __| |/ _ \| '_ \ 
    | | | | (_| \__ \ | | | | | | |_| | (__| |_| | (_) | | | |
    |_| |_|\__,_|___/_| |_| |_|  \__,_|\___|\__|_|\___/|_| |_|


    Author: Julio Zambrano.
    """

    return print(cabera)

def cal_hash(str):
    """
    La funcion recibe de argumento un string (str) el cual el valor del hash y la id es copiado
    a una variable y posteriormente mostrado en pantalla
    """
    identificador = id(str)
    hash_str = hash(str)

    return print("Id:", identificador,"hash:", hash_str)


def solicitarDatos():
    """
    Solicita los datos de un string para obtener su id y hash
    """
    cadena = input(str("Inserta una cadena de texto: "))
    cal_hash(cadena)


# /////////////////////////////////////////////////
#
# Funciones llamadas. Mayus + F10 para ejecutar.
#
#/////////////////////////////////////////////////

bienvenida()
solicitarDatos()

