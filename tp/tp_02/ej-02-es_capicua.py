"""Implementar una función que me permita ver si un número es capicúa o no."""

def es_capicua(numero):
    original = numero
    inverso = 0
    while numero > 0:
        digito = numero % 10
        inverso = inverso * 10 + digito
        numero //= 10
    return inverso == original

def main():
    print(es_capicua(123321)) # True
    print(es_capicua(12210))  # False

main()