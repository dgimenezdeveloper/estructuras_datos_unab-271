#estructura del nodo arbol
class nodo_arbol(object):
	#clase nodo arbol
	def __init__(self,info):
		#crea un nodo con la informacion cargada
		self.info = info
		self.izq = None
		self.der =None
		
def arbol_vacio(raiz):
	#retorna si el arbol esta vacio
	return raiz == None
		
def insertar_nodo(raiz,dato):
	#inserto el dato en el arbol
	if arbol_vacio(raiz):
		raiz = nodo_arbol(dato)
	elif(raiz.info <= dato):
		raiz.der = insertar_nodo(raiz.der,dato)
	else:
		raiz.izq = insertar_nodo(raiz.izq,dato)
	#una vez actualizado el dato se retorna la raiz
	return raiz	
	
def imprimir_arbol(raiz):
	if arbol_vacio(raiz):
		print("-")
	else:
		print(raiz.info)
		imprimir_arbol(raiz.der)
		imprimir_arbol(raiz.izq)
	
arbol= insertar_nodo(None, 45)
arbol = insertar_nodo(arbol, 11)
arbol = insertar_nodo(arbol, 85)
imprimir_arbol(arbol)	
