class NodoCola:
    def __init__(self):
        self.dato = None
        self.siguiente = None
    
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0
    
    def cola_vacia(self):
        return self.frente is None
    
    def encolar(self, dato):
        nuevo_nodo = NodoCola()
        nuevo_nodo.dato = dato
        if self.cola_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo 
        self.final = nuevo_nodo
        self.tamanio += 1
    
    def desencolar(self):
        if self.cola_vacia():
            return None
        else:
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            self.tamanio -= 1
            return dato
    
    