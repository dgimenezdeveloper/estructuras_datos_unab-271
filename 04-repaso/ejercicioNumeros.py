""" Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
una que contenga los números pares y otra para los números impares. """
class Nodo:
    def __init__(self, dato):
        self.dato =  dato
        self.sig = None

class ListaNumeros:
    def __init__(self):
        self.cabeza = None
        self.cant = 0
    
    def es_vacio(self):
        return self.cabeza is None
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.es_vacio() or self.cabeza.dato > dato:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.sig and self.cabeza.dato <dato:
                aux = aux.sig
            nuevo.sig = aux.sig
            aux.sig = nuevo
        self.cant += 1
    
    def eliminar(self, dato):
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.sig
            self.cant -= 1
        else:
            aux = self.cabeza
            while aux.sig and aux.sig.dato != dato:
                aux = aux.sig
            aux.sig=aux.sig.sig
            self.cant -= 1
    
    def buscar(self, dato):
        aux = self.cabeza
        while aux and aux.dato != dato:
            aux = aux.sig
        return aux is not None
    
    def dividir(self):
        aux = self.cabeza
        pares=ListaNumeros()
        impares=ListaNumeros()
        while aux:
            if aux.dato % 2 == 0:
                pares.agregar(aux.dato)
            else:
                impares.agregar(aux.dato)
            aux = aux.sig
        return pares, impares
    
    def mostrar(self):
        if self.es_vacio():
            print("La lista está vacía")
        else:
            aux = self.cabeza
            while aux:
                print(f"|{aux.dato}| -> ", end="")
                aux = aux.sig
            print("None")
    
    def recorrer(self):
        aux = self.cabeza
        while aux:
            print(aux.dato)
            aux = aux.sig
    

numeros = ListaNumeros()
numeros.agregar(1)
numeros.agregar(2)
numeros.agregar(3)
numeros.agregar(4)
numeros.agregar(5)
numeros.agregar(6)
pares, impares = numeros.dividir()
print("Pares:")
pares.mostrar()
print("Impares:")
impares.mostrar()
print(numeros)
print(pares)