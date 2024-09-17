""" Escribir  un  programa  que  calcule  el  área  de  un  triángulo.  Para  ello  el  usuario  deberá 
ingresar la base y la altura. """
def calcular_area(base, altura):
    return (base * altura)/2

def obtener_datos():
    base = float(input('Ingrese el valor de la base: '))
    altura = float(input('Ingrese el valor de la altura: '))
    return base, altura

def mostrar_area():
    b,a = obtener_datos()
    print(f'Área del Triángulo: {calcular_area(b, a)}')

def main():
    mostrar_area()

main()