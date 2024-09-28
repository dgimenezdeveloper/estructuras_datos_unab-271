""" 3. **Suma de dígitos**: Escribe una función recursiva que sume los dígitos de un número entero. """


def suma_numeros(num):
    if num == 0:
        return 0
    else:
        return num % 10 + suma_numeros(num // 10)


print(suma_numeros(23))
