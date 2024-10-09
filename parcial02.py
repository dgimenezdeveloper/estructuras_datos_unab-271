""" Hacer una función recursiva, e iterativa que retorne si los dígitos de un número son pares """

def son_pares_recursivo(numero):
    if numero == 0:
        return True
    else:
        if numero % 2 == 0:
            return son_pares_recursivo(numero // 10)
        else:
            return False

def son_pares_iterativo(numero):
    while numero != 0:
        if numero % 2 == 0:
            numero = numero // 10
        else:
            return False
    return True