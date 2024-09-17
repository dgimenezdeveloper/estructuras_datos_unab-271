""" Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir una función que 
muestre el número más alto, escriba el programa que invoque a la función """


def mostrar_mayor(lista):
    mayor = lista[0]
    n = len(lista)
    for i in range(1, n):
        if mayor < lista[i]:
            mayor = lista[i]
    print(f"El número ás grande es: {mayor}")


lista = [1, 14, 56, 43, 23, 46, 58, 123, 67]
mostrar_mayor(lista)