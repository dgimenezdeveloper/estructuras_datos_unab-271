""" Implementación de una pila en Python """
class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, valor):
        if self.pila_vacia():
            self.cima = NodoPila(valor) # Se crea una instancia de la clase NodoPila
        else:
            nodo = NodoPila(valor) # Se crea una instancia de la clase NodoPila
            nodo.siguiente = self.cima # Se guarda la referencia al nodo que está en la cima de la pila
            self.cima = nodo # Se le asigna a la cima de la pila el nuevo nodo creado
        self.tamanio += 1
    
    def desapilar(self):
        if not self.pila_vacia():
            valor = self.cima.valor
            pila.cima = self.cima.siguiente
            self.tamanio -= 1
            return valor
    
    def pila_vacia(self):
        if self.tamanio == 0:
            return True
    
    def obtener_cima(self):
        if not self.pila_vacia():
            return self.cima.valor
    
    def obtener_tamanio(self):
        return self.tamanio
    
    def recorrer(self):
        nodo = self.cima
        while nodo:
            print(nodo.valor)
            nodo = nodo.siguiente
    
    def imprimir(self):
        nodo = self.cima
        while nodo:
            print(nodo.valor)
            nodo = nodo.siguiente

pila = Pila()
pila.apilar(3)
pila.apilar(2)
pila.apilar(1)
pila.recorrer()
print('Cima:', pila.obtener_cima())
print('Tamaño:', pila.obtener_tamanio())
pila.desapilar()
pila.recorrer()
print('Cima:', pila.obtener_cima())
print('Tamaño:', pila.obtener_tamanio())
