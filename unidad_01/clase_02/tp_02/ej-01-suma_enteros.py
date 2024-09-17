"""Definir una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado."""

def suma_enteros(numero):
    suma = 0
    for i in range(0, numero):
        suma += i
    return suma

def main():
    print(f'La suma total es de {suma_enteros(5)}')

main()
