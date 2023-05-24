import json
import re

ruta = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\parcial_1\\dt.json'

def leer_archivo(path: str) -> list:
    with open(path, 'r') as file:
        return json.load(file)["jugadores"]
    
lista_jugadores = leer_archivo(ruta)

def mostrar_lista_jugadores(lista_jugadores: list[dict]) -> None:
    """
    The function displays a list of players with their names and positions.
    
    :param lista_jugadores: A list of dictionaries representing players in a sports team. Each
    dictionary contains information about a player, including their name and position
    :type lista_jugadores: list[dict]
    """
    if lista_jugadores:
        for jugador in lista_jugadores:
            mensaje = "{0} - {1}".format(jugador["nombre"], jugador["posicion"])
            print(mensaje)
    else:
        print("Error lista vacia")

#2 - Seleccionar jugador por indice y mostrar sus estadisticas
def mostrar_estadisticas_indice(jugador: dict) -> None:
    """
    This function takes a dictionary representing a player and displays their statistics in a formatted
    way.
    
    :param jugador: The parameter "jugador" is a dictionary that represents a player and contains
    information about their statistics
    :type jugador: dict
    """
    estadisticas = jugador["estadisticas"]
    mensaje = ""
    for clave, valor in estadisticas.items():
        clave = clave.replace("_", " ")
        mensaje += "{0}: {1}\n".format(clave.capitalize(), valor)
    print (mensaje)
    return mensaje

#3 - Guardar estadisticas en formato CSV

def exportar_csv(cadena: str, jugador: dict):
    nombre_jugador = (jugador["nombre"]).replace(" ","_")
    nombre_archivo = "C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\parcial_1\\Estadisticas_{0}.csv".format(nombre_jugador)
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(cadena)
        print("El archivo Estadisticas_{0}.csv ha sido creado.".format(nombre_jugador))

#archivo = mostrar_estadisticas_indice(lista_jugadores[0])
#exportar_csv(archivo,lista_jugadores[0])


#4 - Buscar jugador por nombre y mostrar sus logros

def buscar_nombre_logros(lista_jugadores: list[dict], patron_regex: str) -> list:
    if lista_jugadores:
        cadena_logros = ""
        lista_nombre_jugadores = []
        for jugador in lista_jugadores:
            if re.match(patron_regex, jugador["nombre"]):
                logros = jugador["logros"]
            for logro in logros:
                cadena_logros += "{0}\n".format(logro)
            return cadena_logros

            # lista_nombre_jugadores.append(jugadores["nombre"])
        # for nombre in lista_nombre_jugadores:
        #     if re.match(patron_regex, nombre):

            
print(buscar_nombre_logros(lista_jugadores, "Michael Jordan"))