""" Ejercicio 3: Sistema de Evoluciones de Pokémon
Enunciado
Cada Pokémon podría evolucionar a una forma más poderosa, para gestionarlas implementar un sistema utilizando una pila (stack), que permita llevar un registro de las evoluciones en orden inverso ya que la más reciente es la que se aplicará primero.

Contexto
La pila se utilizará para almacenar las evoluciones de un Pokémon. Cuando uno de ellos evoluciona, se agrega su nueva forma a la pila. Si el entrenador decide revertir la evolución se puede desapilar la forma más reciente.

Clases a Implementar
Clase Evolucion:
Atributos:
nombre: (str) Nombre del Pokémon en su forma evolucionada.
Métodos:
__init__(self, nombre: str): Constructor que inicializa el nombre de la evolución.

Clase PilaEvoluciones:
Atributos:
evoluciones: (lista) Lista enlazada que almacena las evoluciones en orden.
Métodos:
__init__(self): Constructor que inicializa la lista de evoluciones como vacía.
apilar(self, evolucion: Evolucion): Método que agrega una evolución a la pila.
desapilar(self): Método que elimina y devuelve la última evolución agregada a la pila. Si la pila está vacía, debe devolver un mensaje indicando que no hay evoluciones para desapilar.
mostrar_evoluciones(self): Método que imprime todas las evoluciones en el orden en que fueron apiladas. """


class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombre


class NodoEvoluciones:
    def __init__(self, evolucion):
        self.evolucion = evolucion
        self.sig = None


class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None

    def apilar(self, evolucion):
        nuevo = NodoEvoluciones(evolucion)
        nuevo.sig = self.evoluciones
        self.evoluciones = nuevo

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar."
        else:
            evolucion = self.evoluciones.evolucion
            self.evoluciones = self.evoluciones.sig
            return evolucion

    def mostrar_evoluciones(self):
        actual = self.evoluciones
        while actual is not None:
            print(actual.evolucion.nombre)
            actual = actual.sig