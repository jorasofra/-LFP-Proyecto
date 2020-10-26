import Transicion_AP
import Estado_AP

class Automata_Pila:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estados = []
        self.alfabeto_maquina = ["epsilon"]
        self.simbolos_pila = ["epsilon", "#"]
        self.estado_inicial = "Io"
        self.estado_aceptacion = "f"
        self.pila = ["epsilon"]
        self.repor = "PILA$ ENTRADA$ TRANSICION \n"
        self.arbol_cadena = ""

    @property
    def lista_alfabeto_maquina_vacia(self):
        if len(self.alfabeto_maquina) == 0:
            print("La lista de estados esta vacia")
            return True
        return False

    # Busca y retorna el estado
    def buscar_estado(self, est):
        for e in self.estados:
            if e.nombre == est:
                return e
        return None

    # Busca y retorna el simbolo del alfabeto
    def buscar_alfabeto_maquina(self, alf):
        if not self.lista_alfabeto_maquina_vacia:
            for al in self.alfabeto_maquina:
                if al == alf:
                    return al
        return None

    # Busca y retorna el simbolo de pila
    def buscar_simbolo_pila(self, sim):
        for s in self.simbolos_pila:
            if s == sim:
                return s
        return None

    # Busca si existe el simbolo en el alfabeto de maquina y si no existe lo agrega
    def agregar_alfabeto_maquina(self, alf):
        if self.buscar_alfabeto_maquina(alf) is None:
            self.alfabeto_maquina.append(alf)
        else:
            input("Este simbolo ya existe en el alfabeto de maquina, presione enter")

    # Busca si existe el simbolo de pila y si no existe lo agrega
    def agregar_simbolo_pila(self, sim):
        if self.buscar_simbolo_pila(sim) is None:
            self.simbolos_pila.append(sim)
        else:
            input("Este simbolo ya existe, presione enter")

    # Busca si el estado no existe y lo agrega
    def agregar_estado(self, nombre):
        nuevo_es = Estado_AP.Estado_AP(nombre)
        self.estados.append(nuevo_es)

    # Agrega una nueva transicion
    def agregar_transicion(self, est_sal, lec, top_pil, est_lleg, rees):
        # No olvidar los parentesis al final de la declaracion
        nueva_transicion = Transicion_AP.Transicion_AP()

        # Verifica que el simbolo de lectura exista en el alfabeto de maquina
        if self.buscar_alfabeto_maquina(lec) is not None:
            nueva_transicion.lectura = lec
        else:
            return input("Simbolo de lectura: " + lec + " no conocido")

        # Verifica que el simbolo del tope de pila exista en los simbolos de pila
        if self.buscar_simbolo_pila(top_pil) is not None:
            nueva_transicion.tope_pila = top_pil
        else:
            return input("Simbolo de pila: " + top_pil + " no existe")

        # Verifica que el estado de llegada exista
        if self.buscar_estado(est_lleg) is not None:
            nueva_transicion.estado_llegada = est_lleg
        else:
            return input("Este estado: " + est_lleg + " no existe, presione enter")

        # Separa la transicion enviada y la coloca en la pila de
        simbs = rees.split(" ")
        aux = 0
        try:
            pi_aux = []
            while aux < len(simbs):
                pi_aux.append(simbs[aux])
                aux += 1
            nueva_transicion.reescritura = pi_aux
            es = self.buscar_estado(est_sal)
            es.agregar_transicion(nueva_transicion)
        except IndexError as e:
            input("Fuera de indice, pila agregar")

    # Retorna el simbolo que esta en el tope de la pila
    def tope_pila(self):
        return self.pila[len(self.pila) - 1]

    def hacer_trancision(self, cadena):
        global estado_actual
        estado_actual = self.buscar_estado(self.estado_inicial)

        estado_actual = self.buscar_estado(self.transicion_tipo_0(cadena))
        estado_actual = self.buscar_estado(self.transicion_tipo_1(cadena))

        aux = 0
        while aux < len(cadena):
            au = aux
            c = ""
            while au < len(cadena):
                c = c + cadena[au]
                au += 1
            self.transicion_tipo_2(cadena[aux], c)
            aux += self.transicion_tipo_3(cadena[aux], c)

        estado_actual = self.transicion_tipo_4()

        if estado_actual.nombre == "f" and len(self.pila) == 0:
            input("Cadena Valida, presione enter")
            self.repor = self.repor + "----------$ ----------$ ACEPTACION"
            self.pila.append("epsilon")
        else:
            input("Cadena invalida, presion enter")

    def transicion_tipo_0(self, cadena):
        est_aux = self.buscar_estado(self.estado_inicial)
        self.cadena_reporte(cadena, est_aux.nombre, est_aux.transiciones[0].lectura, est_aux.transiciones[0].tope_pila,
                            est_aux.transiciones[0].estado_llegada, est_aux.transiciones[0].reescritura)
        self.pila.pop()
        self.pila.append(est_aux.transiciones[0].reescritura[0])
        return est_aux.transiciones[0].estado_llegada

    def transicion_tipo_1(self, cadena):
        est_aux = self.buscar_estado(estado_actual.nombre)
        self.cadena_reporte(cadena, est_aux.nombre, est_aux.transiciones[0].lectura, est_aux.transiciones[0].tope_pila,
                            est_aux.transiciones[0].estado_llegada, est_aux.transiciones[0].reescritura)
        self.pila.append(est_aux.transiciones[0].reescritura[0])
        return est_aux.transiciones[0].estado_llegada

    def transicion_tipo_2(self, letra_actual, cadena):
        est_aux = self.buscar_estado(estado_actual.nombre)
        aux1 = 0
        for tr in est_aux.transiciones:
            if tr.tope_pila == self.tope_pila():
                if tr.reescritura[0] == letra_actual:
                    self.cadena_reporte(cadena, est_aux.nombre, tr.lectura, tr.tope_pila, tr.estado_llegada,
                                        tr.reescritura)
                    self.pila.pop()
                    aux = len(tr.reescritura) - 1
                    while aux >= 0:
                        self.pila.append(tr.reescritura[aux])
                        self.arbol_cadena = self.arbol_cadena + tr.tope_pila + "--" + tr.reescritura[aux] + "\n"
                        aux -= 1
                    return tr.estado_llegada
        return None


    def transicion_tipo_3(self, letra_actual, cadena):
        est_aux = self.buscar_estado(estado_actual.nombre)
        for tr in est_aux.transiciones:
            if (tr.tope_pila == self.tope_pila()) and (letra_actual == tr.lectura):
                self.cadena_reporte(cadena, est_aux.nombre, tr.lectura, tr.tope_pila, tr.estado_llegada,
                                    tr.reescritura)
                self.pila.pop()
                return 1
        return 0

    def transicion_tipo_4(self):
        est_aux = self.buscar_estado(estado_actual.nombre)
        if self.tope_pila() == "#":
            for tr in est_aux.transiciones:
                if tr.tope_pila == "#":
                    self.cadena_reporte("----------", est_aux.nombre, tr.lectura,
                                        tr.tope_pila, tr.estado_llegada, tr.reescritura)
            self.pila.pop()
            return self.buscar_estado("f")
        else:
            return None

    def cadena_reporte(self, cadena, salida, lectura, tope, llegada, reescritura):
        fila = ""
        aux = len(self.pila) - 1
        while aux >= 0:
            fila = fila + self.pila[aux]
            aux -= 1
        fila = fila + "$ " + cadena + "$ "
        fila = fila + "(" + salida + ", " + lectura + ", " + tope + "; " + llegada + ", "
        aux1 = 0
        while aux1 < len(reescritura):
            fila = fila + reescritura[aux1]
            aux1 += 1
        fila = fila + ")\n"

        self.repor = self.repor + fila