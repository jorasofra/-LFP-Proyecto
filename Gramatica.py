import os
import No_Terminal


class Gramatica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaTerminales = []
        self.listaNoTerminales = []
        self.noTerminalInicial = ""
        self.cadenas_validadas = []
        self.cadenas_invalidadas = []

    ## Verifica si la lista de terminales esta vacia
    @property
    def lista_terminales_vacia(self):
        if len(self.listaTerminales) == 0:
            return True
        return False

    ## Verifica si la lista de No Terminales esta vacia
    @property
    def lista_no_terminales_vacia(self):
        if len(self.listaNoTerminales) == 0:
            return True
        return False

    def agregar_terminales(self, terminal):
        if self.lista_terminales_vacia and self.lista_no_terminales_vacia:
            self.listaTerminales.append(terminal)
        else:
            for x in self.listaTerminales:
                if x == terminal:
                    print("Este terminal ya esta ingresado en los terminales")
                    input("Presione enter")
                    os.system("cls")
                    return
            for y in self.listaNoTerminales:
                if y.no_terminal == terminal:
                    print("Este terminal ya esta ingresado como no terminal")
                    input("Presione enter")
                    os.system("cls")
                    return
            self.listaTerminales.append(terminal)

    def agregar_no_terminales(self, nombre_no_terminal):
        if self.lista_no_terminales_vacia and self.lista_terminales_vacia:
            nuevo_no_terminal = No_Terminal.No_Terminal(nombre_no_terminal)
            self.listaNoTerminales.append(nuevo_no_terminal)
        else:
            for x in self.listaTerminales:
                if x == nombre_no_terminal:
                    print("Este no terminal ya esta ingresado como terminal")
                    input("Presione enter")
                    os.system("cls")
                    return
            for y in self.listaNoTerminales:
                if y.no_terminal == nombre_no_terminal:
                    print("Este no terminal es repetido")
                    input("Presione enter")
                    os.system("cls")
                    return
            new_no_terminal = No_Terminal.No_Terminal(nombre_no_terminal)
            self.listaNoTerminales.append(new_no_terminal)

    def determinar_no_terminal_inicial(self, no_terminal):
        if self.lista_no_terminales_vacia:
            print("La lista de no terminales esta vacia")
        else:
            for x in self.listaNoTerminales:
                if x.no_terminal == no_terminal:
                    self.noTerminalInicial = x.no_terminal
                    return
            print("Este No Terminal no existe, ingrese uno que este en la lista de No Terminales")

    def verificar_no_terminal_salida(self, no_terminal):
        if self.lista_no_terminales_vacia:
            print("La lista de no terminales esta vacia")
        else:
            for aux in self.listaNoTerminales:
                if aux.no_terminal == no_terminal:
                    return True
            print("El no terminal no existe")
            return False

    def definir_produccion(self, no_terminal, produccion):
        if self.verificar_no_terminal_salida(no_terminal):
            for aux in self.listaNoTerminales:
                if aux.no_terminal == no_terminal:
                    aux.agregar_produccion(produccion)

    def evaluar_cadena(self, cadena):
        no_termina_actual = self.noTerminalInicial
        if len(cadena) == 0:
            print("Debe ingresar una cadena con al menos 1 simbolo")
        else:
            for letra in cadena:
                index = 0
                while index < len(self.listaNoTerminales):
                    if self.listaNoTerminales[index].no_terminal == no_termina_actual:
                        index1 = 0
                        while index1 < len(self.listaNoTerminales[index].listaProducciones):
                            transition = self.listaNoTerminales[index].listaProducciones[index1].produccion.split(" ")
                            if transition[0] == letra:
                                no_termina_actual = transition[1]
                                break
                            index1 += 1
                            if index1 == len(self.listaNoTerminales[index].listaProducciones):
                                input("Cadena invalida, presione enter")
                                return
                        break
                    index += 1
                    if index == len(self.listaNoTerminales):
                        input("Cadena invalida, presione enter")
                        return
            for ace in self.listaNoTerminales:
                if no_termina_actual == ace.no_terminal:
                    for ace2 in ace.listaProducciones:
                        if ace2.produccion == "epsilon":
                            input("Cadena valida, presione enter")
                            return
            input("Cadena invalida, presione enter")

    def expansion(self, cadena):
        if len(cadena) == 0:
            print("Debe ingresar una cadena con al menos 1 simbolo")
        else:
            no_termina_actual = self.noTerminalInicial
            expa = "Expansion en gramatica " + no_termina_actual
            cade = ""
            for letra in cadena:
                index = 0
                while index < len(self.listaNoTerminales):
                    if self.listaNoTerminales[index].no_terminal == no_termina_actual:
                        index1 = 0
                        while index1 < len(self.listaNoTerminales[index].listaProducciones):
                            transition = self.listaNoTerminales[index].listaProducciones[index1].produccion.split(" ")
                            if transition[0] == letra:
                                cade = cade + letra
                                expa = expa + " -> " + cade
                                no_termina_actual = transition[1]
                                expa = expa + no_termina_actual
                                break
                            index1 += 1
                            if index1 == len(self.listaNoTerminales[index].listaProducciones):
                                input("Cadena invalida, presione enter")
                                return
                        break
                    index += 1
                    if index == len(self.listaNoTerminales):
                        input("Cadena invalida, presione enter")
                        return
            for ace in self.listaNoTerminales:
                if no_termina_actual == ace.no_terminal:
                    for ace2 in ace.listaProducciones:
                        if ace2.produccion == "epsilon":
                            expa = expa + " Valida"
                            print(expa)
                            self.cadenas_validadas.append(cadena)
                            input("Presione enter")
                            return
            input("Cadena invalida, presione enter")
