from listaEnlazada import ListaEnlazada, Nodo

lista = ListaEnlazada()

def pedir_datos():
    dato = int(input("Ingrese un número entero - 0 para finalizar: "))
    while dato != 0:
        lista.agregar(dato)
        dato = int(input("Ingrese un número entero - 0 para finalizar: "))

def mostrar_menu():
    print("1. Agregar un elemento a la lista")
    print("2. Eliminar un elemento de la lista")
    print("3. Buscar un elemento en la lista")
    print("4. Mostrar la lista")
    print("5. Recorrer la lista")
    print("6. Mostrar la cantidad de elementos de la lista")
    print("7. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def main():
    pedir_datos()
    opcion = mostrar_menu()
    while opcion != 7:
        if opcion == 1:
            dato = int(input("Ingrese un número entero: "))
            lista.agregar(dato)
        elif opcion == 2:
            dato = int(input("Ingrese un número entero: "))
            if lista.buscar(dato):
                lista.eliminar(dato)
            else:
                print("El elemento no se encuentra en la lista")
        elif opcion == 3:
            dato = int(input("Ingrese un número entero: "))
            if lista.buscar(dato):
                print("El elemento se encuentra en la lista")
            else:
                print("El elemento no se encuentra en la lista")
        elif opcion == 4:
            lista.mostrar()
        elif opcion == 5:
            lista.recorrer()
        elif opcion == 6:
            print(f"La cantidad de elementos de la lista es: {len(lista)}")
        else:
            print("Opción inválida")
        opcion = mostrar_menu()

if __name__ == "__main__":
    main()