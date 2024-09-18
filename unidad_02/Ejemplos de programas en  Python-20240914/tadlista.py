class nodoLista(object):
	#clase nodo lista
	info,sig = None,None
	
class lista(object):
	#clase lista
	def __init__(self):
		#crea una lista vacia
		self.inicio = None
		self.tamaño = 0
def insertar(lista,dato):
		#inserta el dato en la lista de manera ordenada
		nodo = nodoLista()
		nodo.info = dato
		if(lista.inicio is None) or (lista.inicio.info > dato):
			#el dato nuevo es menor que los elementos insertados en la lista
			nodo.sig = lista.inicio
			lista.inicio = nodo #actualizo el comienzo de la lista			
		else:
			#recorrer la lista buscando donde insertar el elemento
			anterior = lista.inicio
			actual = lista.inicio.sig
			while(actual is not None) and (actual.info < dato):
				anterior = anterior.sig #anterior = actual
				actual = actual.sig
			anterior.sig = nodo
			nodo.sig = actual
		lista.tamaño = lista.tamaño+1 #actualizo la cantidad de elementos de la lista

def imprimir(lista):
	cantidad = 0
	actual = lista.inicio
	while(cantidad < lista.tamaño):
		print(actual.info)
		actual = actual.sig
		cantidad = cantidad +1

def eliminar(lista,valor):
	#si el valor se encuentra en la lista
	# elimina el elemento de la lista y lo retorna 
	dato = None
	if(lista.inicio.info == valor):
		dato = lista.inicio.info
		lista.inicio = lista.inicio.sig
		lista.tamaño = lista.tamaño -1
	else:
		 #recorremos la lista
		 anterior = lista.inicio
		 actual = lista.inicio.sig
		 while(actual is not None) and (actual.info != valor):
			 anterior = anterior.sig #anterior = actual
			 actual = actual.sig
		 if(actual is not None):
			 #suponemos que el elemento puede no existir en la lista
			 anterior.sig = actual.sig
			 dato = actual.sig.info
			 lista.tamaño = lista.tamaño -1
	return dato 
		
lista_enlazada = lista() #creamos la instancia 
insertar(lista_enlazada,8) #insertamos un dato
insertar(lista_enlazada,4) #insertamos otro dato
insertar(lista_enlazada,2) #insertamos y otro dato mas
imprimir(lista_enlazada)
eliminar(lista_enlazada,4)#eliminamos el segundo elemento de la lista
imprimir(lista_enlazada) #verificamos que la lista queda ordenada


	
