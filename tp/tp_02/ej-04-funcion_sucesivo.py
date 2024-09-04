""" Definir una función recursiva que imprime los números sucesivos desde n hasta 10. Por
ejemplo funcion_sucesivo (6) Imprimirá: 6,7,8,9,10 """

def funcion_sucesivo(n):
    if n == 10:
        print(n)
    else:
        print(f'{n},', end='') 
        funcion_sucesivo(n + 1)

def main():
    funcion_sucesivo(6)

main()