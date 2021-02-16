class Menu_Item:
    def __init__(self, nombre: str, precio: float, ingredientes: list, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        descripcion = descripcion
        self.ingredientes = ingredientes
    
    def preparar(self) -> bool:
        print(f"Preparando un delicioso {self.nombre}");
        return True
    
    def imprimir_descripcion(self) -> str:
        return f'{self.nombre}: {self.descripcion}'