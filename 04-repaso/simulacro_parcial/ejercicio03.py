"""  Asumiendo que cuenta con la implementación de un árbol binario de búsqueda, contar cuántos elementos son pares. """
class nodo_arbol(object):
    def __init__(self,info):
        self.izquierda = None
        self.derecha =None
        self.informacion = info

    def es_vacio(self):
        return self.informacion is None

    def agregar_ordenado(self, dato):
        if self.es_vacio():
            self.informacion = dato
        elif dato < self.informacion:
            if self.izquierda is None:
                self.izquierda = nodo_arbol(dato)
            else:
                self.izquierda.agregar_ordenado(dato)
        else:
            if self.derecha is None:
                self.derecha = nodo_arbol(dato)
            else:
                self.derecha.agregar_ordenado(dato)
    
    def imprimir(self):
        if self is None:
            return
        if self.izquierda:
            self.izquierda.imprimir()
        print(self.informacion)
        if self.derecha:
            self.derecha.imprimir()

    def contar_pares(self):
        if self is None:
            return 0
        contador = 0
        if self.izquierda is not None:
            contador += self.izquierda.contar_pares()
        if self.informacion % 2 == 0:
            contador += 1
        if self.derecha is not None:
            contador += self.derecha.contar_pares()
        return contador



# Test
arbol = nodo_arbol(45)
arbol.agregar_ordenado(11)
arbol.agregar_ordenado(85)
arbol.agregar_ordenado(10)
arbol.agregar_ordenado(12)
arbol.agregar_ordenado(84)
arbol.agregar_ordenado(86)
arbol.imprimir()
print(arbol.contar_pares()) # 4