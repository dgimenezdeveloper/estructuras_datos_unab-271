#8. **Combinaciones de un conjunto**: Escribe una función recursiva que genere todas las combinaciones posibles de un conjunto de elementos.


def combinaciones(conjunto):
    if len(conjunto) == 0:
        return [[]]
    else:
        resultado = []
        for combinacion in combinaciones(conjunto[1:]):
            resultado += [combinacion, [conjunto[0]] + combinacion]
        return resultado