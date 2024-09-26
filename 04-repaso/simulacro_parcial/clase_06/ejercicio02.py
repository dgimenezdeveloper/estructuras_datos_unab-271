"""2) (2 puntos) Implementar una función utilzando recursión para determinar si una lista contiene o no un determinado elemento. Alternativamente pueden utilizar una solución iterativa (1 punto) """


def existe_elemento(lista, elemento):
    if lista == []:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return existe_elemento(lista[1:], elemento)

def existe_elemnto1(lista, elemento):
    if lista == []:
        return False
    elif lista[-1] == elemento: # Se compara con el último elemento
        return True
    else:
        return existe_elemnto1(lista[:-1], elemento) # Se pasa la lista desde el inicio hasta el último sin incluirlo.

def existe_elemento_iterativo(lista, elemento):
    existe = False
    for i in lista:
        if i == elemento:
            existe = True
            return existe
    return existe

def existe_elemento_iterativo1(lista, elemento):
    existe = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            existe = True
            return existe
    return existe

def main():
    lista = [1, 3, 5, 7, 9]
    buscado = 2
    buscado1 = 9
    print("Usando la funcion existe_elemento()")
    print(existe_elemento(lista, buscado)) # False
    print(existe_elemento(lista, buscado1)) # True
    print()
    
    print("Usando la funcion existe_elemento1()")
    print(existe_elemnto1(lista, buscado))
    print(existe_elemnto1(lista, buscado1))
    print()
    
    print("Usando la funcion existe_elemento_iterativa()")
    print(existe_elemento_iterativo(lista, buscado))
    print(existe_elemento_iterativo(lista, buscado1))
    print()
    
    print(existe_elemento_iterativo1(lista, buscado))
    print(existe_elemento_iterativo1(lista, buscado1))
    print()
main()
