from tad_arbol import insertar_nodo,arbol_vacio,imprimir_arbol
from tad_cola import Cola,push,pop,cola_vacia

def buscar_nodo(raiz,dato):
    #busca un nodo en el arbol
    if(raiz is None):
        return False
    elif(raiz.informacion == dato):
        return True
    elif(raiz.informacion < dato):
        return buscar_nodo(raiz.derecha,dato)
    else:
        return buscar_nodo(raiz.izquierda,dato)

arbol_binario = insertar_nodo(None, 45)
arbol_binario  = insertar_nodo(arbol_binario , 11)
arbol_binario  = insertar_nodo(arbol_binario , 85)
arbol_binario  = insertar_nodo(arbol_binario , 1)
arbol_binario  = insertar_nodo(arbol_binario , 185)
arbol_binario  = insertar_nodo(arbol_binario , 121)
arbol_binario  = insertar_nodo(arbol_binario , 44)
imprimir_arbol(arbol_binario)
print("Buscar nodo 44: ",buscar_nodo(arbol_binario,44))
print("Buscar nodo 100: ",buscar_nodo(arbol_binario,100))
print("Buscar nodo 1: ",buscar_nodo(arbol_binario,1))
print("Buscar nodo 121: ",buscar_nodo(arbol_binario,121))
print("Buscar nodo 185: ",buscar_nodo(arbol_binario,185))
print("Buscar nodo 85: ",buscar_nodo(arbol_binario,85))