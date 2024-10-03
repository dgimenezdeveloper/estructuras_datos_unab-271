""" ## Ejercicio 4: Sistema de ventas de productos y stock
Desarrolla un sistema que gestione el inventario de una tienda. La tienda vende Productos y realiza Ventas.

Un Producto tiene ID, nombre, precio, stock disponible.
Una Venta tiene número de venta, producto vendido, cantidad, fecha, total venta.
Requisitos:

# Realizar una venta, si hay suficiente stock.
# Modificar el stock de un producto.
# Consultar el stock disponible de un producto.
# Consultar el historial de ventas de un producto.
Generar un informe de todas las ventas realizadas en una fecha determinada. """


class Ventas:
    def __init__(self, num_venta, producto, cantidad, fecha, total_venta):
        self.num_venta = num_venta
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.total_venta = total_venta

    def __str__(self):
        return f"Número de venta: {self.num_venta}, Producto: {self.producto}, Cantidad: {self.cantidad}, Fecha: {self.fecha}, Total de la venta: {self.total_venta}"


class Productos:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Stock disponible: {self.stock}"


class Tienda:
    def __init__(self):
        self.ventas = []
        self.productos = []
    
    def __str__(self):
        return f"Ventas: {self.ventas}, Productos: {self.productos}"
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def _agregar_venta(self, venta):
        self.ventas.append(venta)
    
    def vender(self, producto, cantidad, fecha):
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            total_venta = producto.precio * cantidad
            venta = Ventas(len(self.ventas) + 1, producto, cantidad, fecha, total_venta)
            self._agregar_venta(venta)
            print(f"Venta realizada con éxito. Stock actualizado.")
        else:
            print("No hay suficiente stock para realizar la venta.")
    
    def modificar_stock(self, producto, cantidad):
        producto.stock += cantidad
        print(f"Stock actualizado: {producto.stock}")
    
    def consultar_stock(self, producto):
        return producto.stock
    
    def historial_ventas(self, producto):
        for venta in self.ventas:
            if venta.producto == producto:
                print(venta)
    
    def informe_ventas(self, fecha):
        for venta in self.ventas:
            if venta.fecha == fecha:
                print(venta)
    
    
# Instanciar la tienda
tienda = Tienda()
# Agregar productos
producto1 = Productos(1, "Producto 1", 100, 10)
producto2 = Productos(2, "Producto 2", 200, 5)
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
# Realizar ventas
tienda.vender(producto1, 3, "2021-09-01")
tienda.vender(producto2, 2, "2021-09-02")
# Modificar stock
tienda.modificar_stock(producto1, 5)
# Consultar stock
print(tienda.consultar_stock(producto1))
# Historial de ventas
tienda.historial_ventas(producto1)
# Informe de ventas
tienda.informe_ventas("2021-09-01")