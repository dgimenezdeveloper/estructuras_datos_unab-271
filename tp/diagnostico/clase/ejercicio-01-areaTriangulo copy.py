""" 
Escribir una función llamada area que calcule el área  de un triángulo. 
La función deberá recibir como parámetros la base y la altura del triángulo.

Escribir un programa que calcule el área de un triángulo. EL usuario deberá ingresar la base y la altura por teclado.
"""
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def obtener_datos():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura

def main():
    base, altura = obtener_datos()
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")