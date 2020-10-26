import os

import Menu_Convertir_G2_AP


def obtener_automata():
    os.system("cls")
    automata = input("Escriba el nombre de la gramatica que desea evaluar: ")
    for aut in Menu_Convertir_G2_AP.devolver_lista():
        if aut.nombre == automata:
            return aut
    return input("Este automata no existe, presione enter...")

def menu_principal():
    auto = obtener_automata()
    opcion = 0
    while opcion != 3:
        os.system("cls")
        print("----------Validar Cadena----------")
        print("1) Validar cadena")
        print("2) Generar reporte")
        print("3) Salir")
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                auto.repor = "PILA$ ENTRADA$ TRANSICION \n"
                cadena = input("Ingrese la cadena a evaluar: ")
                auto.hacer_trancision(cadena)
                try:
                    arbol = open("C:/Users/solis/OneDrive/Escritorio/Salidas/" + auto.nombre + "_arbol.dot", "w+")
                    arbol.write("graph " + auto.nombre + "{\n" + auto.arbol_cadena + "}")
                    arbol.close()
                    os.system("dot C:/Users/solis/OneDrive/Escritorio/Salidas/" + auto.nombre + "_arbol.dot" +
                              " -o C:/Users/solis/OneDrive/Escritorio/Salidas/" + auto.nombre + "_arbol.png -Tpng")
                except FileNotFoundError as e:
                    print("Archivo invalido")
            elif opcion == 2:
                try:
                    salida = open("C:/Users/solis/OneDrive/Escritorio/Salidas/" + auto.nombre + ".csv", "w+")
                    salida.write(auto.repor)
                    salida.close()
                except FileNotFoundError as e:
                    print("Archivo invalido")
            elif opcion == 3:
                break
            else:
                input("Opcion invalida, presione enter")
        except ValueError as e:
            input("Opcion invalida, presione enter")