import json
import re
import os

# ruta = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\parcial_1\\dt.json'

def leer_archivo(path: str) -> list:
    with open(path, 'r') as file:
        return json.load(file)["jugadores"]
    
# lista_jugadores = leer_archivo(ruta)

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

def exportar_csv(cadena: str, nombre_archivo: str):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(cadena)
        


#4 - Buscar jugador por nombre y mostrar sus logros

def buscar_nombre_logros(lista_jugadores: list[dict], patron_regex: str) -> list:
    """
    This function searches for a player's achievements based on a regular expression pattern in a list
    of dictionaries containing player information.
    
    :param lista_jugadores: A list of dictionaries representing players and their achievements
    :type lista_jugadores: list[dict]
    :param patron_regex: A regular expression pattern used to search for a player's name in the list of
    players
    :type patron_regex: str
    :return: a list of logros (achievements) of a jugador (player) whose name matches the given regex
    pattern.
    """
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

def indice_min_max(lista_jugadores: list[dict], key: str, modo: str, key_2:str=1) -> int:
    """
    The function returns the index of the minimum or maximum value in a list of dictionaries based on a
    specified key and sorting mode.
    
    :param lista_jugadores: A list of dictionaries representing players and their attributes
    :type lista_jugadores: list[dict]
    :param key: The key is a string that represents the dictionary key that will be used to compare the
    values of the elements in the list
    :type key: str
    :param modo: "asc" or "desc", indicating whether the function should find the index of the minimum
    or maximum value in the list
    :type modo: str
    :param key_2: The optional second key to use for comparison when sorting the list of dictionaries.
    If it is not provided, the function will only use the first key for comparison, defaults to 1
    :type key_2: str (optional)
    :return: an integer, which represents the index of the player with the minimum or maximum value of a
    given key in a list of dictionaries.
    """
    if lista_jugadores:
        i_max_min = 0
        if key_2 != 1:
            for i in range(len(lista_jugadores)):
                if(modo =="asc" and (lista_jugadores[i][key][key_2] < lista_jugadores[i_max_min][key][key_2])):
                    i_max_min = i
                elif(modo == "desc" and (lista_jugadores[i][key][key_2] > lista_jugadores[i_max_min][key][key_2])):
                    i_max_min = i
        else:
            for i in range(len(lista_jugadores)):
                if(modo =="asc" and (lista_jugadores[i][key] < lista_jugadores[i_max_min][key])):
                    i_max_min = i
                elif(modo == "desc" and (lista_jugadores[i][key] > lista_jugadores[i_max_min][key])):
                    i_max_min = i
    return i_max_min

def sort_asc_desc(lista_jugadores: list, key: str, modo: str, key_2: str=1)->list:
    """
    The function sorts a list of players based on a given key and mode, either in ascending or
    descending order.
    
    :param lista_jugadores: A list of dictionaries representing players
    :type lista_jugadores: list
    :param key: The key parameter is a string that represents the attribute of the player object that
    will be used to sort the list. For example, if the player object has attributes such as "name",
    "age", "score", etc., the key parameter would be set to one of these attributes
    :type key: str
    :param modo: "modo" is a string parameter that determines the sorting mode. It can take two values:
    "asc" for ascending order and "desc" for descending order. This parameter is used in the
    "indice_min_max" function to determine whether to find the minimum or maximum value of the key in
    the
    :type modo: str
    :param key_2: The parameter key_2 is a string that represents the secondary key to be used in case
    of ties when sorting the list. It has a default value of 1, which means that if no value is provided
    for key_2, the function will use the index 1 of the list as the, defaults to 1
    :type key_2: str (optional)
    :return: a sorted list of players based on the specified key and mode.
    """
    
    lista_copia = lista_jugadores.copy()
    for i in range(len(lista_jugadores)):
        lista_aux = lista_copia[i:]
        i_min_max = indice_min_max(lista_aux, key, modo, key_2) + i
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
        suma_promedios += estadisticas[key]
    promedio = round((suma_promedios/len(lista_jugadores)), 2)
    print("El promedio de \"{0}\" de todo el equipo es de: {1}".format(formatear_estadistica(lista_jugadores, key) ,promedio))
    return promedio

def mostrar_promedio_y_orden_asc(lista_ordenada: list[dict], modo: str) -> None:
    """
    The function takes a list of dictionaries containing player statistics, calculates their average
    points per game, sorts the list alphabetically by player name, and prints the sorted list with their
    respective average points per game.
    
    :param lista_ordenada: A list of dictionaries representing basketball players, sorted in
    alphabetical order by name
    :type lista_ordenada: list[dict]
    """
    calcular_promedio(lista_ordenada, modo)
    lista_promedios_ordenados = []
    for jugador in lista_ordenada:
        dict_estadisticas = jugador["estadisticas"]
        for clave,valor in dict_estadisticas.items():
            if clave == modo:
                lista_promedios_ordenados.append(valor)
    print("La lista ordenada de jugadores segun su orden alfabetico ascendente es: ")
    for i in range(len(lista_ordenada)):
        mensaje = "{0}. {1} - {2} - {3}: {4}".format(i,lista_ordenada[i]["nombre"],lista_ordenada[i]["posicion"],formatear_estadistica(lista_ordenada,modo), lista_promedios_ordenados[i])
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

def mostrar_jugador_por_clave_estadistica(lista_jugadores: list[dict], clave_estadisticas: str ) -> None:
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
    """
    This function takes a list of dictionaries representing players and returns a new list of players
    whose statistics for a given key are greater than a specified value.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param key: The key parameter is a string that represents the specific statistic that we want to
    compare for each player. For example, it could be "rebotes" (rebounds) or "asistencias" (assists)
    :type key: str
    :param valor_comparacion: An integer value that will be used to compare against the value of the key
    in the "estadisticas" dictionary of each player in the "lista_jugadores" list
    :type valor_comparacion: int
    :return: a list of dictionaries containing information about players whose statistical value for a
    given key is greater than a specified comparison value.
    """
    if lista_jugadores:
        jugadores_mayores = []
        lista_copia = lista_jugadores.copy()
        for jugador in lista_copia:
            promedio_puntos = jugador["estadisticas"][key]
            if promedio_puntos > valor_comparacion:
                jugadores_mayores.append(jugador)
    return jugadores_mayores
    

def mostrar_jugador_estadisticas(lista_jugadores: list[dict], key:str) -> None:
    """
    This function takes a list of dictionaries representing players and a key, and prints out each
    player's name, position, and the value of the specified key in their statistics dictionary.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param key: The "key" parameter is a string that represents the specific statistic that we want to
    display for each player. It is used to access the corresponding value in the "estadisticas"
    dictionary of each player
    :type key: str
    """
    if lista_jugadores:
        i = 0
        lista_copia = lista_jugadores.copy()
        for jugador in lista_copia:
            dict_estadisticas = jugador["estadisticas"]
            mensaje = "{0}. {1} - {2} - {3}: {4}".format(i,jugador["nombre"],jugador["posicion"],formatear_estadistica(lista_copia,key), dict_estadisticas[key])
            i += 1
            print(mensaje)
        

def validar_comparacion_estadistica(lista_jugadores: list[dict], key: str, valor_comparacion: int) -> bool:
    """
    This function validates if the highest value of a specific key in a list of dictionaries is greater
    than or equal to a given value.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param key: The key is a string that represents the statistic that we want to compare. For example,
    if we want to compare the number of goals scored by each player, the key would be "goals"
    :type key: str
    :param valor_comparacion: The value to compare the key's value against in the function. It is an
    integer
    :type valor_comparacion: int
    :return: a boolean value (True or False) depending on whether the highest value of a given key in a
    list of dictionaries is greater than or equal to a given comparison value.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        dict_mayor_key_estadistica = jugador_mayor_estadistica(lista_jugadores, key)
        if dict_mayor_key_estadistica[key] >= valor_comparacion:
            return True
        else:
            return False


def comparacion_logros(lista_jugadores: list[dict]) -> dict:
    """
    The function takes a list of dictionaries representing players and returns the player with the most
    achievements.
    
    :param lista_jugadores: a list of dictionaries representing players, where each dictionary contains
    information about a player, including their name and a list of their achievements or "logros"
    :type lista_jugadores: list[dict]
    :return: a dictionary that represents the player with the most achievements in a list of players.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        jugador_mayor_logro = lista_copia[0]
        for jugador in lista_copia:
            if len(jugador["logros"]) > len(jugador_mayor_logro["logros"]):
                jugador_mayor_logro = jugador
        return jugador_mayor_logro



def ranking_por_estadistica(lista_jugadores: list[dict], estadistica_ranking: str, regex_nombre: str) -> int:
    """
    This function takes a list of players with their statistics, a specific statistic to rank by, and a
    regular expression for a player's name, and returns the ranking of that player based on the
    specified statistic.
    
    :param lista_jugadores: A list of dictionaries representing players and their statistics
    :type lista_jugadores: list[dict]
    :param estadistica_ranking: The parameter "estadistica_ranking" is a string that represents the
    specific statistic by which the players will be ranked. For example, it could be "puntos" (points),
    "rebotes" (rebounds), or "asistencias" (assists)
    :type estadistica_ranking: str
    :param regex_nombre: The parameter "regex_nombre" is a string that contains a regular expression
    used to match the name of a player in the list of players. The function uses this regular expression
    to find the player's name in the list and determine their ranking based on the specified statistic
    :type regex_nombre: str
    :return: the ranking index (position) of a player in a list of players based on a specific statistic
    and a regular expression for the player's name.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        ranking_stats = sort_asc_desc(lista_copia, "estadisticas", "desc", estadistica_ranking)
        i = 0 
        for i in range(len(ranking_stats)):
            if regex_nombre == ranking_stats[i]["nombre"]:
                ranking_indice = i
                break
        return ranking_indice+1
    

def crear_dict_estadistica_jugador(lista_jugadores: list[dict],regex_nombre: str) -> dict:
    """
    This function creates a dictionary with statistics for a specific player from a list of players,
    based on a regular expression for the player's name.
    
    :param lista_jugadores: A list of dictionaries representing basketball players and their statistics
    :type lista_jugadores: list[dict]
    :param regex_nombre: A regular expression string used to match the name of the player in the list of
    players
    :type regex_nombre: str
    :return: a dictionary with the statistics of a player whose name matches a given regular expression,
    based on a list of players' dictionaries. The dictionary includes the player's name, total points
    ranking, total rebounds ranking, total assists ranking, and total steals ranking.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        dict_jugador = {}
        for jugador in lista_copia:
            if regex_nombre in jugador["nombre"]:
                dict_jugador["nombre"] = jugador["nombre"]
                dict_jugador["ranking_puntos_totales"] = ranking_por_estadistica(lista_copia,"puntos_totales",jugador["nombre"])
                dict_jugador["rebotes_totales"] = ranking_por_estadistica(lista_copia,"rebotes_totales",jugador["nombre"])
                dict_jugador["asistencias_totales"] = ranking_por_estadistica(lista_copia,"asistencias_totales",jugador["nombre"])
                dict_jugador["robos_totales"] = ranking_por_estadistica(lista_copia,"robos_totales",jugador["nombre"])
        return dict_jugador

def lista_dict(lista_jugadores: list) -> list[dict]:
    """
    Crea un lista de diccionarios donde cada uno corresponde a un jugador y su ranking
    """
    lista_dict = []
    dic_jugador = {}
    for jugadores in lista_jugadores:         
        dic_jugador = crear_dict_estadistica_jugador(lista_jugadores, jugadores["nombre"])
        lista_dict.append(dic_jugador)
    return lista_dict

def generar_data_csv(lista_diccionarios):
    """
    The function generates a CSV string from a list of dictionaries containing player statistics.
    
    :param lista_diccionarios: a list of dictionaries, where each dictionary represents a player and
    contains their name, total points, total rebounds, total assists, and total steals
    :return: a string in CSV format that includes the data of the players in the input list of
    dictionaries. The first row of the CSV contains the headers "Jugador, Puntos, Rebotes, Asistencias,
    Robos", and each subsequent row contains the data of a player, with their name, total points, total
    rebounds, total assists, and total steals separated by commas.
    """
    cadena_csv = "Jugador, Puntos, Rebotes, Asistencias, Robos"
    for jugador in lista_diccionarios:
        cadena_csv += "\n{0}, {1}, {2}, {3}, {4}".format(jugador['nombre'],jugador['ranking_puntos_totales'],jugador['rebotes_totales'],jugador['asistencias_totales'],jugador['robos_totales'])
    return cadena_csv
