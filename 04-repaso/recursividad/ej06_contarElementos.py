#6. **Conteo de elementos en una lista**: Escribe una función recursiva que cuente el número de elementos en una lista.

l = [1,2,3]
def contar_elementos(lista):
    if not lista:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])


print(contar_elementos(l))