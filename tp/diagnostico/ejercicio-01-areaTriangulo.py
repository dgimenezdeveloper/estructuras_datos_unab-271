""" 
Escribir una función llamada area que calcule el área  de un triángulo. 
La función deberá recibir como parámetros la base y la altura del triángulo.

Escribir un programa que calcule el área de un triángulo. EL usuario deberá ingresar la base y la altura por teclado.
"""

class Triangulo:
    """
    Inicializa un objeto Triangulo con base y altura.
        :param base: La base del triángulo.
        :param altura: La altura del triángulo.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        """ 
        Calcula el área del triángulo.
            :return: El área del triángulo.
        """
        return (self.base * self.altura) / 2

def obtener_datos():
    """ Solicita al usuario la base y la altura para calcular el área de un triángulo
            :return: una tupla con la base y la altura.
    """
    while True:
        try:
            base = float(input('Ingrese la base del triángulo: '))
            altura = float(input('Ingrese la altura del triángulo: '))
            if base <= 0 or altura <= 0:
                raise ValueError('La base y la altura deben ser mayores a cero')
                continue
            return base, altura
        except ValueError:
            print('El valor ingresado no es válido. Intente nuevamente')

def calcular_area():
    """ Llama a las funciones necesarias para calcular el área de un triángulo """
    base, altura = obtener_datos()
    if base and altura:
        triangulo = Triangulo(base, altura)
        print(f'El área del triángulo es: {triangulo.area()}')

if __name__ == '__main__':
    calcular_area()