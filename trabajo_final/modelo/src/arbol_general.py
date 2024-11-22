# src/arbol_general.py

class NodoGeneral:
    def __init__(self, evento):
        self.evento = evento
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

class ArbolGeneral:
    def __init__(self, evento_raiz):
        self.raiz = NodoGeneral(evento_raiz)

    def agregar_evento(self, nodo_padre, evento_hijo):
        nodo_hijo = NodoGeneral(evento_hijo)
        nodo_padre.agregar_hijo(nodo_hijo)
        return nodo_hijo