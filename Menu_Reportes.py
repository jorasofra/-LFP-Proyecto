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
        print("1) VER DETALLE")
        print("2) GENERAR REPORTE")
        print("3) AYUDA")
        print("4) SALIDA")
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError as e:
            print("")

        if opcion == 1:
            if automata is not None:
                imprimir_afd_caracteristicas()
            elif gramatica is not None:
                imprimir_gramatica_caracteristicas()
        elif opcion == 2:
            if automata is not None:
                convertido =  convertir_afd_gramatica()
                imprimir_documento_afd(convertido)
            elif gramatica is not None:
                imprimir_gramatica_caracteristicas()
        elif opcion == 3:
            os.system("cls")
            print("Lenguajes Formales y de Programacion Seccion A")
            print("Auxiliar: Elmer Real")
            print("4")
            input("Presione enter")
        elif opcion == 4:
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


def imprimir_afd_caracteristicas():
    os.system("cls")
    print("Nombre del Automata: " + automata.nombre)
    for alf in automata.alfabeto:
        print("     - Simbolo de alfabeto: " + alf)
    for esta in automata.estados:
        print("     - Estado: " + esta.nombre)
    print("     - Estado inicial: " + automata.estado_inicial)
    for acep in automata.estado_aceptacion:
        print("     - Estado aceptacion: " + acep)
    cadena_transiciones = ""
    for est in automata.estados:
        for tran in est.lista_transiciones:
            cadena_transiciones = cadena_transiciones + est.nombre + "," + tran.estadoDestino + "," + tran.simbolo + ";"
    print("     - Trancisiones: " + cadena_transiciones)
    input("     - Presione enter...")


def imprimir_gramatica_caracteristicas():
    os.system("cls")
    print("Nombre de la Gramatica: " + gramatica.nombre)
    for termi in gramatica.listaTerminales:
        print("     - Terminal: " + termi)
    for notermi in gramatica.listaNoTerminales:
        print("     - No Terminal: " + notermi.no_terminal)
    print("     - No Terminal Inicial: " + gramatica.noTerminalInicial)
    cadena_produc = ""
    for noter in gramatica.listaNoTerminales:
        cadena_produc = cadena_produc + noter.no_terminal + " -> "
        for produc in noter.listaProducciones:
            cadena_produc = cadena_produc + produc.produccion + " | "
        cadena_produc = cadena_produc + '\n'
    print("Producciones: ")
    print(cadena_produc)


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


def imprimir_documento_afd(afd_gramatica):
    archivo_salida = open("C:/Users/solis/OneDrive/Escritorio/Salidas/" + automata.nombre + ".pdf", "w+")
    archivo_salida.write("      AFD" + '\n')
    archivo_salida.write("Nombre del Automata: " + automata.nombre + '\n')
    for alf in automata.alfabeto:
        archivo_salida.write("     - Simbolo de alfabeto: " + alf + '\n')
    for esta in automata.estados:
        archivo_salida.write("     - Estado: " + esta.nombre + '\n')
    archivo_salida.write("     - Estado inicial: " + automata.estado_inicial + '\n')
    for acep in automata.estado_aceptacion:
        archivo_salida.write("     - Estado aceptacion: " + acep + '\n')
    cadena_transiciones = ""
    for est in automata.estados:
        for tran in est.lista_transiciones:
            cadena_transiciones = cadena_transiciones + est.nombre + "," + tran.estadoDestino + "," + tran.simbolo + ";" \
                                  + '\n'
    archivo_salida.write("     - Trancisiones: " + '\n')
    archivo_salida.write(cadena_transiciones + '\n')
    archivo_salida.write("Cadenas Evaluadas:" + '\n')
    for cad_ev in automata.cadenas_validadas:
        archivo_salida.write("      - " + cad_ev + ", Valida" + '\n')
    for cad_n in automata.cadenas_invalidadas:
        archivo_salida.write("      - " + cad_n + ", Invalida" + '\n')
    archivo_salida.write('\n')
    archivo_salida.write("      Gramatica" + '\n')
    for termi in afd_gramatica.listaTerminales:
        archivo_salida.write("Terminal: " + termi + '\n')
    for no_term in afd_gramatica.listaNoTerminales:
        archivo_salida.write("No Terminal: " + no_term.no_terminal + '\n')
    archivo_salida.write("No Terminal inicio: " + afd_gramatica.noTerminalInicial + '\n')
    archivo_salida.write("Producciones Gramatica:" + '\n')
    for nt in afd_gramatica.listaNoTerminales:
        cadena = nt.no_terminal + " -> "
        for pr in nt.listaProducciones:
            cadena = cadena + pr.produccion + " | "
        archivo_salida.write(cadena + '\n')
    archivo_salida.close()
