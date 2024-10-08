""" Ejercicio 2: Recursividad en el Universo Pokémon
Enunciado
Los entrenadores a menudo se enfrentan a desafíos que requieren la búsqueda de Pokémones en un área. Para este ejercicio implementar una función recursiva que simula la búsqueda de un Pokémon específico en un árbol de Pokémones.

Contexto
Suponga que tiene un árbol binario donde cada nodo representa un Pokémon, cada nodo tiene un nombre y puede tener hasta dos hijos (uno a la izquierda y otro a la derecha). La búsqueda de un Pokémon específico se puede realizar de manera recursiva verificando si el Pokémon se encuentra en el nodo actual o en uno de sus subárboles.

Clases a Implementar
Clase PokemonNode:
Atributos:
nombre: (str) Nombre del Pokémon.
izquierda: (PokemonNode) Hijo izquierdo (puede ser None).
derecha: (PokemonNode) Hijo derecho (puede ser None).
Métodos:
__init__(self, nombre: str): Constructor que inicializa el nombre del Pokémon y establece los hijos izquierdo y derecho como None.

Función Recursiva buscar_pokemon:
Parámetros:
nodo: (PokemonNode) Nodo actual del árbol donde se realiza la búsqueda.
nombre_pokemon: (str) Nombre del Pokémon que se busca.
Retorno:
Devuelve True si el Pokémon es encontrado en el árbol, y False si no se encuentra.
Lógica:
Si el nodo actual es None, devuelve False.
Si el nombre del nodo actual coincide con nombre_pokemon, devuelve True.
Llama recursivamente a sí misma para buscar en el hijo izquierdo y luego en el hijo derecho. """


class PokemonNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None
    
def buscar_pokemon(nodo, nombre_pokemon):
    if nodo is None:
        return False
    if nodo.nombre == nombre_pokemon:
        return True
    return buscar_pokemon(nodo.izquierda, nombre_pokemon) or buscar_pokemon(nodo.derecha, nombre_pokemon)