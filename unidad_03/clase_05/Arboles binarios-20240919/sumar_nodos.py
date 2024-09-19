from tad_arbol import insertar_nodo,arbol_vacio,imprimir_arbol
from tad_cola import Cola,push,pop,cola_vacia

def sumar_nodos(raiz):
    #retorna la suma de los nodos del arbol
    if(raiz is None):
        return 0
    else:
        return raiz.informacion + sumar_nodos(raiz.izquierda) + sumar_nodos(raiz.derecha)

arbol_binario = insertar_nodo(None, 45)
arbol_binario  = insertar_nodo(arbol_binario , 11)
arbol_binario  = insertar_nodo(arbol_binario , 85)
arbol_binario  = insertar_nodo(arbol_binario , 1)
arbol_binario  = insertar_nodo(arbol_binario , 185)
arbol_binario  = insertar_nodo(arbol_binario , 121)
arbol_binario  = insertar_nodo(arbol_binario , 44)
imprimir_arbol(arbol_binario)
print("Suma de nodos: ",sumar_nodos(arbol_binario))
