class NodoCola(object):
	#clase nodo cola
	info = None
	siguiente = None

class Cola(object):
	#clase cola
	def __init__(self):
		#crea una cola vacia
		self.frente = None
		self.final = None
		self.tamaño = 0
		
def push(cola,dato):
	#agrega el elemento en la cola
	nodo = NodoCola()#creo el nodo
	nodo.info = dato #agrego el dato
	if(cola.frente == None):#si la cola esta vacia
		cola.frente = nodo #actualizo
	else:
		cola.final.siguiente = nodo #actualizo el punterodel siguiente
	cola.final = nodo #ahora el nodo agregado nos indica el final
	cola.tamaño = cola.tamaño+1 #actualizo el tamaño de la cola

def pop(cola):
	#saco un elemento de la cola
	dato = cola.frente.info #saco el elemento
	cola.frente = cola.frente.siguiente #actualizo el frente
	if (cola.frente == None):
		cola.final = None #se quedo sin elementos
	cola.tamaño = cola.tamaño -1
	return dato
	
def imprimir_cola(cola):
	i = 0
	elemento = cola.frente
	while(i < cola.tamaño):
		print(elemento.info)
		elemento = elemento.siguiente
		i = i +1
		
#programa principal
mi_cola = Cola()
push(mi_cola,25)
push(mi_cola,30)
push(mi_cola,2)
push(mi_cola,78)
imprimir_cola(mi_cola)
dato = pop(mi_cola)
print("sin el elemento")
imprimir_cola(mi_cola)


	
		
	
