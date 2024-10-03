from tad_arbol import insertar_nodo,arbol_vacio,imprimir_arbol
from tad_cola import Cola,push,pop,cola_vacia

def por_nivel(raiz):
	#recorre el arbol por niveles 
	pendientes = Cola()
	push(pendientes,raiz)
	while(not cola_vacia(pendientes)):
		nodo = pop(pendientes)
		print(nodo.info)
		if(nodo.izq is not None):
			push(pendientes,nodo.izq)
		if(nodo.der is not None):
			push(pendientes,nodo.der)

def inorden(raiz):
	#realiza el recorrido en orden del arbol
	if(raiz is not None):
		inorden(raiz.izq)
		print(raiz.info)
		inorden(raiz.der)
		
def preorden(raiz):
	#realiza el recorrido preorden del arbol
	if(raiz is not None):
		print(raiz.info)
		preorden(raiz.izq)
		preorden(raiz.der)
		
		
def postorden(raiz):
	#realiza el recorrido postorden del arbol
	if(raiz is not None):
		postorden(raiz.der)
		print(raiz.info)
		postorden(raiz.izq)

arbol_binario = insertar_nodo(None, 45)
arbol_binario  = insertar_nodo(arbol_binario , 11)
arbol_binario  = insertar_nodo(arbol_binario , 85)
arbol_binario  = insertar_nodo(arbol_binario , 1)
arbol_binario  = insertar_nodo(arbol_binario , 185)
arbol_binario  = insertar_nodo(arbol_binario , 121)
arbol_binario  = insertar_nodo(arbol_binario , 44)
#imprimir_arbol(arbol_binario)
print("Recorrido por niveles: ")
por_nivel(arbol_binario)
print("Recorrido InOrden: ")
inorden(arbol_binario)
print("Recorrido PreOrden: ")
preorden(arbol_binario)
print("Recorrido PostOrden: ")
postorden(arbol_binario)
		
