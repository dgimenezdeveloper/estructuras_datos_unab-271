""" 2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres. """
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCaracteres:
    def __init__(self):
        self.cabeza = None
        self.cant = 0
    
    def es_vacio(self):
        return self.cabeza is None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacio() or self.cabeza.dato > dato:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            aux = self.cabeza
            while aux.siguiente and aux.siguiente.dato < dato:
                aux = aux.siguiente
            nuevo_nodo.siguiente = aux.siguiente
            aux.siguiente = nuevo_nodo
        self.cant += 1
    
    def eliminar(self, dato):
        if self.cabeza.dato == dato:
            self.cabeza= self.cabeza.siguiente
            self.cant -= 1
        else:
            aux = self.cabeza
            while aux.siguiente and aux.siguiente.dato != dato:
                aux = aux.siguiente
            aux.siguiente = aux.siguiente.siguiente
            self.cant -= 1
    
    def buscar(self, dato):
        aux = self.cabeza
        while aux and aux.dato != dato:
            aux = aux.siguiente
        return aux is not None
    
    def eliminar_vocales(self):
        aux = self.cabeza
        vocales = "aeiouAEIOU"
        while aux:
            if self.buscar(aux.dato) and aux.dato in vocales:
                self.eliminar(aux.dato)
            aux = aux.siguiente
    
    def mostrar(self):
        if self.es_vacio():
            print("La lista está vacía")
        else:
            aux = self.cabeza
            while aux:
                print(f"|{aux.dato}| -> ", end="")
                aux = aux.siguiente
            print("None")

    def recorrer(self):
        aux = self.cabeza
        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def __len__(self):
        return self.cant
    
# Test
lista = ListaCaracteres()
lista.agregar("a")
lista.agregar("b")
lista.agregar("c")
lista.agregar("d")
lista.agregar("e")
lista.agregar("f")
lista.mostrar()
lista.eliminar_vocales()
lista.mostrar()