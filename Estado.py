import Transicion


class Estado:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_transiciones = []

    @property
    def transion_esta_vacia(self):
        if len(self.lista_transiciones) == 0:
            return True
        return False

    def agregar_transicion(self, estado_destino, simbolo):
        if self.transion_esta_vacia:
            global transicion
            transicion = Transicion.Transicion(estado_destino, simbolo)
            self.lista_transiciones.append(transicion)
        else:
            if self.verificar_transicion_repetida(simbolo):
                transicion = Transicion.Transicion(estado_destino, simbolo)
                self.lista_transiciones.append(transicion)

    def verificar_transicion_repetida(self, simbolo):
        for x in self.lista_transiciones:
            if x.simbolo == simbolo:
                print("Error, esta haciendo una transicion con simbolo repetido")
                return False
            elif simbolo == "epsilon":
                print("Error, no es posible hacer transiciones con epsilon")
        return True
