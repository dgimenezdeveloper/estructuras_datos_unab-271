""" 
Se tiene la siguiente lista [7, 8, 5, 9, 8, 6, 7, 7, 9, 11, 10]. 
Se puede utilizar funciones en la resolución.

Realizar un programa que muestre  la cantidad de números pares.

Realizar un programa que muestre el promedio de todos los números de la lista.
"""

class ListaNumeros:
    """
    Inicializa un objeto ListaNumeros con una lista de números.
        :param numeros: La lista de números.
    """
    def __init__(self, numeros):
        self.numeros = numeros
    
    def contar_pares(self):
        """ 
        Cuenta la cantidad de números pares en la lista.
            :return: La cantidad de números pares.
        """
        return len([numero for numero in self.numeros if numero % 2 == 0])
    
    def calcular_promedio(self):
        """ 
        Calcula el promedio de los números en la lista.
            :return: El promedio de los números en la lista.
        """
        return sum(self.numeros) / len(self.numeros)

def obtener_datos():
    """ Solicita al usuario los números para crear una lista de números
            :return: una lista de números.
    """
    while True:
        try:
            numeros = [int(numero) for numero in input('Ingrese los números separados por coma: ').split(',')]
            return numeros
        except ValueError:
            print('El valor ingresado no es válido. Intente nuevamente')

def mostrar_resultados():
    """ Llama a las funciones necesarias para mostrar los resultados de la lista de números """
    numeros = obtener_datos()
    if numeros:
        lista_numeros = ListaNumeros(numeros)
        print(f'La cantidad de números pares es: {lista_numeros.contar_pares()}')
        print(f'El promedio de los números es: {lista_numeros.calcular_promedio()}')

if __name__ == '__main__':
    mostrar_resultados()