class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Pila:
    def __init__(self):
        self.cima = None
        self.cant = 0
    
    def pila_vacia(self):
        return self.cima is None
    
    def tamnio_pila(self):
        return self.cant
    
    def cima_pila(self):
        if self.pila_vacia():
            return None
        else:
            return self.cima.dato
    
    def apilar(self, dato):
        nuevo = NodoPila(dato)
        if self.pila_vacia():
            self.cima = nuevo
        else:
            nuevo.sig = self.cima
            self.cima = nuevo
        self.cant += 1
    
    def desapilar(self):
        if self.pila_vacia():
            return None
        else:
            dato = self.cima.dato
            self.cima = self.cima.sig
            self.cant -= 1
            return dato
        
    def apilar_odenado(self, dato):
        pila_aux = Pila()
        while not self.pila_vacia() and self.cima.dato < dato:
            pila_aux.apilar(self.desapilar())
        self.apilar(dato)
        while not pila_aux.pila_vacia():
            self.apilar(pila_aux.desapilar())
    
    def buscar_y_desapilar(self, dato):
        pila_aux = Pila()
        encontrado = False
        dato_encontrado = None
        while not self.pila_vacia() and not encontrado:
            dato_aux = self.desapilar()
            if dato_aux == dato:
                encontrado = True
                dato_encontrado = dato_aux
            else:
                pila_aux.apilar(dato_aux)
        while not pila_aux.pila_vacia():
            self.apilar(pila_aux.desapilar())
        return  dato_encontrado
    
    def mostrar_pila(self):
        nodo_act = self.cima
        while nodo_act:
            print(f'| {nodo_act.dato} |')
            print('-----')
            nodo_act = nodo_act.sig
# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila()
    pila.apilar_odenado(5) # Cima -> 5
    pila.apilar_odenado(3) # Cima -> 3 -> 5
    pila.apilar_odenado(7) # Cima -> 3 -> 5 -> 7
    pila.apilar_odenado(1) # Cima -> 1 -> 3 -> 5 -> 7
    pila.mostrar_pila() # 1 -> 3 -> 5 -> 7
    pila.buscar_y_desapilar(3) # Cima -> 1 -> 5 -> 7
    print("Después de eliminar el 3:")
    pila.mostrar_pila() # 1 -> 5 -> 7
    print("Desapilar un dato inexistente:")
    ras = pila.buscar_y_desapilar(10) 
    print(ras)