#**Torres de Hanoi**: Escribe una función recursiva que resuelva el problema de las Torres de Hanoi.

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mover disco de {origen} a {destino}')
    else:
        hanoi(n-1, origen, auxiliar, destino)
        print(f'Mover disco de {origen} a {destino}')
        hanoi(n-1, auxiliar, destino, origen)