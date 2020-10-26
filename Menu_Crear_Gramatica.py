import os
import Gramatica

global listaGramaticas
listaGramaticas = []


def devolverLista():
    return listaGramaticas


def menu_principal():
    os.system("cls")
    global nombreGramatica
    nombreGramatica = input("Ingrese el nombre de la Gramatica: ")
    if verificar_gramatica_existente(nombreGramatica):
        global gramatica
        gramatica = obtener_gramatica_existente(nombreGramatica)
    else:
        gramatica = Gramatica.Gramatica(nombreGramatica)
        listaGramaticas.append(gramatica)
    os.system("cls")
    opcion = 0
    while opcion != 6:
        os.system("cls")
        print("----------Menu de Gramaticas----------")
        print("1) INGRESAR NO TERMINALES")
        print("2) INGRESAR TERMINALES")
        print("3) DEFINIR NO TERMINAL INICIAL")
        print("4) DEFINIR PRODUCCIONES")
        print("5) AYUDA")
        print("6) SALIR")
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError as e:
            print()
        if opcion == 1:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Ingresar No Terminales----------")
                print("1) INGRESAR NUEVO NO TERMINAL")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    no_terminal = input("Ingrese el no terminal: ")
                    agregar_no_terminales(no_terminal)
                elif seleccion == 2:
                    break
                else:
                    input("Opcion incorrecta, presione enter...")
        elif opcion == 2:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Ingresar Terminales----------")
                print("1) INGRESAR NUEVO TERMINAL")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    terminal = input("Ingrese el terminal: ")
                    agregar_terminales(terminal)
                elif seleccion == 2:
                    break
                else:
                    input("Opcion incorrecta, presione enter...")
        elif opcion == 3:
            os.system("cls")
            print("----------Definir No Terminal Inicial----------")
            no_terminal = input("Ingrese el no terminal desea como inicial: ")
            definir_no_terminal_inicial(no_terminal)
        elif opcion == 4:
            seleccion = 0
            while seleccion != 2:
                os.system("cls")
                print("----------Definir Producciones----------")
                print("1) INGRESAR NUEVA PRODUCCION")
                print("2) SALIR")
                try:
                    seleccion = int(input("Seleccione una opcion: "))
                except:
                    print()
                if seleccion == 1:
                    cadena = input("Ingrese la produccion: ")
                    definir_producciones(cadena)
                elif seleccion == 2:
                    break
                else:
                    input("Opcion incorrecta, presione enter...")
        elif opcion == 5:
            os.system("cls")
            print("Lenguajes Formales y de Programacion Seccion A")
            print("Auxiliar: Elmer Real")
            print("4")
            input("Presione enter")
        elif opcion == 6:
            break
        else:
            input("Opcion incorrecta, presione enter")


##Verifica si la gramatica ya esta creada
def verificar_gramatica_existente(nombreGramatica):
    for aux in listaGramaticas:
        if aux.nombre == nombreGramatica:
            return True
    return False


## Retorna la gramatica que ya esta creada
def obtener_gramatica_existente(nombreGramatica):
    for aux in listaGramaticas:
        if aux.nombre == nombreGramatica:
            return aux
    return None


def agregar_no_terminales(nombre):
    gramatica.agregar_no_terminales(nombre)


def agregar_terminales(terminal):
    gramatica.agregar_terminales(terminal)


def definir_no_terminal_inicial(no_terminal):
    gramatica.determinar_no_terminal_inicial(no_terminal)


def definir_producciones(cadena):
    noT_produccion = cadena.split(">")
    no_terminal = noT_produccion.pop(0).replace(" ", "")
    p1 = noT_produccion.pop(0)
    producciones = p1.split("|")
    for aux in producciones:
        aux = aux.replace(" ", "", 1)
        gramatica.definir_produccion(no_terminal, aux)
