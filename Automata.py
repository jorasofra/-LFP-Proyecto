import Estado
import os

class Automata:

    def __init__(self, nombre):
        self.nombre = nombre
        self.alfabeto = []
        self.estados = []
        self.estado_inicial = ""
        self.estado_aceptacion = []
        self.cadenas_validadas = []
        self.cadenas_invalidadas = []

    ##En estos 3 se verifica si las listas estan vacias
    @property
    def alfabeto_vacio(self):
        if len(self.alfabeto) == 0:
            return True
        False

    @property
    def estados_vacio(self):
        if len(self.estados) == 0:
            return True
        return False

    def aceptacion_vacio(self):
        if len(self.estado_aceptacion) == 0:
            return True
        return False

    ##En estos se hacen las operaciones pertinentes para el momento de agregar algun objeto, o simbolo
    def agregar_simbolo_alfabeto(self, simbolo):
        if self.alfabeto_vacio and self.estados_vacio:
            self.alfabeto.append(simbolo)
        else:
            for x in self.alfabeto:
                if x == simbolo:
                    print("Este simbolo ya esta ingresado en el alfabeto")
                    input("Presione enter")
                    os.system("cls")
                    return
            for y in self.estados:
                if y.nombre == simbolo:
                    print("Este simbolo ya esta ingresado como estado")
                    input("Presione enter")
                    os.system("cls")
                    return
            self.alfabeto.append(simbolo)

    def agregar_estado(self, nombre):
        if self.alfabeto_vacio and self.estados_vacio:
            nuevo_estado = Estado.Estado(nombre)
            self.estados.append(nuevo_estado)
        else:
            for x in self.alfabeto:
                if x == nombre:
                    print("Este estado ya esta ingresado como parte del alfabeto")
                    input("Presione enter")
                    os.system("cls")
                    return
            for y in self.estados:
                if y.nombre == nombre:
                    print("Este estado es repetido")
                    input("Presione enter")
                    os.system("cls")
                    return
            nuevo_estado = Estado.Estado(nombre)
            self.estados.append(nuevo_estado)

    def definir_estado_inicial(self, nombre):
        if self.estados_vacio:
            print("La lista de estados esta vacia")
        else:
            for x in self.estados:
                if x.nombre == nombre:
                    self.estado_inicial = x.nombre
                    return
            print("Este estado no existe, ingrese uno que este en la lista de estados")

    def definir_estado_aceptacion(self, nombre):
        if self.estados_vacio:
            print("La lista de estados esta vacia")
        else:
            if self.aceptacion_vacio():
                for x in self.estados:
                    if x.nombre == nombre:
                        self.estado_aceptacion.append(x.nombre)
                        return
                print("Este estado no existe, ingrese uno que este en la lista de estados")
            else:
                for x in self.estado_aceptacion:
                    if x == nombre:
                        print("Este estado ya esta definido como estado de aceptacion")
                        return
                for x in self.estados:
                    if x.nombre == nombre:
                        self.estado_aceptacion.append(x.nombre)
                        return
                print("Este estado no existe, ingrese uno que este en la lista de estados")

    def verificar_estado_salida_para_transicion(self, estado_salida):
        if self.estados_vacio:
            print("La lista de estados esta vacia")
        else:
            for x in self.estados:
                if x.nombre == estado_salida:
                    return True
            print("El estado de salida no existe")
            return False

    def verificar_estado_llegada_para_transicion(self, estado_llegada):
        if self.estados_vacio:
            print("La lista de estados esta vacia")
        else:
            for x in self.estados:
                if x.nombre == estado_llegada:
                    return True
            print("El estado de llegada no existe")
            return False

    def verificar_simbolo_para_transicion(self, simbolo):
        if self.alfabeto_vacio:
            print("La lista del alfabeto esta vacia")
        else:
            for aux in self.alfabeto:
                if aux == simbolo:
                    return True
            print("El simbolo con el que se hara la transicion no existe en el alfabeto")
            return False

    def definir_transicion(self, estado_salida, estado_destino, simbolo):
        if self.verificar_estado_salida_para_transicion(estado_salida) and self.verificar_simbolo_para_transicion(
            simbolo) \
                and self.verificar_estado_llegada_para_transicion(estado_destino):
            for x in self.estados:
                if x.nombre == estado_salida:
                    x.agregar_transicion(estado_destino, simbolo)

    def evaluar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        if len(cadena) == 0:
            print("Debe ingresar una cadena con al menos 1 simbolo")
        else:
            for letra in cadena:
                index = 0
                while index < len(self.estados):
                    if self.estados[index].nombre == estado_actual:
                        index1 = 0
                        while index1 < len(self.estados[index].lista_transiciones):
                            if self.estados[index].lista_transiciones[index1].simbolo == letra:
                                estado_actual = self.estados[index].lista_transiciones[index1].estadoDestino
                                break
                            index1 += 1
                            if index1 == len(self.estados[index].lista_transiciones):
                                input("Cadena invalida; presione enter")
                                self.cadenas_invalidadas.append(cadena)
                                return
                        break
                    index += 1
                    if index == len(self.estados):
                        input("Cadena invalida; presione enter")
                        self.cadenas_invalidadas.append(cadena)
                        return
            for ace in self.estado_aceptacion:
                if ace == estado_actual:
                    input("Cadena valida; presione enter")
                    self.cadenas_validadas.append(cadena)
                    return
            input("Cadena invalida; presione enter")
            self.cadenas_invalidadas.append(cadena)

    def ruta_Cadena(self, cadena):
        if len(cadena) == 0:
            print("Debe ingresar una cadena con al menos 1 simbolo")
        else:
            estado_actual = self.estado_inicial
            cadena_ruta = "Ruta en AFD "
            for letra in cadena:
                index = 0
                while index < len(self.estados):
                    if self.estados[index].nombre == estado_actual:
                        index1 = 0
                        while index1 < len(self.estados[index].lista_transiciones):
                            if self.estados[index].lista_transiciones[index1].simbolo == letra:
                                cadena_ruta = cadena_ruta + estado_actual + ","
                                estado_actual = self.estados[index].lista_transiciones[index1].estadoDestino
                                cadena_ruta = cadena_ruta + estado_actual + "," + letra + ";"
                                break
                            index1 += 1
                            if index1 == len(self.estados[index].lista_transiciones):
                                input("Cadena invalida; presione enter")
                                self.cadenas_invalidadas.append(cadena)
                                return
                        break
                    index += 1
                    if index == len(self.estados):
                        input("Cadena invalida; presione enter")
                        self.cadenas_invalidadas.append(cadena)
                        return
            for ace in self.estado_aceptacion:
                if ace == estado_actual:
                    cadena_ruta = cadena_ruta + " Valida"
                    print(cadena_ruta)
                    self.cadenas_validadas.append(cadena)
                    input("Presione enter")
                    return
            input("Cadena invalida; presione enter")
            self.cadenas_invalidadas.append(cadena)
