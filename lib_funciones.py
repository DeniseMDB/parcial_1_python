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
            if re.match(patron_regex, jugador["nombre"]): #mejorar con search
                logros = jugador["logros"]
            for logro in logros:
                cadena_logros += "{0}\n".format(logro)
            print(cadena_logros)
            return logros

#5 - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
# ordenado por nombre de manera ascendente.

def indice_min_max(lista_jugadores: list[dict], key: str, modo: str) -> int:
    """
    La función devuelve el índice del valor mínimo o máximo en una
    lista de diccionarios según una clave y modo de ordenamiento especificados.
    Recibe: una lista de diccionarios que representan jugadores
    El parámetro "key" es una cadena que representa la clave del diccionario en la lista
    de jugadores que se utilizará para determinar el valor mínimo o máximo.
    El parámetro "modo" es una cadena que especifica el modo de operación para la función.
    Puede tomar dos valores: "asc" o "desc". Si se pasa "asc",
    la función encontrará el índice del diccionario en la lista con el valor más alto para la clave dada.
    Si se pasa "desc", la función encontrará el índice del diccionario con el valor más bajo para la clave dada.
    Retorna un entero que representa el índice del diccionario en la lista de entrada 
    """
    if lista_jugadores:
        i_max_min = 0
        for i in range(len(lista_jugadores)):
            if(modo =="asc" and (lista_jugadores[i][key] > lista_jugadores[i_max_min][key])):
                i_max_min = i
            elif(modo == "desc" and (lista_jugadores[i][key] < lista_jugadores[i_max_min][key])):
                i_max_min = i
    return i_max_min

def sort_asc_desc(lista_jugadores: list, key: str, modo: str)->list:
    """
    La función ordena una lista de jugadores en orden ascendente o descendente según una clave especificada.
    Recibe una lista de diccionarios que representan jugadores, donde cada diccionario contiene información sobre un héroe como nombre, poder y edad.
    El parámetro "key" es una cadena que representa el atributo del objeto héroe que se utilizará para ordenar la lista.
    "modo" es un parámetro de cadena que determina el modo de ordenamiento.
    Puede tener dos posibles valores: "asc" para orden ascendente o "desc" para orden descendente.
    Retorna una lista ordenada de jugadores basada en la clave y el modo especificados.
    """
    lista_copia = lista_jugadores.copy()
    for i in range(len(lista_jugadores)):
        lista_aux = lista_copia[i:]
        i_min_max = indice_min_max(lista_aux, key, modo) + i
        lista_copia[i], lista_copia[i_min_max] = lista_copia[i_min_max], lista_copia[i]
    return lista_copia


def calcular_promedio_ordenar_nombres(lista_jugadores: list[dict]):
    pass

