# Area de Funciones


def agregar(lista):
    nuevoproducto = input("Ingrese el nombre del nuevo producto: ")
    precio = float(input("Ingrese el precio del nuevo producto: "))
    stock = int(input("Ingrese la cantidad de productos (stock): "))
    prod = [nuevoproducto, precio, stock]
    lista.append(prod)
    return lista


# Programa Principal
print("Bienvenidos a la tienda ALOISE FV")
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
5. Cantidad total de productos que hay en ALOISE FV
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
        # productos=actualizarstock(productos)
        # print (productos)

    elif opcion == 3:
        print("Eligio la opcion 3")

    elif opcion == 4:
        print("Vamos a ingresar un nuevo producto")
        productos = agregar(productos)
        print(productos)

    elif opcion == 5:
        print("Eligio la opcion 5")

    else:
        print("No elegiste una opcion del menu.")

    print(menu)
    opcion = int(input("ingrese una opcion del menu:"))

print("Gracias por usar el Sistema")
