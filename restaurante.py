from abc import ABC, abstractmethod


class Menu_Item(ABC):
    def __init__(self, nombre: str, precio: float, ingredientes: list, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ingredientes = ingredientes

    @abstractmethod
    def preparar(self) -> bool:
        print(f"Preparando una deliciosa {self.nombre}")
        return True

    @abstractmethod
    def imprimir_descripcion(self) -> str:
        return f'{self.nombre}: {self.descripcion}'


class Mesa():
    def __init__(self):
        self.total = 0.0
        self.lista_ordenados = []

    def agregar_platillo(self, platillo):
        self.lista_ordenados.append(platillo)

    def cancelar_platillo(self, platillo):
        self.lista_ordenados.remove(platillo)

    def imprimir_platillos(self) -> str:
        a = ""
        for x in self.lista_ordenados:
            a = a + x.imprimir_descripcion() + "\n"
        return a

    def calcular_total(self) -> float:
        self.total = 0.0
        for x in self.lista_ordenados:
            self.total += x.precio
        return total


class Platillo(Menu_Item):
    def preparar(self) -> bool:
        print(f"Preparando un delicioso {self.nombre}")
        return True

    def imprimir_descripcion(self) -> str:
        return f'{self.nombre}: {self.descripcion}'


class Bebida(Menu_Item):
    def preparar(self) -> bool:
        print(f"Sirviendo un delicioso {self.nombre}")
        return True

    def imprimir_descripcion(self) -> str:
        return f'{self.nombre}: {self.descripcion}'


class Menu():
    def __init__(self):
        self.lista_bebidas = []
        self.lista_platillos = []

    def agregar_platillo(self, platillo: Platillo):
        self.lista_platillos.append(platillo)

    def agregar_bebida(self, bebida: Bebida):
        self.lista_bebidas.append(bebida)

    def eliminar_platillo(self, platillo: Platillo):
        if platillo in self.lista_platillos:
            self.lista_platillos.remove(platillo)

    def eliminar_bebida(self, bebida: Bebida):
        if bebida in self.lista_bebidas:
            self.lista_bebida.remove(bebida)

    def imprimir_menu(self) -> str:
        a = "Bebidas: \n"
        for x in self.lista_bebidas:
            a += "   " + x.imprimir_descripcion() + "\n"
        a += "Platillos: \n"
        for x in self.lista_platillos:
            a += "   " + x.imprimir_descripcion() + "\n"
        return a


if __name__ == "__main__":

    cocacola = Bebida('Coca-cola', 15.00,
                      "Coca-cola", "Refresco de cola")
    fanta = Bebida('Fanta', 15.00,
                   "Fanta", "Refresco de naranja")

    pizza_margarita = Platillo('Pizza margarita', 150.00,
                               "Pizza margarita", "queso, salsa, albahacar")
    pizza_peperoni = Platillo('Pizza peperoni', 160.00,
                              "Pizza de peperoni", "queso, salsa, peperoni")
    pizza_carnes_frias = Platillo('Pizza de carnes frias', 170.00,
                                  "Pizza de carnes frias", "queso, salsa, peperoni")

    print(pizza_margarita.preparar())
    print(cocacola.preparar())

    menu_pizzeria = Menu()
    menu_pizzeria.agregar_platillo(pizza_margarita)
    menu_pizzeria.agregar_platillo(pizza_peperoni)
    menu_pizzeria.agregar_platillo(pizza_carnes_frias)
    menu_pizzeria.agregar_bebida(cocacola)
    menu_pizzeria.agregar_bebida(fanta)

    print(menu_pizzeria.imprimir_menu())
