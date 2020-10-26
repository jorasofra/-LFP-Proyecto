import os

import Gramatica_Tipo_2

global lista_gramaticas
lista_gramaticas = []


def devolver_lista():
    return lista_gramaticas


#Busca la gramatica y la devuelve
def buscar_gramatica(nombre):
    for gr in lista_gramaticas:
        if gr.nombre == nombre:
            return gr
    return None


def menu_principal():
    os.system("cls")
    global gramatica
    nombre = input("Ingrese el nombre de la gramatica: ")
    gramatica = buscar_gramatica(nombre)
    #Si la variable es None ingresa para agregar una nueva gramatica
    if gramatica is None:
        nueva_gramatica = Gramatica_Tipo_2.Gramatica_Tipo_2(nombre)
        lista_gramaticas.append(nueva_gramatica)
        gramatica = buscar_gramatica(nombre)
    opcion = 0
    while opcion != 6:
        opcion = 0
        os.system("cls")
        print("----------Menu de Gramaticas Tipo 2----------")
        print("1) INGRESAR NO TERMINALES")
        print("2) INGRESAR TERMINALES")
        print("3) DEFINIR NO TERMINAL INICIAL")
        print("4) DEFINIR PRODUCCIONES")
        print("5) BORRAR PRODUCCIONES")
        print("6) SALIR")
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                ingresar_no_terminales()
            elif opcion == 2:
                ingresar_terminales()
            elif opcion == 3:
                definir_inicial()
            elif opcion == 4:
                agregar_produccion()
            elif opcion == 5:
                borrar_produccion()
            elif opcion == 6:
                break
            else:
                input("Opcion invalida, presione enter")
        except ValueError as e:
            input("Opcion invalida, persione enter")


def ingresar_no_terminales():
    opcion = 0
    while opcion != 2:
        os.system("cls")
        print("----------Menu de No Terminales----------")
        print("1) INGRESAR NUEVO NO TERMINAL")
        print("2) SALIR")
        try:
            opcion = int(input("Selecciones una opcion: "))
            if opcion == 1:
                no_term = input("Ingrese el no terminal: ")
                #Verifica que lo ingresado este en mayusculas
                if no_term.isupper():
                    gramatica.agregar_no_terminal(no_term)
                else:
                    input("Solo se puede agregar si es letra mayuscula")
            elif opcion == 2:
                break
            else:
                input("Opcion invalida, presione enter")
        except ValueError as e:
            input("Opcion invalida, presione enter")


def ingresar_terminales():
    opcion = 0
    while opcion != 2:
        os.system("cls")
        print("----------Menu de Terminales----------")
        print("1) INGRESAR NUEVO TERMINAL")
        print("2) SALIR")
        try:
            opcion = int(input("Selecciones una opcion: "))
            if opcion == 1:
                term = input("Ingrese el terminal: ")
                # Verifica que lo ingresado sea cualquier cosa, menos mayusculas
                if not term.isupper():
                    gramatica.agregar_terminal(term)
                else:
                    input("Solo se puede agregar si la letra no es mayuscula, o es cualquier otro simbolo")
            elif opcion == 2:
                break
            else:
                input("Opcion invalida, presione enter")
        except ValueError as e:
            input("Opcion invalida, presione enter")


def definir_inicial():
    os.system("cls")
    print("----------Definir No Terminal Inicial----------")
    no_terminal = input("Ingrese el no terminal desea como inicial: ")
    gramatica.determinar_no_terminal_inicial(no_terminal)


def agregar_produccion():
    seleccion = 0
    while seleccion != 2:
        os.system("cls")
        print("----------Definir Producciones----------")
        print("1) INGRESAR NUEVA PRODUCCION")
        print("2) SALIR")
        try:
            seleccion = int(input("Seleccione una opcion: "))
            if seleccion == 1:
                separar_nt_prod(input("Ingrese la produccion: "), 1)
            elif seleccion == 2:
                break
            else:
                input("Opcion incorrecta, presione enter...")
        except ValueError as e:
            print()


def borrar_produccion():
    seleccion = 0
    while seleccion != 2:
        os.system("cls")
        print("----------Borrar Producciones----------")
        print("1) INGRESAR PRODUCCION A BORRAR")
        print("2) SALIR")
        try:
            seleccion = int(input("Seleccione una opcion: "))
            if seleccion == 1:
                separar_nt_prod(input("Ingrese la produccion: "), 2)
            elif seleccion == 2:
                break
            else:
                input("Opcion incorrecta, presione enter...")
        except ValueError as e:
            print()


def separar_nt_prod(cadena, accion):
    try:
        nt_pr = cadena.split(">")
        no_ter = nt_pr.pop(0).replace(" ", "")
        if accion == 1:
            producs = nt_pr.pop(0).split("|")
            for pr in producs:
                r = pr[len(pr) - 1]
                if r == " ":
                    pr = pr[:len(pr) - 1]
                gramatica.definir_produccion(no_ter, pr.replace(" ", "", 1))
        elif accion == 2:
            producs = nt_pr.pop(0).split("|")
            for pr in producs:
                gramatica.borrar_produccion(no_ter, pr.replace(" ", "", 1))
    except IndexError as ie:
        print("No hay produccion")


def imprimir():
    print(gramatica.nombre)
    print("Terminales")
    for t in gramatica.terminales:
        print(t)
    print("\nNo terminales")
    for nt in gramatica.no_terminales:
        print(nt.no_terminal)
        print("Producciones")
        for pr in nt.listaProducciones:
            print(pr.produccion)
        print("")