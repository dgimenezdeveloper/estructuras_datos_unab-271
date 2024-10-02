from tad_arbol import insertar_nodo,arbol_vacio,imprimir_arbol
from tad_cola import Cola,push,pop,cola_vacia

def contar_nodos(raiz):
    #retorna la cantidad de nodos del arbol
    if(raiz is None):
        return 0
    else:
        contador = 1
        contador += contar_nodos(raiz.hijo_izquierdo)
        contador += contar_nodos(raiz.hijo_derecho)
        return contador



arbol_binario = insertar_nodo(None, 45)
arbol_binario  = insertar_nodo(arbol_binario , 11)
arbol_binario  = insertar_nodo(arbol_binario , 85)
arbol_binario  = insertar_nodo(arbol_binario , 1)
arbol_binario  = insertar_nodo(arbol_binario , 185)
arbol_binario  = insertar_nodo(arbol_binario , 121)
arbol_binario  = insertar_nodo(arbol_binario , 44)
imprimir_arbol(arbol_binario)
print("Cantidad de nodos: ",contar_nodos(arbol_binario))