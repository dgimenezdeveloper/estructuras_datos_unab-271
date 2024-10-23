"""  Asumiendo  que  cuenta  con  la  implementación  de  un  árbol  binario  de  búsqueda, 
contar cuántos elementos son pares. """

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if not self.raiz:
            self.raiz = Nodo(dato)
        else:
            self._agregar(dato, self.raiz)

    def _agregar(self, dato, actual):
        if dato < actual.dato:
            if not actual.izq:
                actual.izq = Nodo(dato)
            else:
                self._agregar(dato, actual.izq)
        else:
            if not actual.der:
                actual.der = Nodo(dato)
            else:
                self._agregar(dato, actual.der)

    def contar_pares(self):
        return self._contar_pares(self.raiz)

    def _contar_pares(self, actual):
        if not actual:
            return 0
        return (actual.dato % 2 == 0) + self._contar_pares(actual.izq) + self._contar_pares(actual.der)
    
    def preorden(self):
        self._preorden(self.raiz)
        print()
    
    def _preorden(self, actual):
        if actual:
            print(actual.dato, end=' ')
            self._preorden(actual.izq)
            self._preorden(actual.der)
    
    def inorden(self):
        self._inorden(self.raiz)
        print()
        
    def _inorden(self, actual):
        if actual:
            self._inorden(actual.izq)
            print(actual.dato, end=' ')
            self._inorden(actual.der)
    
    def postorden(self):
        self._postorden(self.raiz)
        print()
    
    def _postorden(self, actual):
        if actual:
            self._postorden(actual.izq)
            self._postorden(actual.der)
            print(actual.dato, end=' ')
    

# Test
arbol = ArbolBinarioBusqueda()
arbol.agregar(40)
arbol.agregar(28)
arbol.agregar(70)
arbol.agregar(9)
arbol.agregar(32)
arbol.agregar(52)
arbol.agregar(10)
#print(arbol.contar_pares()) # 4
arbol.postorden()