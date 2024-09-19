"""  Agregar una función al programa anterior llamada carga_datos , que no  recibe ningún 
parámetro, la función deberá cargar los datos de la tienda ALOISE Burzaco" , la carga de datos termina 
cuando se ingresa como nombre del producto “zzz”. 
Nota: los datos a cargar deberán ser el nombre del producto, el precio  y el stock 
productos= [["HELADERA", 230000, 12 ],["LUSTRADORA", 100000,4 ], ["HORNO",240000, 4 ], ["LAVADORA", 120000, 5 ], 
["SECADORA", 130000, 8 ] ] """

# Area de Funciones


def agregar(lista):
    nuevoproducto = input("Ingrese el nombre del nuevo producto: ")
    precio = float(input("Ingrese el precio del nuevo producto: "))
    stock = int(input("Ingrese la cantidad de productos (stock): "))
    prod = [nuevoproducto, precio, stock]
    lista.append(prod)
    return lista

def actualizarStock(productos):
    nombre = input('Ingrese el producto a actualizar: ').upper()
    for producto in productos:
        if nombre == producto[0]:
            stock = int(input('Ingrese el nuevo stock: '))
            producto[2] = stock
    return productos

def precio_promedio(productos):
    suma = 0
    contador = 0
    for producto in productos:
        suma += producto[1]
        contador +=1
    return (suma/contador)

def cantidad_productos(productos):
    return len(productos)

########## EJERCICIO 2 

def carga_datos():
    productos = []
    nombre = input('Ingrese el nombre dle producto - (zzz para salir): ').upper()
    while nombre != 'ZZZ':
        precio = float(input('Ingrese el precio del producto: '))
        stock = int(input('Ingrese la cantidad de productos (stock): '))
        productos.append([nombre, precio, stock])
        nombre = input('Ingrese el nombre dle producto - (zzz para salir): ').upper()
    return productos

# Programa Principal
print("Bienvenidos a la tienda ALOISE BURZACO")
print()
productos = [
    ["HELADERA", 230000, 12],
    ["LUSTRADORA", 100000, 4],
    ["HORNO", 240000, 4],
    ["LAVADORA", 120000, 5],
    ["SECADORA", 130000, 8],
]


menu = """

(1) Mostrar la lista de productosy precios
(2) Actualice el stock de un producto  
(3) Precio promedio de los productos
4. Ingrese un nuevo producto
5. Cantidad total de productos que hay en ALOISE BURZACO
6. Salir
"""

print(menu)
opcion = int(input("ingrese una opcion del menu:"))
while opcion != 6:

    if opcion == 1:
        print("Eligio la opcion 1")
        print(productos)

    elif opcion == 2:
        print("Vamos a actualizar el stock de un producto")
        productos=actualizarStock(productos)
        #print(productos)

    elif opcion == 3:
        print("Eligio la opcion 3")
        promedio = precio_promedio(productos)
        print(f'El precio promedio de los productos es: {promedio}')

    elif opcion == 4:
        print("Vamos a ingresar un nuevo producto")
        productos = agregar(productos)
        print(productos)

    elif opcion == 5:
        print("Eligio la opcion 5")
        cantidad = cantidad_productos(productos)
        print(f'El total de productos en ALOISE BURZACO es: {cantidad}')

    else:
        print("No elegiste una opcion del menu.")

    print(menu)
    opcion = int(input("ingrese una opcion del menu:"))

print("Gracias por usar el Sistema")

# PRUEBA EJERCICIO 2
print(carga_datos())