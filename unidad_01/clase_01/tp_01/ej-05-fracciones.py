""" Vamos a definir una fracción que está representada por una lista de dos elementos, el 
numerador y el denominador. Por ejemplo la fracción ¾ seria la lista (3,4).  
a) Escribir un programa que sume dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
b) Escribir un programa que reste dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
c) Escribir un programa que multiplique dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
d) Escribir un programa que divida dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. """
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def sumar(self, fraccion):
        return self.num * fraccion.den + fraccion.num * self.den, self.den * fraccion.den

    def restar(self, fraccion):
        return self.num * fraccion.den - fraccion.num * self.den, self.den * fraccion.den

    def multiplicar(self, fraccion):
        return self.num * fraccion.num, self.den * fraccion.den

    def dividir(self, fraccion):
        return self.num * fraccion.den, self.den * fraccion.num

    def __str__(self):
        return f'{self.num}/{self.den}'

def obtener_datos():
    num = int(input('Ingresa el numerador: '))
    den = int(input('Ingresa el denominador: '))
    return num,den

def main():
    num1, den1 = obtener_datos()
    num2, den2 = obtener_datos()
    fraccion1 = Fraccion(num1, den1)
    fraccion2 = Fraccion(num2, den2)
    print(f'La suma de las fracciones es: {fraccion1.sumar(fraccion2)}')
    print(f'La resta de las fracciones es: {fraccion1.restar(fraccion2)}')
    print(f'La multiplicación de las fracciones es: {fraccion1.multiplicar(fraccion2)}')
    print(f'La división de las fracciones es: {fraccion1.dividir(fraccion2)}')

main()