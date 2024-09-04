""" Escribir  un  programa  que  calcule  el  perímetro  de  un  triángulo.  Para  ello  el  usuario 
deberá ingresar los lados del triángulo """
def calcular_perimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def obtener_datos():
    l1 = float(input('Ingresa el valor del lado 1: '))
    l2 = float(input('Ingresa el valor del lado 2: '))
    l3 = float(input('Ingresa el valor del lado 3: '))
    lados = (l1, l2, l3)
    return lados

def main():
    lad1, lad2, lad3 = obtener_datos()
    perimetro = calcular_perimetro(lad1, lad2, lad3)
    print(f'Perímetro del triángulo: {perimetro}')

if __name__ == '__main__':
    main()