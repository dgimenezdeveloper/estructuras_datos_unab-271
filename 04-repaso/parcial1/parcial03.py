def listar_pares(arbol):
    pares = []
    if arbol is not None:
        listar_pares(arbol.izq)
        if arbol.elemento % 2 == 0:
            pares.append(arbol.elemento)
        listar_pares(arbol.der)
    return pares