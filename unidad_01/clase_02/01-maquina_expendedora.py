class MaquinaExpendedora():
    def __init__(self, cantidad_limite_fichas, cantidad_limite_prodcutos):
        self.cantidad_limite_fichas = cantidad_limite_fichas
        self.cantidad_limite_productos = cantidad_limite_prodcutos
        self.productos = []
        self.cantidad_extracciones = 0
        self.cantidad_reposiciones = 0
        self.cantidad_fichas = 0
    
    def extraccion(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            self.cantidad_extracciones += 1
            return True
        else:
            return False
    
    def reposicion(self, producto, cantidad):
        if (len(self.productos) + cantidad) <= self.cantidad_limite_productos:
            for x in range(cantidad):
                self.productos.append(producto)
                self.cantidad_reposiciones += 1
        else:
            return False
    
    def colocar_ficha(self, cantidad):
        if (self.cantidad_fichas + cantidad) <= self.cantidad_limite_fichas:
            self.cantidad_fichas += cantidad
    
    def get_stock(self):
        return len(self.productos)
    
    def get_extracciones(self):
        return self.cantidad_extracciones
    
    def get_reposiciones(self):
        return self.cantidad_reposiciones
    
    def get_fichas(self):
        return self.cantidad_fichas
    
    def get_productos(self):
        return self.productos
    
    def imprimir_estado(self):
        print(f'Reposiciones: {self.get_reposiciones()}')
        print(f'Extracciones: {self.get_extracciones()}')
        print(f'Productos: {self.get_productos()}')



m1 = MaquinaExpendedora(20,30)
res = m1.reposicion("Coca 500ml", 10)
print(res)
res= m1.reposicion("Fanta 600ml", 4)
print(res)
m1.extraccion("Fanta 600ml")
m1.extraccion("Fanta 600ml")
m1.extraccion("Fanta 600ml")
print(m1.productos)
m1.imprimir_estado()