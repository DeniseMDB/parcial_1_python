import json
import re
import lib_funciones as lib


def print_menu():
    menu =\
    """
    1 - Mostrar lista de jugadores del Dream Team (Nombre jugador - Posicion)
    2 - Seleccionar jugador por indice y mostrar sus estadisticas
    3 - Guardar estadisticas en formato CSV
    4 - Buscar jugador por nombre y mostrar sus logros
    5 - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
        ordenado por nombre de manera ascendente.
    6 - Buscar si el jugador es miembro del Salón de la Fama del Baloncesto.
    7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8 - Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9 - Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10 - Mostrar jugadores que han promediado más puntos por partido que un valor ingresado.
    11 - Mostrar jugadores que han promediado más rebotes por partido que un valor ingresado.
    12 - Mostrar jugadores que han promediado más asistencias por partido que un valor ingresado.
    13 - Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14 - Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15 - Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a un valor ingresado.
    16 - Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al 
        jugador con la menor cantidad de puntos por partido. 
    17 - Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    18 - Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a un valor ingresado.
    19 - Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
    20 - Mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje
    de tiros de campo superior a un valor ingresado.
    """

    print(menu)


def ejercicios_examen():
    ruta_json = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\parcial_1\\dt.json'
    ruta_csv = ""
    lista_jugadores = lib.leer_archivo(ruta_json)
    lista_copia = []
    while True:
        print_menu()
        respuesta = input("Ingrese la opcion elegida: >> ")
        respuesta = lib.validar_numero(respuesta, "[1-9]{1,2}")
        match respuesta:
            case 1:
                accion = "Lista de jugadores del Dream Team: "
                lista_copia = lista_jugadores.copy()
                lista_nombres = lib.mostrar_lista_jugadores(lista_copia)
                lib.imprimir_mensaje(accion, "Success")
                print(lista_nombres)
                lib.limpiar_consola()
            case 2:
                accion = "Las estadisticas del jugador elegido son: "
                lista_copia = lista_jugadores.copy()
                indice = input("Ingrese el indice del jugador: ")
                indice = lib.validar_numero(indice,"^[1-9]{1,2}$")
                indice = lib.validar_lista(lista_copia, indice)
                lib.imprimir_mensaje(accion, "Success")
                jugador = lista_copia[indice]
                archivo_estadisticas = lib.mostrar_estadisticas_indice(jugador)
                lib.limpiar_consola()
            case 3:
                accion = "Exito"
                lista_copia = lista_jugadores.copy()
                lib.imprimir_mensaje(accion, "Success")
                lib.exportar_csv(archivo_estadisticas,jugador)
                lib.limpiar_consola()
            case 4:
                accion = "Logros del jugador elegido :"
                lista_copia = lista_jugadores.copy()
                patron_regex = input("Ingrese el nombre del jugador: ")
                logros = lib.buscar_nombre_logros(lista_copia, patron_regex)
                cadena_logros = ""
                if logros:
                    lib.imprimir_mensaje(accion, "Success")
                    for logro in logros:
                        cadena_logros += "{0}\n".format(logro)
                    print(cadena_logros)
                lib.limpiar_consola()
            case 5:
                accion = "Promedio puntos por partido y lista ordenada: "
                lista_copia = lista_jugadores.copy()
                lib.imprimir_mensaje(accion, "Success")
                lib.mostrar_promedio_y_orden_asc(lista_copia)
                lib.limpiar_consola()
            case 6:
                lista_copia = lista_jugadores.copy()
                jugador = input("Ingrese el nombre del jugador:  ")
                if lib.es_miembro_fama:
                    accion = "El jugador {0} es Miembro del Salon de la Fama del Baloncesto".format(jugador)
                    exito = "Success"
                else:
                    accion = "El jugador {0} no es Miembro del Salon de la Fama del Baloncesto".format(jugador)
                    exito = "Error"
                lib.imprimir_mensaje(accion, exito)
                lib.limpiar_consola()
            case 7:
                accion = "El jugador con la mayor cantidad de rebotes totales es: "
                lista_copia = lista_jugadores.copy()
                key ="rebotes_totales"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 8:
                accion = "El jugador con el mayor porcentaje tiros de campo es: "
                lista_copia = lista_jugadores.copy()
                key ="porcentaje_tiros_de_campo"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 9:
                accion = "El jugador con la mayor asistencias totales es: "
                lista_copia = lista_jugadores.copy()
                key = "asistencias_totales"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 10:
                lista_copia = lista_jugadores.copy()
                key = "promedio_puntos_por_partido"
                valor_a_comparar = input("Ingrese un valor ")
                valor_a_comparar = lib.validar_numero(valor_a_comparar,"[1-9]{1,2}")
                if lib.validar_comparacion_estadistica(lista_copia, key, valor_a_comparar):
                    lista_comparacion = lib.comparacion_valores_estadisticas(lista_jugadores,key, valor_a_comparar)
                    accion = "Los jugadores que han promediado más de {0} en puntos por partido son: ".format(valor_a_comparar)
                    lib.imprimir_mensaje(accion,"Success" )
                    lib.mostrar_jugador_estadisticas(lista_comparacion, key)
                    lib.limpiar_consola()
                else:
                    lib.imprimir_mensaje("El numero ingresado es mayor que el mayor valor a comparar","Error" )
            case 11:
                lista_copia = lista_jugadores.copy()
                key = "promedio_rebotes_por_partido"
                valor_a_comparar = input("Ingrese un valor ")
                valor_a_comparar = lib.validar_numero(valor_a_comparar,"[1-9]{1,2}")
                if lib.validar_comparacion_estadistica(lista_copia, key, valor_a_comparar):
                    lista_comparacion = lib.comparacion_valores_estadisticas(lista_jugadores,key, valor_a_comparar)
                    accion = "Los jugadores que han promediado más de {0} en rebotes por partido son: ".format(valor_a_comparar)
                    lib.imprimir_mensaje(accion,"Success" )
                    lib.mostrar_jugador_estadisticas(lista_comparacion, key)
                    lib.limpiar_consola()
                else:
                    lib.imprimir_mensaje("El numero ingresado es mayor que el mayor valor a comparar","Error" )
            case 12:
                lista_copia = lista_jugadores.copy()
                key = "promedio_asistencias_por_partido"
                valor_a_comparar = input("Ingrese un valor ")
                valor_a_comparar = lib.validar_numero(valor_a_comparar,"[1-9]{1,2}")
                if lib.validar_comparacion_estadistica(lista_copia, key, valor_a_comparar):
                    lista_comparacion = lib.comparacion_valores_estadisticas(lista_jugadores,key, valor_a_comparar)
                    accion = "Los jugadores que han promediado más de {0} en asistencias por partido son: ".format(valor_a_comparar)
                    lib.imprimir_mensaje(accion,"Success" )
                    lib.mostrar_jugador_estadisticas(lista_comparacion, key)
                    lib.limpiar_consola()
                else:
                    lib.imprimir_mensaje("El numero ingresado es mayor que el mayor valor a comparar","Error" )
            case 13:
                accion = "El jugador con la mayor cantidad de robos totales es: "
                lista_copia = lista_jugadores.copy()
                key = "robos_totales"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 14:
                accion = "El jugador con la mayor cantidad de bloqueos totales: "
                lista_copia = lista_jugadores.copy()
                key = "bloqueos_totales"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 15:
                lista_copia = lista_jugadores.copy()
                key = "porcentaje_tiros_libres"
                valor_a_comparar = input("Ingrese un valor ")
                valor_a_comparar = lib.validar_numero(valor_a_comparar,"[1-9]{1,2}")
                if lib.validar_comparacion_estadistica(lista_copia, key, valor_a_comparar):
                    lista_comparacion = lib.comparacion_valores_estadisticas(lista_jugadores,key, valor_a_comparar)
                    accion = "Los jugadores que han promediado más de {0} en porcentaje de tiros libres son: ".format(valor_a_comparar)
                    lib.imprimir_mensaje(accion,"Success" )
                    lib.mostrar_jugador_estadisticas(lista_comparacion, key)
                    lib.limpiar_consola()
                else:
                    lib.imprimir_mensaje("El numero ingresado es mayor que el mayor valor a comparar","Error" )
            case 16:
                pass
            case 17:
                pass
            case 18:
                lista_copia = lista_jugadores.copy()
                key = "porcentaje_tiros_triples"
                valor_a_comparar = input("Ingrese un valor ")
                valor_a_comparar = lib.validar_numero(valor_a_comparar,"[1-9]{1,2}")
                if lib.validar_comparacion_estadistica(lista_copia, key, valor_a_comparar):
                    lista_comparacion = lib.comparacion_valores_estadisticas(lista_jugadores,key, valor_a_comparar)
                    accion = "Los jugadores que han promediado más de {0} en porcentaje de tiros triples son: ".format(valor_a_comparar)
                    lib.imprimir_mensaje(accion,"Success" )
                    lib.mostrar_jugador_estadisticas(lista_comparacion, key)
                    lib.limpiar_consola()
                else:
                    lib.imprimir_mensaje("El numero ingresado es mayor que el mayor valor a comparar","Error" )
            case 19:
                accion = "El jugador con la mayor cantidad de temporadas es: "
                lista_copia = lista_jugadores.copy()
                key ="temporadas"
                lib.imprimir_mensaje(accion,"Success" )
                print(lib.mostrar_jugador_por_clave_estadistica(lista_copia, key))
                lib.limpiar_consola()
            case 20:
                pass
            case 21:
                pass
            case _:
                # Opción no reconocida, no se realiza ninguna acción
                pass

ejercicios_examen()