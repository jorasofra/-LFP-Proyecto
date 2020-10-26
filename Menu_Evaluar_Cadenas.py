import os
import Menu_Crear_Gramatica
import Menu_Crear_AFD
import Gramatica


def menu_principal():
    os.system("cls")
    global automata
    global gramatica
    automata = None
    gramatica = None
    nombre = input("Ingrese el nombre del AFD o Gramatica que desea evaluar: ")
    if existe_automata(Menu_Crear_AFD.devolver_automatas(), nombre):
        automata = buscar_automata(Menu_Crear_AFD.devolver_automatas(), nombre)
    elif existe_gramatica(Menu_Crear_Gramatica.devolverLista(), nombre):
        gramatica = buscar_gramatica(Menu_Crear_Gramatica.devolverLista(), nombre)
    else:
        print("El nombre que busca no existe como automata o gramatica")
        input("Presione enter para salir")
        return

    opcion = 0
    while opcion != 5:
        os.system("cls")
        print("----------Menu Evaluar Cadenas----------")
        print("1) SOLO VALIDAR")
        print("2) RUTA EN AFD")
        print("3) EXPANDIR CON GRAMATICA")
        print("4) AYUDA")
        print("5) SALIR")
        try:
            opcion = int(input("Seleccione una opcion: "))
        except:
            print("")

        if opcion == 1:
            cadena = input("Ingrese la cadena que desea evaluar: ")
            if automata is not None:
                automata.evaluar_cadena(cadena)
            elif gramatica is not None:
                gramatica.evaluar_cadena(cadena)
        elif opcion == 2:
            cadena = input("Ingrese la cadena que desea evaluar: ")
            if automata is not None:
                automata.ruta_Cadena(cadena)
            elif gramatica is not None:
                print()
        elif opcion == 3:
            cadena = input("Ingrese la cadena que desa evaluar: ")
            if automata is not None:
                gr = convertir_afd_gramatica()
                gr.expansion(cadena)
        elif opcion == 4:
            os.system("cls")
            print("Lenguajes Formales y de Programacion Seccion A")
            print("Auxiliar: Elmer Real")
            print("4")
            input("Presione enter")
        elif opcion == 5:
            break
        else:
            input("Opcion invalida, presone enter")


def buscar_automata(lista_automata, nombre):
    for aux in lista_automata:
        if aux.nombre == nombre:
            return aux


def buscar_gramatica(lista_gramatica, nombre):
    for aux in lista_gramatica:
        if aux.nombre == nombre:
            return aux


def existe_automata(lista_automata, nombre):
    for aux in lista_automata:
        if aux.nombre == nombre:
            return True
    return False


def existe_gramatica(lista_gramatica, nombre):
    for aux in lista_gramatica:
        if aux.nombre == nombre:
            return True
    return False


def convertir_afd_gramatica():
    nueva_gramatica = Gramatica.Gramatica(automata.nombre)
    nueva_gramatica.agregar_terminales("epsilon")
    for aux in automata.alfabeto:
        nueva_gramatica.agregar_terminales(aux)
    for aux1 in automata.estados:
        nueva_gramatica.agregar_no_terminales(aux1.nombre)
    nueva_gramatica.determinar_no_terminal_inicial(automata.estado_inicial)
    for aux2 in automata.estado_aceptacion:
        for aux3 in nueva_gramatica.listaNoTerminales:
            if aux2 == aux3.no_terminal:
                nueva_gramatica.definir_produccion(aux3.no_terminal, "epsilon")
    for aux4 in automata.estados:
        for aux5 in nueva_gramatica.listaNoTerminales:
            if aux4.nombre == aux5.no_terminal:
                for aux6 in aux4.lista_transiciones:
                    produccion = aux6.simbolo + " " + aux6.estadoDestino
                    aux5.agregar_produccion(produccion)
    return nueva_gramatica

def convertir_gramatica_afd():
    print()