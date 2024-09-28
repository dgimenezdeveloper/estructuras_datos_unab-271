""" 1. **Factorial de un número**: Escribe una función recursiva que calcule el factorial de un número dado. """
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))