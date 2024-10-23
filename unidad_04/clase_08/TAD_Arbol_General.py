class Arbol_General(object):
	#clase nodo arbol
	def __init__(self,info):
		self.info = info
		self.sig = None #lista donde guarda todos sus hijos
		self.hijos = None#sin hijos
		
def arbol_vacio(raiz):
	#retorna si el arbol esta vacio
	return raiz == None
	
def agregar_hijo_raiz(raiz,info):
	#inserto el dato en el arbol
	if arbol_vacio(raiz):
		raiz = Arbol_General(info)
		#referencio el comienzo de la lista
	else:
		raiz = agregar_nodo(raiz,info)
	return raiz #una vez actualizado el dato se retorna la raiz
	
def agregar_nodo(raiz,info):
	nodo = Arbol_General(info)
	if(raiz.hijos is None):
			#no tiene hijos
			raiz.hijos = nodo 
	else:
		anterior = raiz.hijos
		actual = raiz.hijos.sig
		while (actual is not None):
			anterior = anterior.sig #anterior = actual
			actual = actual.sig
		anterior.sig = nodo
		nodo.sig = actual
	return raiz
	
def agregar_hijo_nodo(raiz,nodo,info):	
		if not arbol_vacio(raiz):
			anterior = raiz.hijos
			actual = raiz.hijos.sig
			ok = False
			while (actual is not None) and (not ok):
				if anterior.info == nodo:
					ok = True
				else:
					anterior = anterior.sig #anterior = actual
					actual = actual.sig
			if ok:
				nodo = agregar_nodo(anterior,info)					
			anterior.sig = nodo
			nodo.sig = actual
		return raiz

def preorden(raiz):
	if(raiz is not None):
		print(raiz.info)
		hijos = raiz.hijos
		while(hijos is not  None):
			preorden(hijos)
			hijos = hijos.sig
def postorden(raiz):
	if(raiz is not None):
		hijos = raiz.hijos
		while(hijos is not  None):
			postorden(hijos)
			hijos = hijos.sig
		print(raiz.info)			

#def por_niveles(raiz):
	#encolar(raiz)
	#mientras la cola no este vacia
	#desencolamos v
	#imprimimos dato de v
	#para cada hijo de v
	#encolar (hijo)
			
dato = input("Ingrese dato: ")
ag = agregar_hijo_raiz(None,dato)#raiz
for i in range(4):
	dato = input("Ingrese dato: ")
	ag = agregar_hijo_raiz(ag,dato)
dato = input("Ingrese dato del nodo Padre: ")
dato1 = input("Ingrese dato del nodo hijo: ")
ag = agregar_hijo_nodo(ag,dato,dato1)
dato = input("Ingrese dato del nodo Padre: ")
dato1 = input("Ingrese dato del nodo hijo: ")
ag = agregar_hijo_nodo(ag,dato,dato1)
dato = input("Ingrese dato del nodo Padre: ")
dato1 = input("Ingrese dato del nodo hijo: ")
ag = agregar_hijo_nodo(ag,dato,dato1)
preorden(ag)
postorden(ag)
#por_niveles(ag)

