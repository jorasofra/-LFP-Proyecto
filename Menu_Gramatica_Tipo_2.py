import os

import Menu_Crear_Gramatica_Tipo_2
import Menu_Convertir_G2_AP
import Menu_Validar_Cadena_AP


def menu_principal():
    opcion = 0
    while opcion != 4:
        os.system("cls")
        print("----------Menu Principal----------")
        print("1) INGRESAR/MODIFICAR GRAMTICA")
        print("2) GENERAR AUTOMATA DE PILA")
        print("3) VALIDAR CADENA")
        print("4) SALIR")
        try:
            opcion = int(input("Seleccione la accion a realizar: "))
            if opcion == 1:
                Menu_Crear_Gramatica_Tipo_2.menu_principal()
            elif opcion == 2:
                Menu_Convertir_G2_AP.menu_principal()
            elif opcion == 3:
                Menu_Validar_Cadena_AP.menu_principal()
            elif opcion == 4:
                break
            else:
                input("Opcion incorrecta, presione enter")
        except ValueError as e:
            input("Solo se permite numeros, presione enter")
