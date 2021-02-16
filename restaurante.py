from abc import ABC


class Menu_Item(ABC):
    def __init__(self, nombre: str, precio: float, ingredientes: list, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ingredientes = ingredientes

    def preparar(self) -> bool:
        print(f"Preparando un delicioso {self.nombre}")
        return True

    def imprimir_descripcion(self) -> str:
        return f'{self.nombre}: {self.descripcion}'


class Mesa():
    def __init__(self):
        self.total = 0.0
        self.lista_platillos = []

    def agregar_platillo(self, platillo):
        self.lista_platillos.append(platillo)

    def cancelar_platillo(self, platillo):
        self.lista_platillos.remove(platillo)

    def imprimir_platillos(self) -> str:
        a = ""
        for x in self.lista_platillos:
            a = a + x.imprimir_descripcion() + "\n"
        return a

    def calcular_total(self) -> float:
        self.total = 0.0
        for x in self.lista_platillos:
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


cocacola = Bebida('Coca-cola', 15.00,
                  "Refrescante bebida efervescente", "Azucar, agua. colorante...")
print(cocacola.preparar())

pizza_margarita = Platillo('Pizza margarita', 150.00,
                           "Pizza margarita", "queso, salsa, albahacar")
print(pizza_margarita.preparar())
