#Utilizando TADs se deberá representar y programar los métodos más importantes de una **factura** de **compra** y sus correspondientes **ítems** que la conforman. Una factura contiene información de número, fecha, importe total y cantidad de ítems. Sobre los ítems se conoce un código de producto, descripción del producto, cantidad y su precio unitario.


class Factura:
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha
        self.importe_total = 0
        self.cantidad_items = 0
        self.items = []

    def agregar_item(self, codigo_producto, descripcion_producto, cantidad, precio_unitario):
        item = {
            'codigo_producto': codigo_producto,
            'descripcion_producto': descripcion_producto,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario
        }
        self.items.append(item)
        self.cantidad_items += 1
        self.importe_total += cantidad * precio_unitario

    def obtener_importe_total(self):
        return self.importe_total

    def obtener_cantidad_items(self):
        return self.cantidad_items

    def obtener_items(self):
        return self.items

    def generar_informe(self):
        print(f'Factura N° {self.numero} - Fecha: {self.fecha}')
        print('---------------------------')
        for item in self.items:
            print(f'Código producto: {item["codigo_producto"]} - Descripción: {item["descripcion_producto"]} - Cantidad: {item["cantidad"]} - Precio unitario: {item["precio_unitario"]}')
        print('---------------------------')
        print(f'Importe total: {self.importe_total}\n')


def main():
    factura = Factura('A00001000', '25-09-2024')
    factura.agregar_item('A001', 'Samsung Galaxy S21', 1, 112400)
    factura.agregar_item('A002', 'Samsung Galaxy S21 Ultra', 1, 145000)
    print(factura.generar_informe())

main()