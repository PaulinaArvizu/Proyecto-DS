class Mesa():
    def __init__(self):
        self.total = 0.0
        self.lista_platillos = []
    def agregar_platillo(self, platillo):
        self.lista_platillos.append(platillo)
    def cancelar_platillo(self, platillo):
        self.lista_platillos.remove(platillo)
    def imprimir_platillos(self)->str:
        a = ""
        for x in self.lista_platillos:
            a = a + x.imprimir_descripcion() + "\n"
        return a;
    def calcular_total(self)->float:
        self.total= 0.0
        for x in self.lista_platillos:
            self.total += x.precio
        return total