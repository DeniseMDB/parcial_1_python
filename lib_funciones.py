import json
import re
import os

ruta = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\parcial_1\\dt.json'

def leer_archivo(path: str) -> list:
    with open(path, 'r') as file:
        return json.load(file)["jugadores"]
    
lista_jugadores = leer_archivo(ruta)

_b_red: str = '\033[41m'
_b_green: str = '\033[42m'
_b_blue: str = '\033[44m'
_f_white: str = '\033[37m'
_no_color: str = '\033[0m'

def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    This function prints a message with a specified type (error, success, or info) in a colored format.
    :param mensaje: a string containing the message to be printed
    :param tipo_mensaje: The parameter "tipo_mensaje" is a string that represents the type of message
    that will be printed. It can be "Error", "Success", or "Info"
    """
    match tipo_mensaje.strip().capitalize():
        case 'Error':
            print(f'{_b_red}{_f_white}> Error: {mensaje}{_no_color}')
        case 'Success':
            print(f'{_b_green}{_f_white}>{mensaje}{_no_color}')
        case 'Info':
            print(f'{_b_blue}{_f_white}> Information: {mensaje}{_no_color}')

def validar_numero(respuesta: str, patron_regex: str)-> int:  #valida opcion numerica de menu
    if respuesta: #evalua si es vacio o no, false vacio
        if re.match(patron_regex, respuesta):
            return int(respuesta)
        return -1

def validar_lista(lista: list[dict], respuesta: int)-> list:
    if lista:
        if respuesta <= len(lista):
            print("Valor correcto")
            n = respuesta
            return n
        print("Valor incorrecto, hay {0} jugadores en la lista".format(len(lista)))
        return len(lista)

def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input('Presione una tecla para continuar...')
    if os.name in ['ce', 'nt', 'dos']: os.system("cls")
    else: os.system("clear")

def validar_respuesta():
    pass


def formatear_estadistica(lista_jugadores: list[dict], clave_a_formatear: str) -> str:
    """
    The function takes a list of dictionaries containing player statistics and a key to format, and
    returns the formatted key if it exists in the dictionaries, otherwise it returns -1.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param clave_a_formatear: The parameter "clave_a_formatear" is a string that represents the key of a
    dictionary that will be formatted. The function will check if this key exists in the "estadisticas"
    dictionary of each player in the "lista_jugadores" list. If it exists, the function
    :type clave_a_formatear: str
    :return: If the `clave_a_formatear` is found in the `estadisticas` dictionary of any player in the
    `lista_jugadores`, the function will return the formatted version of the key (with underscores
    replaced by spaces and capitalized). If the key is not found, the function will return -1.
    """
    for jugador in lista_jugadores:
        dict_estadistica = jugador["estadisticas"]
    if clave_a_formatear in dict_estadistica.keys():
        clave_a_formatear = (clave_a_formatear.replace("_", " ")).capitalize()
        return clave_a_formatear
    else:
        return -1

def formatear_jugador(jugador: dict, dict_estadisticas: dict, clave: str) -> str:
    """
    This function takes a dictionary of a player's statistics, a dictionary of all players' statistics,
    and a key to format the message and returns a formatted string with the player's name, position, and
    the specified statistic.
    
    :param jugador: A dictionary containing information about a player, including their name and
    position
    :type jugador: dict
    :param dict_estadisticas: A dictionary containing the statistics of a player
    :type dict_estadisticas: dict
    :param clave: The parameter "clave" is a string that represents a key in the dictionary
    "dict_estadisticas". It is used to retrieve a specific statistic for a player
    :type clave: str
    """
    if jugador:
        for key, value in dict_estadisticas.items():
            if clave in key:
                clave_a_formatear = (clave.replace("_", " ")).capitalize()
                mensaje = mensaje = "{0} - {1} - {2}: {3}".format(jugador["nombre"], jugador["posicion"],clave_a_formatear, value)
                return mensaje
    else:
        return "-1"

def mostrar_lista_jugadores(lista_jugadores: list[dict]) -> None:
    """
    The function displays a list of players with their names and positions.
    
    :param lista_jugadores: A list of dictionaries representing players in a sports team. Each
    dictionary contains information about a player, including their name and position
    :type lista_jugadores: list[dict]
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        i = 0
        mensaje = ""
        for jugador in lista_copia:
            mensaje += "{0}. {1} - {2} \n".format(i,jugador["nombre"], jugador["posicion"])
            i += 1
        return mensaje
    else:
        return -1


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
        lista_copia = lista_jugadores.copy()
        encontrado = False
        while encontrado == False:
            for jugador in lista_copia:
                if re.search(patron_regex, jugador["nombre"],re.IGNORECASE):
                    logros = jugador["logros"]
                    encontrado = True
                    break
            else:
                print("No se ha encontrado, por favor intente nuevamente.")
                patron_regex = input("Ingrese el nombre del jugador: ")
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
            if(modo =="asc" and (lista_jugadores[i][key] < lista_jugadores[i_max_min][key])):
                i_max_min = i
            elif(modo == "desc" and (lista_jugadores[i][key] > lista_jugadores[i_max_min][key])):
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


def calcular_promedio(lista_jugadores: list[dict], key: str) -> float:
    """
    This function calculates the average of a specific statistic for a list of players.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param key: The "key" parameter is a string that represents the specific statistic that we want to
    calculate the average for. It is used to access the corresponding value in the "estadisticas"
    dictionary for each player in the "lista_jugadores" list
    :type key: str
    :return: a float value which represents the average of a specific statistic (indicated by the "key"
    parameter) for all the players in a given list of dictionaries (indicated by the "lista_jugadores"
    parameter).
    """
    suma_promedios = 0
    lista_promedios = []
    contador = 0
    estadisticas = {}
    for jugador in lista_jugadores:
        estadisticas = jugador["estadisticas"]
        for clave_promedio,valor_promedio in estadisticas.items():
            clave_promedio = key
            suma_promedios += valor_promedio
            contador += 1
    promedio = round(suma_promedios % contador, 2)
    print("El promedio de \"{0}\" de todo el equipo es de: {1}".format(formatear_estadistica(lista_jugadores, key) ,promedio))
    return promedio

def mostrar_promedio_y_orden_asc(lista_ordenada: list[dict]) -> None:
    """
    The function takes a list of dictionaries containing player statistics, calculates their average
    points per game, sorts the list alphabetically by player name, and prints the sorted list with their
    respective average points per game.
    
    :param lista_ordenada: A list of dictionaries representing basketball players, sorted in
    alphabetical order by name
    :type lista_ordenada: list[dict]
    """
    calcular_promedio(lista_ordenada, "promedio_puntos_por_partido")
    lista_promedios_ordenados = []
    for jugador in lista_ordenada:
        dict_estadisticas = jugador["estadisticas"]
        for clave,valor in dict_estadisticas.items():
            if clave == "promedio_puntos_por_partido":
                lista_promedios_ordenados.append(valor)
    print("La lista ordenada de jugadores segun su orden alfabetico ascendente es: ")
    for i in range(len(lista_ordenada)):
        mensaje = "{0}. {1} - {2} - {3}: {4}".format(i,lista_ordenada[i]["nombre"],lista_ordenada[i]["posicion"],formatear_estadistica(lista_ordenada,"promedio_puntos_por_partido"), lista_promedios_ordenados[i])
        print(mensaje)
    
#6 - Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.

def es_miembro_fama (lista_jugadores: list[dict], regex_nombre: str) -> bool:
    """
    The function checks if a given name is a member of the Basketball Hall of Fame by searching for it
    in a list of player dictionaries.
    
    :param lista_jugadores: a list of dictionaries representing basketball players and their
    achievements
    :type lista_jugadores: list[dict]
    :param regex_nombre: A regular expression string used to search for a player's name in the list of
    players' dictionaries
    :type regex_nombre: str
    :return: a boolean value (True or False) depending on whether the input regex_nombre matches the
    name of a player in the input lista_jugadores who is a member of the Basketball Hall of Fame.
    """
    logros = buscar_nombre_logros(lista_jugadores, regex_nombre)
    if (re.search(r"\bMiembro del Salon de la Fama del Baloncesto\b", logro) for logro in logros):
        return True
    elif (re.search(r"\bMiembro del Salon de la Fama del Baloncesto Universitario\b", logro) for logro in logros):
        return False 

#7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.

def jugador_mayor_estadistica(lista_jugadores: list[dict], clave_estadisticas: str) -> dict:
    """
    This function takes a list of dictionaries representing players and a key for a statistic, and
    returns the player with the highest value for that statistic.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param clave_estadisticas: a string representing the key of the statistic to be used for comparison
    :type clave_estadisticas: str
    :return: a dictionary containing the statistics of the player with the highest value for the
    specified key in the list of players.
    """
    if lista_jugadores:
        lista_copia_jugadores = lista_jugadores.copy()
        lista_estadistica = []
        for jugador in lista_copia_jugadores:
            dict_estadisticas = jugador["estadisticas"]
            lista_estadistica.append(dict_estadisticas)
        lista_ord_asc = sort_asc_desc(lista_estadistica,clave_estadisticas,"asc")
        jugador_mayor_clave = lista_ord_asc[-1]
        return jugador_mayor_clave

def mostrar_jugador_por_clave_estadistica(lista_jugadores: list[dict],clave_estadisticas: str ) -> None:
    """
    This function takes a list of dictionaries representing players and a key for a statistic, finds the
    player with the highest value for that statistic, and returns a formatted string with information
    about that player.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param clave_estadisticas: The parameter "clave_estadisticas" is a string that represents the key or
    name of a specific statistic in the dictionary of statistics for each player in the list of players.
    This function is designed to find the player with the highest value for this specific statistic and
    display their information in a formatted message
    :type clave_estadisticas: str
    :return: a formatted string message that includes information about the player with the highest
    value for the specified statistic key.
    """
    jugador_mayor_clave = jugador_mayor_estadistica(lista_jugadores, clave_estadisticas)
    for jugador in lista_jugadores:
        dic_estadistica = jugador["estadisticas"]
        if dic_estadistica[clave_estadisticas] == jugador_mayor_clave[clave_estadisticas]:
            mensaje = "{0}".format(formatear_jugador(jugador, jugador_mayor_clave, clave_estadisticas))
            return mensaje

                    
def comparacion_valores_estadisticas(lista_jugadores: list[dict], key: str, valor_comparacion: int) -> list[dict]:
    if lista_jugadores:
        jugadores_mayores = []
        lista_copia = lista_jugadores.copy()
        for jugador in lista_copia:
            promedio_puntos = jugador["estadisticas"][key]
            if promedio_puntos > valor_comparacion:
                jugadores_mayores.append(jugador)
    return jugadores_mayores
    

def mostrar_jugador_estadisticas(lista_jugadores: list[dict], key:str) -> None:
    if lista_jugadores:
        i = 0
        lista_copia = lista_jugadores.copy()
        for jugador in lista_copia:
            dict_estadisticas = jugador["estadisticas"]
            mensaje = "{0}. {1} - {2} - {3}: {4}".format(i,jugador["nombre"],jugador["posicion"],formatear_estadistica(lista_copia,key), dict_estadisticas[key])
            i += 1
            print(mensaje)
        

def validar_comparacion_estadistica(lista_jugadores: list[dict], key: str, valor_comparacion: int) -> bool:
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        dict_mayor_key_estadistica = jugador_mayor_estadistica(lista_jugadores, key)
        if dict_mayor_key_estadistica[key] >= valor_comparacion:
            return True
        else:
            return False





