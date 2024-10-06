# Dado un arbol binario de busqueda, determinar la cantidad de nodos pares
class Nodo:
    def __init__(self, valor, dato):
        self.valor = valor
        self.dato = dato
        self.izq = None
        self.der = None
        
    def set_izq(self, nodo):
        self.izq = nodo
    
    def set_der(self, nodo):
        self.der = nodo
        
    def contar_nodos_pares(self):
        if self is None:
            return 0      
        # contamos los nodos pares del subarbol izq
        if self.izq is None:
            cant_izq = 0
        else:    
            cant_izq = self.izq.contar_nodos_pares()
        
        if self.valor % 2 == 0:
            cant = 1
        else:
            cant = 0
            
        if self.dato[0] == 'F':
            print(self.dato)    
        
        # contamos los nodos pares del subarbol der
        if self.der is None:
            cant_der = 0
        else:    
            cant_der = self.der.contar_nodos_pares()
        return cant_izq + cant + cant_der
        

arbol = None
arbol = Nodo(10, 'Felipe')
arbol.set_izq(Nodo(5, 'Jose'))
arbol.set_der(Nodo(15, 'Maria'))

c = arbol.contar_nodos_pares() 