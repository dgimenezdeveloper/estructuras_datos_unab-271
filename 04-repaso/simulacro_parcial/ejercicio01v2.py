""" Utilizando TADs se deberá representar y programar los métodos más importantes de una **factura** de **compra** y sus correspondientes **ítems** que la conforman. Una factura contiene información de número, fecha, importe total y cantidad de ítems. Sobre los ítems se conoce un código de producto, descripción del producto, cantidad y su precio unitario. """
class FacturaCompraItems:
    def __init__(self, cod_prod, descripcion, cantidad, precio_unitario):
        self.cod_prod = cod_prod
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.importe = cantidad * precio_unitario

class FacturaCompra:
    def __init__(self, num_fac, fecha):
        self.numero = num_fac
        self.fecha = fecha
        self.items = []
        self.importe_total = 0.0
    
    def agregar_item(self, cod_prod, descripcion, cantidad, precio_unitario):
        item = FacturaCompraItems(cod_prod, descripcion, cantidad, precio_unitario)
        self.items.append(item)
        self.importe_total += item.importe
    
    def eliminar_item(self, cod_prod):
        """ Se elimina un ítem de la factura por código de producto """
        for item in self.items:
            if item.cod_prod == cod_prod:
                self.importe_total -= item.importe
                self.items.remove(item)
                return
    
    def mostrar_factura(self):
        print(f"Factura N° {self.numero}")
        print(f"Fecha: {self.fecha}")
        print(f"Importe total: {self.importe_total}")
        print("Detalle de ítems:")
        for item in self.items:
            print(f"Código: {item.cod_prod}")
            print(f"Descripción: {item.descripcion}")
            print(f"Cantidad: {item.cantidad}")
            print(f"Precio unitario: {item.precio_unitario}")
            print(f"Importe: {item.importe}")
            print("")

def main():
    factura = FacturaCompra('A00001000', '25-09-2024')
    factura.agregar_item('A001', 'Samsung Galaxy S21', 1, 112400)
    factura.agregar_item('A002', 'Samsung Galaxy S21 Ultra', 1, 145000)
    factura.mostrar_factura()

main()