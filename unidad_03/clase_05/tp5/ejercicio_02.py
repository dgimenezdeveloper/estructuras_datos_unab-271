""" Utilizando TADs se deberá representar y programar los métodos más importantes de 
una proforma de venta de  productos. La proforma contiene la siguiente información: Número de 
la proforma, fecha, vendedor y Detalle de la proforma y propuesta económica.  El detalle de la 
proforma  tendrá:  código  del  producto,  nombre  del  producto,  marca,  cantidad  y  precio  del 
producto. 
Es importante precisar que cada proforma puede contener uno o más productos.  Debe definir 
los métodos: agregar_producto, imprimir  la proforma y eliminar un producto de la proforma. """

class Proforma:
    def __init__(self, numero, fecha, vendedor):
        self.numero = numero
        self.fecha = fecha
        self.vendedor = vendedor
        self.detalle = []
    
    def agregar_producto(self, producto):
        self.detalle.append(producto)
    
    def eliminar_producto(self, codigo):
        for producto in self.detalle:
            if producto.codigo == codigo:
                self.detalle.remove(producto)
                return True
        return False
    
    def mostrar_proforma(self):
        print(f'Número de proforma: {self.numero}')
        print(f'Fecha: {self.fecha}')
        print(f'Vendedor: {self.vendedor}')
        print('Detalle de la proforma:')
        for producto in self.detalle:
            producto.mostrar_producto()
            print('---------------------')
            
class Producto:
    def __init__(self, codigo, nombre, marca, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
    
    def mostrar_producto(self):
        print(f'Código: {self.codigo}')
        print(f'Nombre: {self.nombre}')
        print(f'Marca: {self.marca}')
        print(f'Cantidad: {self.cantidad}')
        print(f'Precio: {self.precio}')


# Crear productos
producto1 = Producto(1, 'Producto 1', 'Marca 1', 2, 100)
producto2 = Producto(2, 'Producto 2', 'Marca 2', 3, 200)
producto3 = Producto(3, 'Producto 3', 'Marca 3', 4, 300)
producto4 = Producto(4, 'Producto 4', 'Marca 4', 5, 400)

# Crear proforma
proforma = Proforma(1, '2021-10-10', 'Vendedor 1')
proforma.agregar_producto(producto1)
proforma.agregar_producto(producto2)
proforma.agregar_producto(producto3)
proforma.agregar_producto(producto4)

# Mostrar proforma
proforma.mostrar_proforma()