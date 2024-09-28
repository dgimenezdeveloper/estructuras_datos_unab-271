# 7. **Máximo común divisor (MCD)**: Escribe una función recursiva que calcule el MCD de dos números usando el algoritmo de Euclides.
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)