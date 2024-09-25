class NodoPila:
    def __init__(self):
        self.dato = None
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    def pila_vacia(self):
        return self.cima is None
    
    def apilar(self, dato):
        nuevo_nodo = NodoPila()
        nuevo_nodo.dato = dato # asignamos el dato al nuevo nodo
        if self.pila_vacia():
            self.cima = nuevo_nodo # cima ahora apunta al nuevo nodo
        else:
            nuevo_nodo.siguiente = self.cima # nuevo_nodo.siguiente apunta donde apuntaba cima, es decir, al nodo que estaba en la cima de la pila
            self.cima = nuevo_nodo # cima ahora apunta al nuevo nodo
        self.tamanio += 1
    
    def desapilar(self):
        if self.pila_vacia():
            return None
        else:
            dato = self.cima.dato # guardamos el dato que vamos a retornar en una variable
            self.cima = self.cima.siguiente # cima ahora apunta al nodo siguiente al que estaba apuntando antes
            self.tamanio -= 1
            return dato
    
    def tamanio_pila(self):
        return self.tamanio
    
    def cima_pila(self):
        if self.pila_vacia():
            return None
        else:
            return self.cima.dato
    
    def mostrar_pila(self):
        nodo_actual = self.cima
        while nodo_actual:
            print(f"| {nodo_actual.dato} |")
            print(" -----")
            nodo_actual = nodo_actual.siguiente
    
    def apilar_ordenado(self, dato):
        nuevo_nodo = NodoPila()
        nuevo_nodo.dato = dato
        if self.pila_vacia() or self.cima.dato >= dato:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
        else:
            nodo_actual = self.cima
            while nodo_actual.siguiente and nodo_actual.siguiente.dato < dato: # mientras haya un nodo siguiente y el dato del nodo siguiente sea menor al dato que queremos insertar
                nodo_actual = nodo_actual.siguiente # avanzamos al siguiente nodo
            nuevo_nodo.siguiente = nodo_actual.siguiente # el nodo siguiente del nuevo nodo apunta al nodo siguiente del nodo actual
            nodo_actual.siguiente = nuevo_nodo # el nodo siguiente del nodo actual apunta al nuevo nodo
        self.tamanio += 1
    
    def buscar_y_desapilar(self, dato):
        if self.pila_vacia():
            return None
        
        # Caso especial: el dato está en la cima
        elif self.cima.dato == dato:
            return self.desapilar()
        else:
            nodo_actual = self.cima
            while nodo_actual.siguiente and nodo_actual.siguiente.dato != dato:
                nodo_actual = nodo_actual.siguiente
            
            # Si encontramos el nodo con el dato
            if nodo_actual.siguiente and nodo_actual.siguiente.dato == dato:
                nodo_a_eliminar = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_a_eliminar.siguiente
                self.tamanio -= 1
                return nodo_a_eliminar.dato
        
        # Si no encontramos el dato
        return f'El dato {dato} no se encuentra en la pila'

# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila()
    pila.apilar_ordenado(5) # Cima -> 5
    pila.apilar_ordenado(3) # Cima -> 3 -> 5
    pila.apilar_ordenado(7) # Cima -> 3 -> 5 -> 7
    pila.apilar_ordenado(1) # Cima -> 1 -> 3 -> 5 -> 7
    pila.mostrar_pila() # 1 -> 3 -> 5 -> 7
    pila.buscar_y_desapilar(3) # Cima -> 1 -> 5 -> 7
    print("Después de eliminar el 3:")
    pila.mostrar_pila() # 1 -> 5 -> 7
    print("Desapilar un dato inexistente:")
    ras = pila.buscar_y_desapilar(10) 
    print(ras)