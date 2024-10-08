""" Ejercicio 1: Implementación de TADs
Enunciado
En este universo, cada entrenador tiene un equipo Pokémon. Para este ejercicio deberá implementar dos clases en Python: Pokemon y Entrenador.

Clases a Implementar
Clase Pokemon:
Atributos:
nombre: (str) Nombre del Pokémon.
tipo: (str) Tipo del Pokémon (por ejemplo, Agua, Fuego, Planta).
nivel: (int) Nivel del Pokémon (debe estar entre 1 y 100).
Métodos:
__init__(): Constructor que inicializa los atributos del Pokémon.
subir_nivel(): Método que incrementa el nivel del Pokémon en 1, siempre y cuando no supere el nivel 100.
__str__(): Método que devuelve una representación en cadena del Pokémon en el formato:

Clase Entrenador:
Atributos:
nombre: (str) Nombre del entrenador.
equipo: (lista) Lista que contiene instancias de la clase Pokemon.
Métodos:
__init__(): Constructor que inicializa el nombre del entrenador y crea una lista vacía para el equipo.
agregar_pokemon(): Método que agrega un Pokémon al equipo. Si ya hay 6 Pokémon en el equipo, debe mostrar un mensaje indicando que no se pueden tener más Pokémon.
mostrar_equipo(): Método que imprime todos los Pokémon del equipo utilizando el método __str__ de la clase Pokemon.
nivel_promedio(): Método que calcula y devuelve el nivel promedio de los Pokémon en el equipo. Si no hay Pokémon en el equipo, debe devolver 0. """


class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        try:
            if self.nivel < 100:
                self.nivel += 1
        except ValueError:
            print("El nivel debe estar entre 1 y 100")

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Nivel {self.nivel}"

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else:
            print("No se pueden tener más de 6 Pokémon en el equipo.")

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)

    def nivel_promedio(self):
        if len(self.equipo) == 0:
            return 0
        else:
            suma_niveles = 0
            for pokemon in self.equipo:
                suma_niveles += pokemon.nivel
            return suma_niveles / len(self.equipo)