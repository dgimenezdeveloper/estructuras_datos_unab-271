class Item:
    def __init__(self, cod_prod,descripcion, cantidad, precio_unitario):
        self.cod_prod = cod_prod
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    
    def calcular_importe(self):
        return self.cantidad * self.precio_unitario

class Factura:
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha
        self.items = []
        self.importe = 0.0
    
    def agregar_item(self, item):
        self.items.append(item)
        self.importe += item.calcular_importe()
    
    def eliminar_item(self, item):
        pass
    
    def calcular_importe_total(self):
        total = 0
        for item in self.items:
            total += item.calcular_importe()
        return total
    
    def imprimir_factura(self, items):
        print(f"Factura Nro: {self.numero}")
        print(f"Fecha: {self.fecha}")
        print('Items: ')
        for item in items:
            print(f'Código: {item.cod_prod} - Descripción: {item.descripcion} - Cantidad: {item.cantidad} - Precio unitario: {item.precio_unitario} - Importe: {item.calcular_importe()}')
        print(f'Importe total: {self.importe}')

if __name__ == '__main__':
    item1 = Item(1, 'Producto 1', 2, 100)
    item2 = Item(2, 'Producto 2', 3, 150)
    item3 = Item(3, 'Producto 3', 1, 200)
    factura = Factura(1, '2021-09-01')
    factura.agregar_item(item1)
    factura.agregar_item(item2)
    factura.agregar_item(item3)
    factura.imprimir_factura(factura.items)