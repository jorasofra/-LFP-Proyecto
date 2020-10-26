import os

import Menu_Crear_Gramatica
import Menu_Crear_AFD
import Menu_Evaluar_Cadenas
import Menu_Cargar_Archivo
import Menu_Reportes
import Menu_Gramatica_Tipo_2

opcion = 0

print("----------Universidad de San Carlos de Guatemala----------")
print("---------Lenguajes Formales y de Programacion A+----------")
print("--------------------Carnet: 2016-12344--------------------")
input("Presione cualquier tecla")

while opcion != 7:
    os.system("cls")
    print("---------------Menu Principal---------------")
    print("1) CREAR AFD")
    print("2) CREAR GRAMATICA")
    print("3) EVALUAR CADENAS")
    print("4) REPORTES")
    print("5) CARGAR ARCHIVO DE ENTRADA")
    print("6) GRAMATICAS DE TIPO 2 Y AUTOMATAS DE PILA")
    print("7) SALIR")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("")

    if opcion == 1:
        os.system("cls")
        Menu_Crear_AFD.menu_principal()
    elif opcion == 2:
        os.system("cls")
        Menu_Crear_Gramatica.menu_principal()
    elif opcion == 3:
        os.system("cls")
        Menu_Evaluar_Cadenas.menu_principal()
    elif opcion == 4:
        Menu_Reportes.menu_principal()
    elif opcion == 5:
        Menu_Cargar_Archivo.menu_principal()
    elif opcion == 6:
        Menu_Gramatica_Tipo_2.menu_principal()
    elif opcion == 7:
        break
    else:
        print("Opción invalida, vuelva a ingresar")