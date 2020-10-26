class Estado_AP:
    def __init__(self, nombre):
        self.nombre = nombre
        self.transiciones = []

    def agregar_transicion(self, transic):
        self.transiciones.append(transic)
