#11. **Suma de una lista**: Escribe una función recursiva que calcule la suma de todos los elementos en una lista

def sumaLista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumaLista(lista[1:])