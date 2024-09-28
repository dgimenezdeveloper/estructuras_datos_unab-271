""" 2. **Fibonacci**: Escribe una función recursiva que devuelva el n-ésimo número de la secuencia de Fibonacci. """


def fibo(num):
    if num <= 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
