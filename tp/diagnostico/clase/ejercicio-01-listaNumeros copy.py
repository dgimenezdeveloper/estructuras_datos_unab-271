""" 
Se tiene la siguiente lista [7, 8, 5, 9, 8, 6, 7, 7, 9, 11, 10]. 
Se puede utilizar funciones en la resolución.

Realizar un programa que muestre  la cantidad de números pares.

Realizar un programa que muestre el promedio de todos los números de la lista.
"""
def obtener_cantidad_pares(lista):
    return len([numero for numero in lista if numero % 2 == 0])

# def pares(lista):
#     cont = 0
#     for n in lista:
#         if n % 2 == 0:
#             cont += 1

def obtener_promedio(lista):
    return sum(lista) / len(lista)

def main():
    lista = [7, 8, 5, 9, 8, 6, 7, 7, 9, 11, 10]
    print(f'Cantidad de números pares: {obtener_cantidad_pares(lista)}')
    print(f'Promedio de la lista: {obtener_promedio(lista):.2f}')

main()