import os
import Menu_Crear_Gramatica
import Automata
import Menu_Crear_AFD
import Gramatica


def menu_principal():
    opcion = 0
    while opcion != 3:
        opcion = 0
        os.system("cls")
        print("---------------Menu Principal---------------")
        print("1) CARGAR ARCHIVO AFD")
        print("2) CARGAR ARCHIVO GRAMATICA")
        print("3) SALIDA")
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("")
        if opcion == 1:
            ruta = input("Ingrese la ruta del archivo: ")
            analizar_automata(ruta)
        elif opcion == 2:
            ruta = input("Ingrese la ruta del archivo: ")
            analizar_gramatica(ruta)
        elif opcion == 3:
            os.system("cls")
            break
        else:
            input("Opcion invalida, presione enter")


def analizar_automata(ruta):
    if verificar_extension_automata(ruta):
        try:
            archivo = open(ruta, "r")
            contenido = archivo.read()
            archivo.close()
            analizar_archivo_automata(contenido)
            Menu_Crear_AFD.devolver_automatas().append(nuevo_automata)
        except FileNotFoundError as e:
            input("El archivo no existe, presione enter")


def analizar_gramatica(ruta):
    if verificar_extension_gramatica(ruta):
        try:
            archivo = open(ruta, "r")
            contenido = archivo.read()
            archivo.close()
            analizar_archivo_gramatcia(contenido)
            Menu_Crear_Gramatica.devolverLista().append(nueva_gramatica)
        except FileNotFoundError as e:
            input("El archivo no existe, presione enter")


def verificar_extension_automata(ruta):
    nombre, extension = os.path.split(ruta)
    extension = extension.split(".")
    global nuevo_automata
    if extension[1] == "afd":
        nuevo_automata = Automata.Automata(extension[0])
        return True
    else:
        input("Archivo no valido, presione enter")
        return False


def verificar_extension_gramatica(ruta):
    nombre, extension = os.path.split(ruta)
    extension = extension.split(".")
    global nueva_gramatica
    if extension[1] == "grm":
        nueva_gramatica = Gramatica.Gramatica(extension[0])
        return True
    else:
        return False


def analizar_archivo_automata(contenido):
    aux = contenido.split('\n')
    contador_linea = 1
    for linea in aux:
        separada = linea.split(";")
        transicion = separada[0].split(",")
        nuevo_automata.agregar_estado(transicion[0])
        nuevo_automata.agregar_estado(transicion[1])
        nuevo_automata.agregar_simbolo_alfabeto(transicion[2])
        if contador_linea == 1:
            nuevo_automata.definir_estado_inicial(transicion[0])
        nuevo_automata.definir_transicion(transicion[0], transicion[1], transicion[2])
        aceptacion = separada[1].split(",")
        if aceptacion[0] == "true":
            nuevo_automata.definir_estado_aceptacion(transicion[0])
        if aceptacion[1] == "true":
            nuevo_automata.definir_estado_aceptacion(transicion[1])
        contador_linea += 1


def analizar_archivo_gramatcia(contenido):
    aux = contenido.split('\n')
    contador_linea = 1
    for linea in aux:
        separada = linea.split(">")
        nueva_gramatica.agregar_no_terminales(separada[0])
        produccion = separada[1].split(" ")
        for ter in produccion:
            if ter.islower() or ter.isnumeric():
                nueva_gramatica.agregar_terminales(ter)
            elif ter.isupper():
                nueva_gramatica.agregar_no_terminales(ter)
        if contador_linea == 1:
            nueva_gramatica.determinar_no_terminal_inicial(separada[0])
        nueva_gramatica.definir_produccion(separada[0], separada[1])
        contador_linea += 1
