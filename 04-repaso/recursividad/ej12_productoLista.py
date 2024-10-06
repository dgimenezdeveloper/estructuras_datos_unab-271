# 12. **Producto de una lista**: Escribe una función recursiva que calcule el producto de todos los elementos en una lista.
def productoLista(lista):
    if not lista:
        return 1
    else:
        return lista[0] * productoLista(lista[1:])

print(productoLista([1,2,3]))