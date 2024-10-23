"""  Utilizando TADs se deberá representar y programar los métodos más importantes de 
una  factura  de  venta  y  sus  correspondientes  ítems  que  la  conforman.  Una  factura  contiene 
información de número, fecha, importe total y cantidad de ítems. Sobre los ítems se conoce un 
código  de  producto,  descripción  del  producto,  cantidad  y  su  precio  unitario.  Importante 
agregar_item y el imprimir en factura  """

class Factura:
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha
        self.items = []
        self.importe_total = 0.0
    
    def agregar_item(self, cod_prod, descripcion, cantidad, precio_unitario):
        item = [cod_prod, descripcion, cantidad, precio_unitario]
        self.items.append(item)
        self.importe_total += cantidad * precio_unitario
        
    def eliminar_item(self, cod_prod):
        # Consideramos que se elimina de a un item a la vez
        # Todo: Descontar el precio unitario del item eliminado del importe total
        pass
    
    def get_importe(self):
        return self.importe_total
    
    def imprimir_factura(self):
        print(f"Factura Nro: {self.numero}")
        print(f"Fecha: {self.fecha}")
        print('Items: ')
        for item in self.items:
            print(f'Código: {item[0]} - Descripción: {item[1]} - Cantidad: {item[2]} - Precio unitario: {item[3]} - Importe: {item[2] * item[3]}')
        print(f'Importe total: {self.importe_total}')

if __name__ == '__main__':
    factura = Factura(1, '2021-09-01')
    factura.agregar_item(1, 'Producto 1', 2, 100)
    factura.agregar_item(2, 'Producto 2', 3, 150)
    factura.agregar_item(3, 'Producto 3', 1, 200)
    factura.imprimir_factura()