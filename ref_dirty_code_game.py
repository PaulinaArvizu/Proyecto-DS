# ---------------------------------------------------------------------------------------------
# * Equipo: N
# Nombre de los integrantes del equipo
# - Paulina Arvizu
# - Hector Silva
# - Anahi Santana
# - Guillermo Hernandez
# ---------------------------------------------------------------------------------------------

from __future__ import annotations
from abc import ABC
from time import sleep

class Personaje:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.mochilas = None
        self.vida = 100
    
    def comer(self, alimento:Alimento):
        '''
        El personaje consume los alimentos para ganar vida
        '''
        self.vida += alimento.aporte_vida

class Alimento(ABC):
    def __init__(self, nombre, tiempo_coccion):
        self.nombre = nombre
        self.tiempo_coccion = tiempo_coccion
        self.cocido = False
    def tiempo_coccion(self):
        return self.tiempo_coccion

class Mochila:
    '''
    La mochila tiene la capacidad de guardar un número limitado de artículos
    '''
    ESPACIADO_IMPRIMIR  = 40
    
    def __init__(self, nombre, max_items:int=5):
        self.nombre = nombre
        self._max_items = max_items
        self.items = []
        self.tipo_hacha = ''
        self.tipo_martillo = ''
    # ---------------------------------------------------------------------------------------------
    # * RETO
    # Encargado: Hector
    # ---------------------------------------------------------------------------------------------
    # Objetivo: recoger colecciones de objetos a la mochila. Los objetos se pueden agrupar. No hace
    # falta conocer el numero de objetos. Actualmente solo es posible incluir los nombres de los
    # articulos.
    # 
    # Por ejemplo:
    #  - palitos x 5
    #  - rocas x 4
    #
    def recoger(self, nombre:str) -> bool:
        '''
        Ingresa articulos en la mochila
        '''
        if self.has_capacity():
            if len(self.items) < 1:
                self.items.append([nombre, 1])
                return True
            else:
                for x in self.items:
                    if x[0] == nombre:
                        x[1] += 1
                        return True
                #No lo encuentra en la mochila y genera uno nueva
                self.items.append([nombre, 1])
                return True
        else:
            raise ValueError(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')
    
    def has_capacity(self) -> bool:
        cuenta = 0;
        for x in self.items:
            cuenta += x[1]
        return cuenta < self._max_items
    # ---------------------------------------------------------------------------------------------
    # * RETO -  Replace type code with state/strategy
    # Encargado: Anahi
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Poder guardar herramientas dentro de la mochila, pero una version de la herramienta
    # a la vez. Por ejemplo, no se puede tener un Hacha normal y un Hacha de lujo en la misma mochila.
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO - Consolidate Conditional Expresion
    # Encargado: Guillermo
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Consolidad las expresiones en las condicionales
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO - Consolidate Conditional Expresion
    # Encargado: Gillermo
    # ---------------------------------------------------------------------------------------------
    # La lógica de las condicionales parece algo compleja 
    # Objetivo: Crear métodos para el manero de las expresiones en las condicionales
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO
    # Encargado: Paulina
    # ---------------------------------------------------------------------------------------------
    # Existe código que se repite constantemente
    # Objetivo: Evitar duplicidad de código en cada una de las ramas de las condicionales
    #
    def fabricar(self, herramienta) -> bool:
        '''
        Fabricar herramientas a través de los artículos en tu inventario. Regresa True si se pudo
        fabricar la herramienta
        '''
        if herramienta == 'martillo' and self.es_fabricable('martillo'):
            self.tipo_martillo = Martillo()
            self.quitar_item('ramita', 3)
            self.quitar_item('roca', 3)
            self.quitar_item('cuerda', 2)
            return True

        if herramienta == 'hacha' and self.es_fabricable('hacha'):
            self.tipo_hacha = Hacha()
            self.quitar_item('ramita', 1)
            self.quitar_item('pedernal', 1)
            return True

        if herramienta == 'hacha_lujo' and self.es_fabricable('hacha_lujo'):
            self.tipo_hacha = HachaLujo()
            self.quitar_item('ramita', 4)
            self.quitar_item('pepita oro', 2)
            return True
        else:
            return False
    

    def quitar_item(self, item, cantidad):
         for x in self.items:
            if x[0] == item:
                x[1] -= cantidad
                if x[1] == 0:
                    self.items.remove(x)


    def contar_item(self, item):
        for x in self.items:
            if x[0] == item:
                return x[1]
        return 0

    def es_fabricable(self, herramienta) -> bool:
        if herramienta == 'martillo':
            return self.contar_item('ramita') >= 3 and self.contar_item('roca') >= 3 and self.contar_item('cuerda') >= 2
        if herramienta == 'hacha':
            return self.contar_item('ramita') >= 1 and self.contar_item('pedernal') >= 1
        if herramienta == 'hacha_lujo':
            return self.contar_item('ramita') >= 4 and self.contar_item('pepita oro') >= 2
        return False


    
    # ---------------------------------------------------------------------------------------------
    # * RETO - Replace magic number with symbolic constant
    # Encargado: Anahi
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Reemplazar los números con variables de clase.
    # Se puede aplicar a todo el código, no solamente a este dunder method.
    #
    def __str__(self) -> str:
        
        mochila_str=  f'''{self.nombre:^{self.ESPACIADO_IMPRIMIR}} \n{"="*self.ESPACIADO_IMPRIMIR}\n'''
        herramientas = f'''-Herramientas:\n   {self.tipo_hacha}\n   {self.tipo_martillo}'''
        materiales = '-Materiales:\n'

        for i in self.items:
            materiales += '   ' + i[0] + ' x' + str(i[1]) + '\n'
            
        return  mochila_str + materiales + herramientas

# ---------------------------------------------------------------------------------------------
# * RETO
# Encargado: Hector
# ---------------------------------------------------------------------------------------------
# Objetivo: Agrega el metodo "demoler" con un "assert" el cual suponga que se tiene al menos
# 1 de durabilidad antes de ejecutar la acción.
#
class Martillo:
    '''
    El martillo es una herramienta que se puede utilizar para demoler estructuras.
    El martillo requiere 3 rocas, 3 ramitas y 2 cuerdas para que se pueda fabricar.
    La durabilidad es el número de usos.
    '''
    def __init__(self, durabilidad:int=75, daño=17):
        self.durabilidad = durabilidad
        self.daño = daño

    def __str__(self) -> str:
        return 'Martillo'
    
    def demoler(self) -> bool:
        assert self.durabilidad >= 1, "El martillo no tiene suficiente durabilidad" #assert hace una condicional, si no se cumple regresa un Asserition error
        self.durabilidad = self.durabilidad-1
        return True
        
class TipoHacha(ABC):
    def __init__(self, durabilidad, daño):
        self.durabilidad = durabilidad
        self.daño = daño
    
    def __str__(self) -> str:
        return 'Hacha'

class Hacha(TipoHacha):
    '''
    El hacha es una herramienta que se puede utilizar para talar árboles. Se puede crear
    al comienzo del juego con 1 ramita y 1 pedernal.
    '''
    def __init__(self, durabilidad:int=100, daño=27):
        self.durabilidad = durabilidad
        self.daño = daño
    
    def __str__(self) -> str:
        return 'Hacha normal'

class HachaLujo(TipoHacha):
    '''
    El Hacha de lujo es una versión del Hacha normal que tiene cuatro veces más durabilidad
    y requiere pepitas de oro en lugar de pedernal. Se necesitan 4 ramitas y 2 pepitas de oro
    para fabricar.
    '''
    def __init__(self, durabilidad:int=400, daño=27):
        self.durabilidad = durabilidad
        self.daño = daño
        
    def __str__(self) -> str:
        return 'Hacha de Lujo'

class Fogata:
    '''
    Una fogata es la clave para la supervivencia básica en el mundo. Aporta luz, calor y permite
    cocinar los alimentos. Requiere 3 césped y 2 troncos para que se pueda fabricar.
    Los personajes no pueden consumir alimentos crudos.
    '''

    def __init__(self):
        # Agrega la validación necesaria antes de fabricar una fogata
        pass

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # Encargado: Paulina
    # ---------------------------------------------------------------------------------------------
    # Los alimentos tienen diferentes tiempos de cocción. No queremos tener condicionales, entonces
    # usamos refactorización. Se ha comentado parte del código original.
    # Objetivo: Usar polimorfismo para obtener el tiempo de cocción y simplificar el método. Trata de
    # usar una interface con al menos los atributos: nombre, tiempo_coccion, cocido

    def cocinar(self, alimento:object) -> None:
        '''
        Permite cocinar un alimento crudo en la fogata. Regresa el mismo alimento pero cocinado.
        '''
        # if alimento == 'cordero' and alimento.cocido == False:
        #     sleep(2)
        # elif alimento == 'beef' and alimento.cocido == False:
        #     sleep(5)

        if alimento.cocido == False:
            print(f'cocinando {alimento.nombre}')
            sleep(alimento.tiempo_coccion)
            alimento.cocido = True
            print(f'{alimento.nombre} cocido')

if __name__ == '__main__':
    # Personajes
    wilson = Personaje('Wilson')

    # Items
    backpack = Mochila('Morral chico', 10)
    backpack.recoger('ramita')
    backpack.recoger('ramita')
    backpack.recoger('ramita')
    backpack.recoger('roca')
    backpack.recoger('roca')
    backpack.recoger('roca')
    backpack.recoger('cuerda')
    backpack.recoger('cuerda')
    backpack.recoger('cuerda')
    print(backpack)

    # Fabrica
    backpack.fabricar('martillo')

    #Items 
    backpack.recoger('ramita')
    backpack.recoger('pedernal')
    print(backpack)
    #Fabrica
    backpack.fabricar('hacha')
    print(backpack)

    #Items 
    backpack.recoger('ramita')
    backpack.recoger('ramita')
    backpack.recoger('ramita')
    backpack.recoger('ramita')
    backpack.recoger('pepita oro')
    backpack.recoger('pepita oro')
    print(backpack)

    backpack.fabricar('hacha_lujo')

    print(backpack)

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # Encargado: Anahi
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Agregar al menos dos alimentos que se puedan cocinar en la fogata. Crear una fogata,
    # Cocinar los alimentos en la fogata y comer los alimentos.
    # 
    malvavisco = Alimento('malvavisco', 2)
    beef = Alimento('beef', 5)
    hoguera = Fogata()
    hoguera.cocinar(malvavisco)
    hoguera.cocinar(beef)
    # Listamos los articulos en nuestra mochila
    print(backpack)