class Nodo:
    def __init__(self, info):
        self.info = info
        self.hijos = []

class ArbolGeneral:
    def __init__(self):
        self.raiz = None

def arbol_vacio(arbol):
    return arbol.raiz is None

def agregar_hijo_raiz(arbol, info):
    if arbol_vacio(arbol):
        arbol.raiz = Nodo(info)
    else:
        arbol.raiz.hijos.append(Nodo(info))
    return arbol.raiz

def agregar_hijo_nodo(nodo, info):
    nuevo_hijo = Nodo(info)
    nodo.hijos.append(nuevo_hijo)
    return nodo

def buscar_nodo(nodo, info):
    if nodo is None:
        return None
    if nodo.info == info:
        return nodo
    for hijo in nodo.hijos:
        resultado = buscar_nodo(hijo, info)
        if resultado is not None:
            return resultado
    return None

def eliminar_nodo(nodo, info):
    if nodo is None:
        return None
    for i, hijo in enumerate(nodo.hijos):
        if hijo.info == info:
            del nodo.hijos[i]
            return nodo
        eliminar_nodo(hijo, info)
    return nodo

def preorden(nodo):
    if nodo is None:
        return
    print(nodo.info)
    for hijo in nodo.hijos:
        preorden(hijo)

def postorden(nodo):
    if nodo is None:
        return
    for hijo in nodo.hijos:
        postorden(hijo)
    print(nodo.info)

def por_niveles(arbol):
    if arbol_vacio(arbol):
        return
    cola = []
    cola.append(arbol.raiz)
    while cola:
        nodo = cola.pop(0)
        print(nodo.info)
        for hijo in nodo.hijos:
            cola.append(hijo)

def main():
    arbol = ArbolGeneral()
    raiz = agregar_hijo_raiz(arbol, 'A')
    agregar_hijo_nodo(raiz, 'B')
    agregar_hijo_nodo(raiz, 'C')
    nodo = buscar_nodo(raiz, 'B')
    agregar_hijo_nodo(nodo, 'D')
    agregar_hijo_nodo(nodo, 'E')
    nodo = buscar_nodo(raiz, 'C')
    agregar_hijo_nodo(nodo, 'F')
    #recorrido en preorden
    print('Recorrido en preorden')
    preorden(arbol.raiz)
    #recorrido en postorden
    print('Recorrido en postorden')
    postorden(arbol.raiz)
    #recorrido por niveles
    print('Recorrido por niveles')
    por_niveles(arbol)

main()