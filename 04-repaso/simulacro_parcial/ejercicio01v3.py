""" Utilizando TADs se deberá representar y programar los métodos más importantes de una **factura** de **compra** y sus correspondientes **ítems** que la conforman. Una factura contiene información de número, fecha, importe total y cantidad de ítems. Sobre los ítems se conoce un código de producto, descripción del producto, cantidad y su precio unitario. """
class Factura:
    def __init__(self, numero, fecha, importe_total, cantidad_items):
        self.numero = numero
        self.fecha = fecha
        self.importe_total = importe_total
        self.cantidad_items = cantidad_items
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def quitar_item(self, item):
        self.items.remove(item)

    def obtener_item(self, index):
        return self.items[index]

    def __str__(self):
        return f"Factura Nº {self.numero} - Fecha: {self.fecha} - Importe Total: {self.importe_total} - Cantidad de ítems: {self.cantidad_items}"
    
class Item:
    def __init__(self, codigo_producto, descripcion, cantidad, precio_unitario):
        self.codigo_producto = codigo_producto
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"Código: {self.codigo_producto} - Descripción: {self.descripcion} - Cantidad: {self.cantidad} - Precio Unitario: {self.precio_unitario}"


def main():
    factura = Factura(1, "01/01/2021", 1000, 2)
    item1 = Item(1, "Producto 1", 2, 500)
    item2 = Item(2, "Producto 2", 1, 500)
    factura.agregar_item(item1)
    factura.agregar_item(item2)
    print(factura)
    print(factura.obtener_item(0))
    print(factura.obtener_item(1))
    factura.quitar_item(item1)
    print(factura)

if __name__ == "__main__":
    main()