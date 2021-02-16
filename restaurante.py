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
