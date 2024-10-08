class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
    
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.cant = 0
    
    def cola_vacia(self):
        return self.frente is None
    
    def tamanio(self):
        return self.cant
    
    def mostrar_frente(self):
        if self.cola_vacia():
            return None
        return self.frente.dato
    
    def mostrar_final(self):
        if self.cola_vacia():
            return None
        return self.final.dato
    
    def encolar(self, dato):
        nuevo_nodo = NodoCola(dato)
        if self.cola_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.sig = nuevo_nodo
        self.final = nuevo_nodo
        self.cant += 1
    
    def desencolar(self):
        if self.cola_vacia():
            return None
        else:
            dato = self.frente.dato
            self.frente = self.frente.sig
            if self.frente is None:
                self.final = None
            self.cant -= 1
            return dato
    
    def encolar_ordenado(self, dato):
        cola_aux = Cola()
        while not self.cola_vacia() and self.frente.dato < dato:
            cola_aux.encolar(self.desencolar())
        cola_aux.encolar(dato)
        self.cant += 1
        while not cola_aux.cola_vacia():
            self.encolar(cola_aux.desencolar())
    
    def buscar_y_desencolar(self, dato):
        cola_aux = Cola()
        encontrado = False
        while not self.cola_vacia() and not encontrado:
            dato_act = self.desencolar()
            if dato_act == dato:
                encontrado = True
                self.cant -= 1
            else:
                cola_aux.encolar(dato_act)
        while not cola_aux.cola_vacia():
            self.encolar(cola_aux.desencolar())
        return encontrado
    
    def mostrar_cola(self):
        nodo_actual = self.frente
        while nodo_actual:
            print(f"{nodo_actual.dato} -> ", end="")
            nodo_actual = nodo_actual.sig
        print("None")

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()
    cola.encolar(5)
    cola.encolar(3)
    cola.encolar(7)
    cola.encolar(1)
    print("Cola original:")
    cola.mostrar_cola() # 5 -> 3 -> 7 -> 1 -> None
    
    print("Frente de la cola:", cola.mostrar_frente()) # Frente de la cola: 5
    print("Final de la cola:", cola.mostrar_final())   # Final de la cola: 1
    
    cola.encolar_ordenado(4)
    print("Cola después de encolar 4 de manera ordenada:")
    cola.mostrar_cola() # 1 -> 3 -> 4 -> 5 -> 7 -> None
    
    print("Frente de la cola:", cola.mostrar_frente()) # Frente de la cola: 1
    print("Final de la cola:", cola.mostrar_final())   # Final de la cola: 7
    
    print("Desencolar el elemento 4:")
    encontrado = cola.buscar_y_desencolar(4)
    print(f"Elemento encontrado y desencolado: {encontrado}")
    cola.mostrar_cola() # 1 -> 3 -> 5 -> 7 -> None