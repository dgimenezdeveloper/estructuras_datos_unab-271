#estructura del TAD pila

class Nodo_pila(object):
	#clase nodo pila
	info = None
	siguiente = None

class Pila(object):
	#clase pila
	def __init__(self):
		#referencia al nodo que está en la cima de la pila
		self.cima = None 
		self.tamaño = 0 #pila sin datos

def apilar(pila,dato):
	#agrego el dato en la pila actualizando los punteros
	nodo = Nodo_pila() #creo el nodo
	nodo.info = dato #agrego al nodo los datos 
	nodo.siguiente = pila.cima #actualizo el puntero
	pila.cima = nodo #actualizo la cima
	pila.tamaño = pila.tamaño+1
	
def desapilar(pila):
	#elimino el elemento de la cima de la pila
	nodo = pila.cima #guardo el elemento a sacar
	pila.cima = nodo.siguiente #actualizo el elemento de la cima
	pila.tamaño = pila.tamaño-1 #actualizo el tamaño
	return nodo
	
def recorrer_pila(pila):
	print("recorremos la pila")
	pila_auxiliar = Pila()
	i = 0
	j = pila.tamaño
	while(i < j):
		print(i)
		elemento = desapilar(pila)
		imprimir_nodo(elemento)
		apilar(pila_auxiliar,elemento.info)
		i = i+1
	#volvemos a cargar los datos en la pila
	i = 0
	while(i < j):
		elemento = desapilar(pila_auxiliar)
		#imprimir_nodo(elemento)
		apilar(pila,elemento.info)
		i = i+1
		
def imprimir_nodo(nodo):
	print(nodo.info)
	
#programa principal
mi_pila = Pila()
apilar(mi_pila,25)
apilar(mi_pila,15)
apilar(mi_pila,2)
apilar(mi_pila,33)
apilar(mi_pila,525)
apilar(mi_pila,115)
apilar(mi_pila,12)
apilar(mi_pila,133)
dato = desapilar(mi_pila)
imprimir_nodo(dato)
recorrer_pila(mi_pila)

