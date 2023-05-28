import json
import re
import os


def leer_archivo(path: str) -> list:
    with open(path, 'r') as file:
        return json.load(file)["jugadores"]
    
_b_red: str = '\033[41m'  
_b_green: str = '\033[42m'
_b_blue: str = '\033[44m'
_f_white: str = '\033[37m'
_no_color: str = '\033[0m'

def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    La función imprimir_mensaje imprime un mensaje en la consola con un formato específico según el tipo de mensaje.
    Recibe:
        El mensaje que se desea imprimir.
        El tipo de mensaje, que puede ser "Error", "Success" o "Info".
    Retorna:
        No devuelve ningún valor, simplemente imprime el mensaje en la consola.
    """
    match tipo_mensaje.strip().capitalize():
        case 'Error':
            print(f'{_b_red}{_f_white}> Error: {mensaje}{_no_color}')
        case 'Success':
            print(f'{_b_green}{_f_white}>{mensaje}{_no_color}')
        case 'Info':
            print(f'{_b_blue}{_f_white}>{mensaje}{_no_color}')

def validar_numero(respuesta: str, patron_regex: str)-> int:
    """
    Valida una opción numérica de un menú.
    Recibe:
        respuesta (str): La respuesta ingresada por el usuario.
        patron_regex (str): El patrón regular utilizado para validar la respuesta.
    Retorna el número validado si cumple con el patrón, de lo contrario, devuelve -1.
    """
    if respuesta: 
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


def formatear_estadistica(lista_jugadores: list[dict], clave_a_formatear: str) -> str:
    """
    Formatea una clave de estadística en un formato legible.
    Recibe:
        lista_jugadores (list[dict]): Una lista de diccionarios que contiene información de los jugadores.
        clave_a_formatear (str): La clave de estadística a formatear.
    Retorna:
        str: La clave de estadística formateada si existe en los diccionarios de jugadores, de lo contrario, devuelve -1.
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
    Formatea los datos del jugador en una cadena que incluye el nombre, la posición y la estadística deseada.
    Recibe:
        jugador (dict): Un diccionario que contiene la información del jugador.
        dict_estadisticas (dict): Un diccionario que contiene las estadísticas del jugador.
        clave (str): La clave de estadística específica a formatear.
    Retorna:
        str: Una cadena con los datos del jugador en el siguiente formato: "{nombre} - {posicion} - {clave formateada}: {valor}".
        Si el jugador no existe, devuelve -1.
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
    Muestra una lista de jugadores en el siguiente formato: "{índice}. {nombre} - {posicion}".
    Recibe:
        lista_jugadores (list[dict]): Una lista de diccionarios que contiene información de los jugadores.
    Retorna:
        None: Esta función no devuelve ningún valor. Muestra la lista de jugadores directamente en la salida.
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
    Muestra las estadísticas de un jugador en el siguiente formato: "{clave}: {valor}".
    Recibe:
        jugador (dict): Un diccionario que contiene la información del jugador, incluyendo las estadísticas.
    Retorna:
        None: Esta función no devuelve ningún valor. Muestra las estadísticas del jugador directamente en la salida.
    """
    estadisticas = jugador["estadisticas"]
    mensaje = ""
    for clave, valor in estadisticas.items():
        clave = clave.replace("_", " ")
        mensaje += "{0}: {1}\n".format(clave.capitalize(), valor)
    print (mensaje)
    return mensaje

#3 - Guardar estadisticas en formato CSV

def exportar_csv(cadena: str, nombre_archivo: str) -> None:
    """
    Exporta una cadena de texto a un archivo CSV.
    Recibe:
        cadena (str): La cadena de texto a exportar.
        nombre_archivo (str): El nombre del archivo CSV a crear o sobrescribir.
    """
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(cadena)
        


#4 - Buscar jugador por nombre y mostrar sus logros

def buscar_nombre_logros(lista_jugadores: list[dict], patron_regex: str) -> list:
    """
    Busca y devuelve los logros de un jugador cuyo nombre coincide con un patrón de expresión regular.
    Recibe:
        lista_jugadores (list[dict]): Una lista de diccionarios que contiene información de los jugadores.
        patron_regex (str): El patrón de expresión regular a utilizar para buscar el nombre del jugador.
    Retorna:
        list: Una lista de logros del jugador cuyo nombre coincide con el patrón de expresión regular.
            Si no se encuentra ningún jugador con el nombre buscado, se solicita un nuevo patrón al usuario.
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
    Encuentra el índice del jugador con el valor mínimo o máximo de una clave específica en una lista de jugadores.
    Recibe:
        lista_jugadores (list[dict]): Una lista de diccionarios que contiene información de los jugadores.
        key (str): La clave específica dentro de cada diccionario de jugador para comparar.
        modo (str): El modo de comparación. Puede ser "asc" (ascendente) o "desc" (descendente).
        key_2 (str, optional): La segunda clave específica dentro de un diccionario de cada diccionario de jugador para comparar.
        Por defecto es "1".
    Retorna:
        int: El índice del jugador con el valor mínimo o máximo de la clave específica.
            Si la lista de jugadores está vacía, se devuelve 0.
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
    Ordena una lista de jugadores en orden ascendente o descendente según una clave específica.
    Recibe:
        lista_jugadores (list): Una lista de elementos a ser ordenados.
        key (str): La clave específica dentro de cada elemento para realizar la comparación.
        modo (str): El modo de ordenación. Puede ser "asc" (ascendente) o "desc" (descendente).
        key_2 (str, optional): La segunda clave específica dentro de un diccionario de cada diccionario jugador para comparar.
        Por defecto es "1".
    Retorna:
        list: Una lista ordenada en el modo especificado según la clave específica y, opcionalmente, la segunda clave.
    """
    lista_copia = lista_jugadores.copy()
    for i in range(len(lista_jugadores)):
        lista_aux = lista_copia[i:]
        i_min_max = indice_min_max(lista_aux, key, modo, key_2) + i
        lista_copia[i], lista_copia[i_min_max] = lista_copia[i_min_max], lista_copia[i]
    return lista_copia

def calcular_promedio(lista_jugadores: list[dict], key: str) -> float:
    """
    Calcula el promedio de una estadística específica para un conjunto de jugadores.
    Recibe:
        lista_jugadores (list[dict]): Una lista de diccionarios que contiene información de los jugadores.
        key (str): La clave de estadística para la cual se calculará el promedio.
    Retorna:
        float: El promedio de la estadística especificada para el conjunto de jugadores.
    """
    suma_promedios = 0
    estadisticas = {}
    for jugador in lista_jugadores:
        estadisticas = jugador["estadisticas"]
        suma_promedios += estadisticas[key]
    promedio = round((suma_promedios/len(lista_jugadores)), 2)
    print("El promedio de \"{0}\" de todo el equipo es de: {1}".format(formatear_estadistica(lista_jugadores, key) ,promedio))
    return promedio

def mostrar_promedio_y_orden_asc(lista_ordenada: list[dict], modo: str) -> None:
    """
    Muestra el promedio de una estadística específica y la lista ordenada de jugadores en orden alfabético ascendente.
    Recibe:
        lista_ordenada (list[dict]): Una lista ordenada de diccionarios que contiene información de los jugadores.
        modo (str): La clave de estadística para la cual se calculará el promedio y se ordenará la lista.
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
    Verifica si un jugador en la lista tiene logros que si se encuentra en el Salón de la Fama del Baloncesto
    o en el Salón de la Fama del Baloncesto Universitario.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios que contiene información de los jugadores.
        regex_nombre (str): Expresión regular utilizada para buscar el nombre del jugador.
    Retorna:
        bool: True si el jugador es miembro del Salón de la Fama del Baloncesto,
            False si el jugador es miembro del Salón de la Fama del Baloncesto Universitario,
            None si no se encuentra ningún logro correspondiente.
    """
    logros = buscar_nombre_logros(lista_jugadores, regex_nombre)
    if (re.search(r"\bMiembro del Salon de la Fama del Baloncesto\b", logro) for logro in logros):
        return True
    elif (re.search(r"\bMiembro del Salon de la Fama del Baloncesto Universitario\b", logro) for logro in logros):
        return False 

#7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.

def jugador_mayor_estadistica(lista_jugadores: list[dict], clave_estadisticas: str) -> dict:
    """
    Encuentra al jugador con la mayor estadística en una lista de jugadores.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios que contiene información de los jugadores.
        clave_estadisticas (str): La clave de estadística a considerar para encontrar al jugador con la mayor estadística.
    Retorna:
        dict: Diccionario que contiene la información de las estadisticas del jugador con la mayor estadística.
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
    Muestra la información del jugador con la mayor estadística en una clave de estadísticas específica en una lista de jugadores.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios que contiene información de los jugadores.
        clave_estadisticas (str): La clave de estadística a considerar para encontrar al jugador con la mayor estadística.
    Retorna:
        None
    """
    jugador_mayor_clave = jugador_mayor_estadistica(lista_jugadores, clave_estadisticas)
    for jugador in lista_jugadores:
        dic_estadistica = jugador["estadisticas"]
        if dic_estadistica[clave_estadisticas] == jugador_mayor_clave[clave_estadisticas]:
            mensaje = "{0}".format(formatear_jugador(jugador, jugador_mayor_clave, clave_estadisticas))
            return mensaje

                    
def comparacion_valores_estadisticas(lista_jugadores: list[dict], key: str, valor_comparacion: int) -> list[dict]:
    """
    Compara los valores de una estadística específica en una lista de jugadores y devuelve una lista de jugadores
    cuyos valores en esa estadística son mayores que un valor de comparación dado.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios que contiene información de los jugadores.
        key (str): La clave de estadística a comparar.
        valor_comparacion (int): El valor de comparación.
    Retorna:
        list[dict]: Una nueva lista de jugadores cuyos valores en la estadística son mayores que el valor de comparación.
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
    Muestra las estadísticas de los jugadores en la lista.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios con información de jugadores.
        key (str): Estadística que se desea mostrar.
    Retorna:
        None
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
    Valida si el numero a comparar es mayor al mayor valor de estadisticas a comparar.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios con información de jugadores.
        key (str): Estadística que se desea comparar.
        valor_comparacion (int): Valor de comparación.
    Retorna:
        bool: True si alguna estadística es mayor o igual al valor de comparación, False en caso contrario.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        dict_mayor_key_estadistica = jugador_mayor_estadistica(lista_copia, key)
        if dict_mayor_key_estadistica[key] >= valor_comparacion:
            return True
        else:
            return False


def comparacion_logros(lista_jugadores: list[dict]) -> dict:
    """
    Compara los logros de los jugadores y devuelve el jugador con la mayor cantidad de logros.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios con información de jugadores.
    Retorna:
        dict: Diccionario que representa al jugador con la mayor cantidad de logros.
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
    Obtiene el ranking de un jugador basado en una estadística específica y un patrón de nombre.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios con información de jugadores.
        estadistica_ranking (str): Estadística utilizada para el ranking.
        regex_nombre (str): Patrón de nombre del jugador para buscar en el ranking.
    Retorna:
        int: Posición del jugador en el ranking (+1 para lograr una lista valida de rankings).
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
    Crea un diccionario con las estadísticas de un jugador específico.
    Recibe:
        lista_jugadores (list[dict]): Lista de diccionarios con información de jugadores.
        regex_nombre (str): Expresión regular para buscar el nombre del jugador.
    Retorna:
        dict: Diccionario con las estadísticas del jugador encontrado. Si no se encuentra el jugador,
        el diccionario estará vacío.
    """
    if lista_jugadores:
        lista_copia = lista_jugadores.copy()
        dict_jugador = {}
        for jugador in lista_copia:
            if regex_nombre in jugador["nombre"]:
                dict_jugador["nombre"] = jugador["nombre"]
                dict_jugador["puntos_totales"] = ranking_por_estadistica(lista_copia,"puntos_totales",jugador["nombre"])
                dict_jugador["rebotes_totales"] = ranking_por_estadistica(lista_copia,"rebotes_totales",jugador["nombre"])
                dict_jugador["asistencias_totales"] = ranking_por_estadistica(lista_copia,"asistencias_totales",jugador["nombre"])
                dict_jugador["robos_totales"] = ranking_por_estadistica(lista_copia,"robos_totales",jugador["nombre"])
        return dict_jugador

def lista_dict(lista_jugadores: list) -> list[dict]:
    """
    Crea una lista de diccionarios donde cada uno corresponde a un jugador y el ranking de sus estadísticas.
    Recibe:
        lista_jugadores (list): Lista de jugadores.
    Retorna:
        list[dict]: Lista de diccionarios con las estadísticas de cada jugador.
    """
    lista_dict = []
    dic_jugador = {}
    for jugadores in lista_jugadores:         
        dic_jugador = crear_dict_estadistica_jugador(lista_jugadores, jugadores["nombre"])
        lista_dict.append(dic_jugador)
    return lista_dict

def generar_data_csv(lista_diccionarios):
    """
    La función genera una cadena CSV a partir de una lista de diccionarios que contienen estadísticas de jugadores.
    Recibe:
    Una lista de diccionarios, donde cada diccionario representa a un jugador y contiene su nombre,
    puntos totales, rebotes totales, asistencias totales y robos totales.
    Retorna:
    Una cadena en formato CSV que incluye los datos de los jugadores en la lista de diccionarios de entrada.
    La primera fila del CSV contiene los encabezados "Jugador, Puntos, Rebotes, Asistencias, Robos",
    y cada fila subsiguiente contiene los datos de un jugador, con su nombre, puntos totales, rebotes totales,
    asistencias totales y robos totales separados por comas.
    """
    cadena_csv = "Jugador, Puntos, Rebotes, Asistencias, Robos"
    for jugador in lista_diccionarios:
        cadena_csv += "\n{0}, {1}, {2}, {3}, {4}".format(jugador['nombre'],jugador['puntos_totales'],jugador['rebotes_totales'],jugador['asistencias_totales'],jugador['robos_totales'])
    return cadena_csv
