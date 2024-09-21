class ArbolBinario:
    def __init__(self, elemento, esMenor = lambda x, y: x < y):
        self.elemento = elemento
        self.izquierda = None
        self.derecha = None
        self.esMenor = esMenor

def insertar(arbol, elemento):
    if arbol is None:
        return ArbolBinario(elemento)
    elif arbol.esMenor(elemento, arbol.elemento):
        arbol.izquierda = insertar(arbol.izquierda, elemento)
    else:
        arbol.derecha = insertar(arbol.derecha, elemento)
    return arbol



def imprimir_arbol_grafico(arbol, espacio=0, nivel=0, separacion=4):
    if arbol is None:
        return

    espacio += separacion

    # Imprimir el subárbol derecho primero (nodos a la derecha)
    imprimir_arbol_grafico(arbol.derecha, espacio, nivel+1, separacion)

    # Imprimir el nodo actual
    print()
    print(" " * (espacio - separacion) + " " * separacion + f"{arbol.elemento}")

    # Imprimir el subárbol izquierdo después (nodos a la izquierda)
    imprimir_arbol_grafico(arbol.izquierda, espacio, nivel+1, separacion)

def imprimir_arbol(raiz, nivel=0, prefijo="Raíz: "):
    if raiz is not None:
        print(" " * (nivel * 4) + prefijo + str(raiz.elemento))
        if raiz.izquierda is not None or raiz.derecha is not None:
            if raiz.izquierda is not None:
                imprimir_arbol(raiz.izquierda, nivel + 1, "Izq: ")
            else:
                print(" " * ((nivel + 1) * 4) + "Izq: None")
            if raiz.derecha is not None:
                imprimir_arbol(raiz.derecha, nivel + 1, "Der: ")
            else:
                print(" " * ((nivel + 1) * 4) + "Der: None")


# Ejemplo de uso
arbol = insertar(None, 45)
arbol = insertar(arbol, 11)
arbol = insertar(arbol, 85)
arbol = insertar(arbol, 5)
arbol = insertar(arbol, 20)
arbol = insertar(arbol, 70)
arbol = insertar(arbol, 100)
arbol = insertar(arbol, 1)

imprimir_arbol_grafico(arbol)
print('#'*100)
imprimir_arbol(arbol)