import Automata
import os

global listaAutomatas
listaAutomatas = []
global nombreAutomata
nombreAutomata = ""
global estado
global nombreEstado
nombreEstado = ""


def devolver_automatas():
    return listaAutomatas


def menu_principal():
    os.system("cls")
    nombreAutomata = input("Ingrese el nombre del automata: ")
    if verificar_afd_creado(nombreAutomata):
        global automata
        automata = obtener_afd_creado(nombreAutomata)
    else:
        automata = Automata.Automata(nombreAutomata)
        listaAutomatas.append(automata)
    os.system("cls")
    opcion = 0
    while opcion != 7:
        os.system("cls")
        print("----------Menu de Automatas----------")
        print("1) INGRESAR ESTADOS")
        print("2) INGRESAR ALFABETO")
        print("3) DEFINIR ESTADO INICIAL")
        print("4) DEFINIR ESTADOS DE ACEPTACION")
        print("5) DEFINIR TRANSICIONES")
        print("6) AYUDA")
        print("7) SALIR")
        try:
            opcion = int(input("Seleccione una opcion: "))
        except:
            print()
        if opcion == 1:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Ingresar Estados----------")
                print("1) INGRESAR NUEVO ESTADO")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    nombreEstado = input("Ingrese el nombre del estado: ")
                    ingresar_estado(nombreEstado)
                elif seleccion == 2:
                    break
                else:
                    print("Opcion incorrecta, presione enter")
                    input()
        elif opcion == 2:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Ingresar Alfabeto----------")
                print("1) INGRESAR NUEVO SIMBOLO")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    simbolo = input("Ingrese el simbolo: ")
                    ingresar_alfabeto(simbolo)
                elif seleccion == 2:
                    break
                else:
                    print("Opcion incorrecta, presione enter")
                    input()
        elif opcion == 3:
            print("----------Definir Estado Inicial----------")
            estado_inicial = input("Ingrese el nombre del estado que desea como inicial: ")
            definir_estado_inicial(estado_inicial)
        elif opcion == 4:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Estados de Aceptacion----------")
                print("1) DEFINIR NUEVO ESTADO DE ACEPTACION")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    nombre_estado = input("Escriba el nombre de un estado existente: ")
                    definir_estado_aceptacion(nombre_estado)
                elif seleccion == 2:
                    break
                else:
                    print("Opcion incorrecta, presione enter")
                    input()
        elif opcion == 5:
            seleccion = 0
            while seleccion != 3:
                os.system("cls")
                print("----------Menu de Transiciones----------")
                print("1) MODO 1")
                print("2) MODO 2")
                print("3) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    os.system("cls")
                    cadena = input("Ingrese la transicion: ")
                    transicion_tipo_1(cadena)
                elif seleccion == 2:
                    os.system("cls")
                    cadena_terminales = input("Ingrese los terminales: ")
                    cadena_estados = input("Ingrese los estados: ")
                    cadena_transiciones = input("Ingrese las transiciones: ")
                    transicion_tipo_2(cadena_terminales, cadena_estados, cadena_transiciones)
        elif opcion == 6:
            os.system("cls")
            print("Lenguajes Formales y de Programacion Seccion A")
            print("Auxiliar: Elmer Real")
            print("4")
            input("Presione enter")
        elif opcion == 7:
            break
        else:
            print("Opcion invalida, presione enter")
            input()
            os.system("cls")


## Verifica si el afd ingresado ya fue creado
def verificar_afd_creado(nombre):
    for x in listaAutomatas:
        if x.nombre == nombre:
            return True
    return False


##Retorna el afd credado que se desea modificar
def obtener_afd_creado(nombre):
    for x in listaAutomatas:
        if x.nombre == nombre:
            return x


## Crea nuevo estado y lo agrega a la lista de estados
def ingresar_estado(nombre):
    automata.agregar_estado(nombre)


##Ingresa nuevo simbolo al automata
def ingresar_alfabeto(simbolo):
    automata.agregar_simbolo_alfabeto(simbolo)


def definir_estado_inicial(nombre):
    automata.definir_estado_inicial(nombre)


def definir_estado_aceptacion(nombre):
    automata.definir_estado_aceptacion(nombre)


##Metodos de ingreso de transiciones
def transicion_tipo_1(cadena):
    cad1 = cadena.replace(",", " ")
    cad2 = cad1.replace(";", " ")
    datos = cad2.split(" ")
    simbolo = datos.pop(2)
    destino = datos.pop(1)
    origen = datos.pop(0)
    automata.definir_transicion(origen, destino, simbolo)


def transicion_tipo_2(cadena_terminales, cadena_estados, cadena_transiciones):
    cadena_terminales = cadena_terminales.replace("[", "")
    cadena_terminales = cadena_terminales.replace("]", "")

    cadena_estados = cadena_estados.replace("[", "")
    cadena_estados = cadena_estados.replace("]", "")

    cadena_transiciones = cadena_transiciones.replace("[", "")
    cadena_transiciones = cadena_transiciones.replace("]", "")

    alfabeto = cadena_terminales.split(",")
    estados = cadena_estados.split(",")
    transiciones = cadena_transiciones.split(";")
    if len(transiciones) == len(estados):
        for aux in estados:
            transi = transiciones.pop(0).split(",")
            if len(transi) == len(alfabeto):
                for au1 in alfabeto:
                    tran = transi.pop(0)
                    if tran != "-":
                        automata.definir_transicion(aux, tran, au1)

            else:
                print("La cantidad de transiciones no coinciden con la de simbolos")
    else:
        print("La cantidad de transiciones no coinciden con la de estados")
