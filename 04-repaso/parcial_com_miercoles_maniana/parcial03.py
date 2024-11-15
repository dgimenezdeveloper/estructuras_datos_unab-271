""" Contando que cuenta con un árbol binario, hacer los recorridos
Crear la función post-orden que imprima los números impares """

class Arbol:
    def __init__(self, elemento, izquierda = None, derecha = None):
        self.elemento = elemento
        self.izquierda = izquierda
        self.derecha = derecha

def agregar(arbol, valor):
    if arbol is None:
        return Arbol(valor)
    elif valor < arbol.elemento:
        arbol.izquierda = agregar(arbol.izquierda, valor)
    else:
        arbol.derecha = agregar(arbol.derecha, valor)
    return arbol

def preorden(arbol):
    if arbol is not None:
        print(arbol.elemento)
        preorden(arbol.izquierda)
        preorden(arbol.derecha)

def inorden(arbol):
    if arbol is not None:
        inorden(arbol.izquierda)
        print(arbol.elemento)
        inorden(arbol.derecha)

def postorden(arbol):
    if arbol is not None:
        postorden(arbol.izquierda)
        postorden(arbol.derecha)
        print(arbol.elemento)

def post_orden_impares(arbol):
    if arbol is not None:
        post_orden_impares(arbol.izquierda)
        post_orden_impares(arbol.derecha)
        if arbol.elemento % 2 != 0:
            print(arbol.elemento)

def main():
    arbol = Arbol(10)
    arbol = agregar(arbol, 5)
    arbol = agregar(arbol, 15)
    arbol = agregar(arbol, 3)
    arbol = agregar(arbol, 7)
    arbol = agregar(arbol, 13)
    arbol = agregar(arbol, 17)
    print('Preorden:')
    preorden(arbol)
    print('Inorden:')
    inorden(arbol)
    print('Postorden:')
    postorden(arbol)
    print('Postorden Impares:')
    post_orden_impares(arbol)

main()