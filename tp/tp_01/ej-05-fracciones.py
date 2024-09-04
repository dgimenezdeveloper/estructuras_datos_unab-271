""" Vamos a definir una fracción que está representada por una lista de dos elementos, el 
numerador y el denominador. Por ejemplo la fracción ¾ seria la lista (3,4).  
a) Escribir un programa que sume dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
b) Escribir un programa que reste dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
c) Escribir un programa que multiplique dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. 
d) Escribir un programa que divida dos fracciones. Para ello el usuario deberá ingresar los datos de las dos fracciones por teclado. """

def sumar(fracc1, fracc2):
    return fracc1[0] + fracc2[0], fracc1[1] + fracc2[1]

def restar(fracc1, fracc2):
    return fracc1[0] - fracc2[0], fracc1[1] - fracc2[1]

def multiplicar(fracc1, fracc2):
    return fracc1[0] * fracc2[0], fracc1[1] * fracc2[1]

def dividir(fracc1, fracc2):
    return fracc1[0] * fracc2[1], fracc1[1] * fracc2[0]

def obtener_datos():
    num = int(input('Ingresa el numerador: '))
    den = int(input('Ingresa el denominador: '))
    return num,den

def main():
    fracc1 = obtener_datos()
    fracc2 = obtener_datos()
    
    suma = sumar(fracc1, fracc2)
    resta = restar(fracc1, fracc2)
    producto = multiplicar(fracc1, fracc2)
    division = dividir(fracc1, fracc2)
    
    print(f'Suma: {suma}')
    print(f'resta: {resta}')
    print(f'Producto: {producto}')
    print(f'División: {division}')

main()