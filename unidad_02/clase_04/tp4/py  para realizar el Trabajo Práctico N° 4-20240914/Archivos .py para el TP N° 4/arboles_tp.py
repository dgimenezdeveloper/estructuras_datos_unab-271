import random


class NodoArbol:
    """Clase que representa un nodo en un árbol."""

    def __init__(self, data):
        """Inicializa un nodo con un valor (data) y una lista vacía de hijos."""
        self.data = data
        self.hijos = []

    def agregar_hijo(self, hijo):
        """Añade un nodo hijo a la lista de hijos."""
        self.hijos.append(hijo)

    def obtener_data(self):
        """Devuelve el valor almacenado en el nodo."""
        return self.data

    def obtener_hijos(self):
        """Devuelve la lista de hijos del nodo."""
        return self.hijos

    def eliminar_hijo(self, hijo):
        """Elimina un nodo hijo de la lista de hijos si existe."""
        if hijo in self.hijos:
            self.hijos.remove(hijo)
        else:
            print("El hijo no existe en la lista de hijos.")

    def contar_hijos(self):
        """Devuelve la cantidad de hijos del nodo."""
        return len(self.hijos)

    def __str__(self):
        """Sobrescribe la representación en cadena del nodo llamando a `dibujar_arbol`."""
        return self.dibujar_arbol()

    def dibujar_arbol(self, nivel=0):
        """Dibuja el árbol a partir del nodo actual y sus hijos, mostrando la jerarquía.
        - Parámetros:
            - nivel: int
                - Nivel de profundidad en el árbol, usado para la indentación visual."""
        resultado = "  " * nivel + "└── " + str(self.data) + "\n"
        for hijo in self.hijos:
            resultado += hijo.dibujar_arbol(nivel + 1)
        return resultado


# Example usage of the NodoArbol class
if __name__ == "__main__":
    # Create a root node
    root = NodoArbol("raiz")

    # Create child nodes
    child1 = NodoArbol("nodo 1")
    child2 = NodoArbol("nodo 2")
    child3 = NodoArbol("nodo 3")
    child4 = NodoArbol("nodo 4")
    child5 = NodoArbol("nodo 5")
    child6 = NodoArbol("nodo 6")
    child7 = NodoArbol("nodo 7")
    child8 = NodoArbol("nodo 8")
    child9 = NodoArbol("nodo 9")
    child10 = NodoArbol("nodo 10")

    # Add child nodes to the root node

    root.agregar_hijo(child10)

    # Create child nodes for each child node
    for i in range(1, random.randint(1, 6)):
        child = NodoArbol(f"nodo {i}")
        root.agregar_hijo(child)
        for j in range(1, random.randint(1, 5)):
            subchild = NodoArbol(f"nodo {i}.{j}")
            child.agregar_hijo(subchild)
            for k in range(1, random.randint(1, 4)):
                subsubchild = NodoArbol(f"nodo {subchild.obtener_data()}.{k}")
                subchild.agregar_hijo(subsubchild)

    # Print the tree structure
    print(root)
