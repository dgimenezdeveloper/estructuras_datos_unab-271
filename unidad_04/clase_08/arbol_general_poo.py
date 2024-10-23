class Nodo:
    def __init__(self, info):
        self.info = info
        self.hijos = []

class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def arbol_vacio(self):
        return self.raiz is None

    def agregar_hijo_raiz(self, info):
        if self.arbol_vacio():
            self.raiz = Nodo(info)
        else:
            self.raiz.hijos.append(Nodo(info))
        return self.raiz

    def agregar_hijo_nodo(self, nodo, info):
        nuevo_hijo = Nodo(info)
        nodo.hijos.append(nuevo_hijo)
        return nodo

    def buscar_nodo(self, nodo, info):
        if nodo is None:
            return None
        if nodo.info == info:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_nodo(hijo, info)
            if resultado is not None:
                return resultado
        return None

    def eliminar_nodo(self, nodo, info):
        if nodo is None:
            return None
        for i, hijo in enumerate(nodo.hijos):
            if hijo.info == info:
                del nodo.hijos[i]
                return nodo
            self.eliminar_nodo(hijo, info)
        return nodo

    def preorden(self, nodo):
        if nodo is None:
            return
        print(nodo.info)
        for hijo in nodo.hijos:
            self.preorden(hijo)

    def postorden(self, nodo):
        if nodo is None:
            return
        for hijo in nodo.hijos:
            self.postorden(hijo)
        print(nodo.info)

    def por_niveles(self):
        if self.arbol_vacio():
            return
        cola = []
        cola.append(self.raiz)
        while cola:
            nodo = cola.pop(0)
            print(nodo.info)
            for hijo in nodo.hijos:
                cola.append(hijo)

def main():
    arbol = ArbolGeneral()
    raiz = arbol.agregar_hijo_raiz('A')
    arbol.agregar_hijo_nodo(raiz, 'B')
    arbol.agregar_hijo_nodo(raiz, 'C')
    nodo = arbol.buscar_nodo(raiz, 'B')
    arbol.agregar_hijo_nodo(nodo, 'D')
    arbol.agregar_hijo_nodo(nodo, 'E')
    nodo = arbol.buscar_nodo(raiz, 'C')
    arbol.agregar_hijo_nodo(nodo, 'F')
    # recorrido en preorden
    print('Recorrido en preorden')
    arbol.preorden(arbol.raiz)
    # recorrido en postorden
    print('Recorrido en postorden')
    arbol.postorden(arbol.raiz)
    # recorrido por niveles
    print('Recorrido por niveles')
    arbol.por_niveles()

main()