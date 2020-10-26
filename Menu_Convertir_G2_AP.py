import os

import Menu_Crear_Gramatica_Tipo_2
import Automata_Pila

global lista_automatas
lista_automatas = []


def devolver_lista():
    return lista_automatas


def lista_automatas_vacia():
    if len(lista_automatas) == 0:
        return True
    return False


def buscar_automata(nombre):
    if not lista_automatas_vacia():
        for ap in lista_automatas:
            if ap.nombre == nombre:
                return ap
    return None


def obtener_gramatica():
    os.system("cls")
    global gramatica
    busqueda = input("Escriba el nombre de la gramatica que desea convertir: ")
    if Menu_Crear_Gramatica_Tipo_2.buscar_gramatica(busqueda) is not None:
        gramatica = Menu_Crear_Gramatica_Tipo_2.buscar_gramatica(busqueda)
        return True
    else:
        return False


def menu_principal():
    if obtener_gramatica() is False:
        input("Esta gramatica no existe, presione enter...")
        return
    opcion = 0
    while opcion != 3:
        opcion = 0
        print("----------Convertir Gramatica a Automata de Pila----------")
        print("1) Convertir")
        print("2) Visualizar Automata de Pila")
        print("3) Salir")
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                os.system("cls")
                if buscar_automata(gramatica.nombre) is None:
                    dibujar_automata(convertir())
                else:
                    aux = 0
                    while aux < len(lista_automatas):
                        if lista_automatas[aux].nombre == gramatica.nombre:
                            lista_automatas.pop(aux)
                        aux += 1
                    convertir()
            elif opcion == 2:
                ver_detalle()
            elif opcion == 3:
                break
            else:
                input("Opcion invalida, presione enter")
        except ValueError as e:
            input("Opcion invalida, presione enter")


def convertir():
    automata = Automata_Pila.Automata_Pila(gramatica.nombre)
    automata.agregar_estado("Io")
    automata.agregar_estado("p")
    automata.agregar_estado("q")
    automata.agregar_estado("f")

    # Agrega cada terminal de la gramatica al alfabeto del automata
    for ter in gramatica.terminales:
        automata.alfabeto_maquina.append(ter)

    # Agrega terminales y no terminales de la gramatica a los simbolos de pila
    for ter in gramatica.terminales:
        automata.simbolos_pila.append(ter)
    for n_t in gramatica.no_terminales:
        automata.simbolos_pila.append(n_t.no_terminal)

    # Agrega las transiciones
    # Transicion de tipo 1
    automata.agregar_transicion("Io", "epsilon", "epsilon", "p", "#")
    automata.agregar_transicion("p", "epsilon", "epsilon", "q", gramatica.no_terminal_inicial)

    # Transicion de tipo 2
    for no_ter in gramatica.no_terminales:
        for pr in no_ter.listaProducciones:
            automata.agregar_transicion("q", "epsilon", no_ter.no_terminal, "q", pr.produccion)

    # Transicion de tipo 3
    for ter in gramatica.terminales:
        automata.agregar_transicion("q", ter, ter, "q", "epsilon")

    # Transicion final
    automata.agregar_transicion("q", "epsilon", "#", "f", "epsilon")
    # Agrega el automata a la lista
    lista_automatas.append(automata)
    return automata

def ver_detalle():
    automata = buscar_automata(gramatica.nombre)
    print("\n Nombre Automata: " + automata.nombre)

    estados = ""
    for es in automata.estados:
        estados = estados + es.nombre + ", "
    print("S: { " + estados[:len(estados) - 1] + " }")

    alfabeto = ""
    for al in automata.alfabeto_maquina:
        alfabeto = alfabeto + al + ", "
    print("E: { " + alfabeto[:len(alfabeto) - 1] + " }")

    sim_pi = ""
    for sp in automata.simbolos_pila:
        sim_pi = sim_pi + sp + ", "
    print("r: { " + sim_pi[:len(sim_pi) - 1] + " }")

    print("L: " + automata.estado_inicial)
    print("F: " + automata.estado_aceptacion)
    print("T:")
    for es in automata.estados:
        for tr in es.transiciones:
            rees = ""
            for ree in tr.reescritura:
                rees = rees + ree
            print("(" + es.nombre + ", " + tr.lectura + ", " + tr.tope_pila + "; " + tr.estado_llegada + ", " + rees + ")")


def dibujar_automata(automata):
    aut = open("C:/Users/solis/OneDrive/Escritorio/Salidas/" + automata.nombre + "_ap.dot", "w+")
    aut.write("digraph " + automata.nombre + "{\n")
    cade = ""
    ree = ""
    for es in automata.estados:
        for tr in es.transiciones:
            for re in tr.reescritura:
                ree = ree + re
            cade = es.nombre + "->" + tr.estado_llegada + " [label=\"" + es.nombre + "," + tr.lectura + "," + tr.tope_pila + "; " + tr.estado_llegada + ", " + ree + "\"]\n"
            aut.write(cade)
            cade = ""
            ree = ""
    aut.write("f [shape=doublecircle]\n")
    aut.write("}")
    aut.close()
    os.system("dot C:/Users/solis/OneDrive/Escritorio/Salidas/" + automata.nombre + "_ap.dot" +
              " -o C:/Users/solis/OneDrive/Escritorio/Salidas/" + automata.nombre + "_ap.png -Tpng")
