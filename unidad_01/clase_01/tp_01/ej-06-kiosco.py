"""
Escribir un programa que permita ingresar datos de un Kiosko. Código del producto,
nombre del producto, marca del producto, proveedor, precio, stock. La carga de datos finalizará
cuando ingrese como código de producto 9999.
"""

def cargar_productos():
    productos = {}
    continuar = True
    while continuar:
        codigo = int(input('Ingrese el código del producto: '))
        if (codigo == 9999):
            continuar = False
        else:
            nombre = input('Ingrese el nombre del producto: ')
            marca = input('Ingrese marca del producto: ')
            proveedor = input('Ingrese el nombre del proveedor: ')
            precio = input('Ingrese el precio del producto: ')
            stock = input('Ingrese el stock del producto: ')
            productos[codigo] = {'nombre': nombre, 'marca': marca, 'proveedor': proveedor, 'precio': precio, 'stock': stock}
    return productos

def mostrar_productos(productos):
    for codigo, datos in productos.items():
        print(f'Código: {codigo}')
        print(f'Nombre: {datos["nombre"]}')
        print(f'Marca: {datos["marca"]}')
        print(f'Proveedor: {datos["proveedor"]}')
        print(f'Precio: {datos["precio"]}')
        print(f'Stock: {datos["stock"]}')

def main():
    productos = cargar_productos()
    mostrar_productos(productos)

main()