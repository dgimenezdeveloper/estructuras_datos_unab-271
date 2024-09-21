class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return f"{self.valor}"

def arbol_vacio(raiz):
    return raiz == None 

def insertar_nodo(raiz, dato):
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif raiz.valor <= dato:
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz, nivel=0, prefijo="Raíz: "):
    if raiz is not None:
        print(" " * (nivel * 4) + prefijo + str(raiz.valor))
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
raiz = None
datos = [10, 5, 15, 3, 7, 12, 18]
for dato in datos:
    raiz = insertar_nodo(raiz, dato)

imprimir_arbol(raiz)