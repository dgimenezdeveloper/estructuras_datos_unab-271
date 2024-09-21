class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cantidad = 0
        
    def es_vacio(self):
        return self.cabeza is None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacio() or self.cabeza.dato >= dato:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual =  self.cabeza
            while actual.siguiente and actual.siguiente.dato < dato:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.cantidad +=1
    
    def eliminar(self, dato):
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.cantidad -= 1
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato != dato:
                actual = actual.siguiente
            actual.siguiente = actual.siguiente.siguiente
            self.cantidad -= 1
    
    def buscar(self, dato):
        actual = self.cabeza
        while actual and actual.dato != dato:
            actual = actual.siguiente
        return actual is not None

    def mostrar(self):
        if self.es_vacio():
            print("La lista está vacía")
        else:
            actual = self.cabeza
            while actual:
                print(f"|{actual.dato}| -> ", end="")
                actual = actual.siguiente
            print("None")
    
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def __len__(self):
        return self.cantidad

# Ejemplo de uso de la clase ListaEnlazada
if __name__ == "__main__":
    mi_lista = ListaEnlazada()
    mi_lista.agregar(10)
    mi_lista.agregar(20)
    mi_lista.agregar(30)
    mi_lista.agregar(40)
    mi_lista.mostrar()
    mi_lista.eliminar(30)
    print("Se eliminó el 30")
    mi_lista.mostrar()
    mi_lista.recorrer()
