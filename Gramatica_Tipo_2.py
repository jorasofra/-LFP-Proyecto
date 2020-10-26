import No_Terminal


class Gramatica_Tipo_2:
    def __init__(self, nombre):
        self.nombre = nombre
        self.no_terminales = []
        self.terminales = []
        self.producciones = []
        self.no_terminal_inicial = ""

    #Verifica que la lista de terminales este vacia
    @property
    def lista_terminales_vacia(self):
        if len(self.terminales) == 0:
            print("La lista de terminales esta vacia")
            return True
        return False

    #Verifica que la lista de no terminales este vacia
    @property
    def lista_no_terminales_vacia(self):
        if len(self.no_terminales) == 0:
            print("La lista de no terminales esta vacia")
            return True
        return False

    #Retorna el terminal en caso exista
    def buscar_terminal(self, termin):
        if not self.lista_terminales_vacia:
            for ter in self.terminales:
                if ter == termin:
                    return ter
        return None

    #Retorna el no terminal en caso exista
    def buscar_no_terminal(self, notermi):
        if not self.lista_no_terminales_vacia:
            for noter in self.no_terminales:
                if noter.no_terminal == notermi:
                    return noter
        return None

    #Agrega el terminal que se manda
    def agregar_terminal(self, terminal):
        if (self.buscar_terminal(terminal) is None) and (self.buscar_no_terminal(terminal) is None):
            self.terminales.append(terminal)
        else:
            input("Este terminal ya esta ingresado, presione Enter")

    #Agrega el no terminal que se manda
    def agregar_no_terminal(self, no_term):
        if (self.buscar_no_terminal(no_term) is None) and (self.buscar_terminal(no_term) is None):
            nuevo_no_terminal = No_Terminal.No_Terminal(no_term)
            self.no_terminales.append(nuevo_no_terminal)
        else:
            input("Este no terminal ya esta ingresado, presione Enter")

    #Busca el no terminal y si existe lo define coomo inicio
    def determinar_no_terminal_inicial(self, no_term):
        nt = self.buscar_no_terminal(no_term)
        if nt is not None:
            self.no_terminal_inicial = nt.no_terminal
        else:
            input("Ingrese un no terminal existente, presione enter")

    #Busca el no terminal y si existe define su produccion
    def definir_produccion(self, no_term, produccion):
        nt = self.buscar_no_terminal(no_term)
        if nt is not None:
            nt.agregar_produccion(produccion)
        else:
            input("Este no terminal no existe, presione enter")

    #Busca el no terminal y si existe borra la produccion
    def borrar_produccion(self, no_term, produccion):
        nt = self.buscar_no_terminal(no_term)
        if nt is not None:
            nt.borrar_produccion(produccion)
        else:
            input("Este no terminal no existe, presione enter")
