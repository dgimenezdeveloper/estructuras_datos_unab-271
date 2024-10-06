# 13. **Número de ocurrencias**: Escribe una función recursiva que cuente el número de veces que un elemento aparece en una lista.
def ocurrencias(lista, num):
    if not lista:
        return 0
    elif lista[0] == num:
        return  1 + ocurrencias(lista[1:], num)
    else:
        return ocurrencias(lista[1:], num)