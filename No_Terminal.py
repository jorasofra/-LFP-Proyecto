import Produccion


class No_Terminal:
    def __init__(self, no_terminal):
        self.no_terminal = no_terminal
        self.listaProducciones = []

    @property
    def lista_producciones_vacia(self):
        if len(self.listaProducciones) == 0:
            return True
        return False

    def verificar_produccion_repetida(self, produccion):
        for x in self.listaProducciones:
            if x == produccion:
                print("Error, esta produccion ya existe")
                return False
        return True

    def agregar_produccion(self, produccion):
        if self.lista_producciones_vacia:
            global nueva_produccion
            nueva_produccion = Produccion.Produccion(produccion)
            self.listaProducciones.append(nueva_produccion)
        else:
            if self.verificar_produccion_repetida(produccion):
                nueva_produccion = Produccion.Produccion(produccion)
                self.listaProducciones.append(nueva_produccion)

    def borrar_produccion(self, produccion):
        if self.lista_producciones_vacia:
            input("No hay producciones que borrar")
        else:
            index = 0
            while index < len(self.listaProducciones):
                if self.listaProducciones[index].produccion == produccion:
                    self.listaProducciones.pop(index)
                    return
                index += 1
            input("Esta produccion no existe, presione enter")