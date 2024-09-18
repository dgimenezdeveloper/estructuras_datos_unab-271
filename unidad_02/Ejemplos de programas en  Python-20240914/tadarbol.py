#estructura del nodo arbol
class nodo_arbol(object):
	#clase nodo arbol
	def __init__(self,info):
		#crea un nodo con la informacion cargada
		self.izquierda = None
		self.derecha =None
		self.informacion = info
		
def arbol_vacio(raiz):
	#retorna si el arbol esta vacio
	return raiz == None
		
def insertar_nodo(raiz,dato):
	#inserto el dato en el arbol
	if arbol_vacio(raiz):
		raiz = nodo_arbol(dato)
	elif(raiz.informacion <= dato): 
		raiz.derecha = insertar_nodo(raiz.derecha,dato)
	else:
		raiz.izquierda = insertar_nodo(raiz.izquierda,dato)
	#una vez actualizado el dato se retorna la raiz
	return raiz	
	
def imprimir_arbol(raiz):
	if arbol_vacio(raiz):
		print("-")
	else:
		print(raiz.informacion)
		imprimir_arbol(raiz.derecha)
		imprimir_arbol(raiz.izquierda)
	
arbol= insertar_nodo(None, 45)
arbol = insertar_nodo(arbol, 11)
arbol = insertar_nodo(arbol, 85)
imprimir_arbol(arbol)	