"""  
Ejercicio 2 

Nos contratan para realizar un sistema para una editorial. Se recibe un texto por teclado y se desea 
obtener la siguiente información, para esto deberá construir un menú que permita ingresar las 
diferentes opciones: (RESOLVER CADA PUNTO CON UNA FUNCION): 
- La longitud total del texto. 
- La cantidad de palabras componen el texto. 
- La cantidad de oraciones que componen el texto. 
- La cantidad de palabras que comienzan con vocal o con consonante, dependiendo del 
valor ingresado por el usuario. 
- Buscar una palabra ingresada por el usuario y retornar la cantidad de veces que se 
encuentra en el texto. 
- La cantidad de palabras que comienzan con mayúscula. 
- La cantidad de caracteres que son números. 
- La cantidad de palabras que comienzan con vocal y la cantidad de palabras que 
comienzan con consonante. 
- Imprimir todas las palabras que terminan en infinitivo (terminadas en ar er o ir). 
"""

def imprimir_menu():
    print("\nMenú de Opciones:")
    print("1. Longitud total del texto")
    print("2. Cantidad de palabras del texto")
    print("3. Cantidad de oraciones del texto")
    print("4. Cantidad de palabras que comienzan con vocal o consonante")
    print("5. Buscar una palabra ingresada por el usuario")
    print("6. Cantidad de palabras que comienzan con mayúscula")
    print("7. Cantidad de caracteres que son números")
    print("8. Cantidad de palabras que comienzan con vocal y consonante")
    print("9. Imprimir todas las palabras que terminan en infinitivo")
    print("0. Salir\n")

def longitud_total(texto):
    return len(texto)

def cantidad_palabras(texto):
    return len(texto.split())



def cantidad_oraciones(texto):
    oraciones = texto.split()
    oraciones = [oracion for oracion in oraciones if oracion.strip()]
    return len(oraciones)

def cantidad_vocal_consonante_letra(texto, letra):
    palabras = texto.split()
    vocal = 0
    consonante = 0
    for palabra in palabras:
        if palabra[0].lower() == letra:
            vocal += 1
        else:
            consonante += 1
    return vocal, consonante

def buscar_palabra(texto, palabra):
    return texto.count(palabra)

def cantidad_palabras_mayuscula(texto):
    palabras = texto.split()
    mayuscula = 0
    for palabra in palabras:
        if palabra[0].isupper():
            mayuscula += 1
    return mayuscula

def cantidad_numeros(texto):
    numeros = '0123456789'
    suma = 0
    for caracter in texto:
        if caracter in numeros:
            suma += 1
    return suma

def cantidad_palabras_vocal_consonante(texto):
    palabras = texto.split()
    vocal = 0
    consonante = 0
    vocales = 'aeiou'
    for palabra in palabras:
        if palabra[0].lower() in vocales:
            vocal += 1
        else:
            consonante += 1
    return vocal, consonante

def palabras_infinitivo(texto):
    palabras = texto.split()
    infinitivo = []
    for palabra in palabras:
        if palabra.endswith('ar'):
            infinitivo.append(palabra)
        elif palabra.endswith('er'):
            infinitivo.append(palabra)
        elif palabra.endswith('ir'):
            infinitivo.append(palabra)
    return infinitivo

def procesar_opcion(opcion, texto):
    if opcion == 1:
        print("Longitud total del texto:", longitud_total(texto))
    elif opcion == 2:
        print("Cantidad de palabras del texto:", cantidad_palabras(texto))
    elif opcion == 3:
        print("Cantidad de oraciones del texto:", cantidad_oraciones(texto))
    elif opcion == 4:
        letra = input("Ingrese una letra: ")
        vocal, consonante = cantidad_vocal_consonante_letra(texto, letra)
        print(f"Cantidad de palabras que comienzan con vocal: {vocal}")
        print(f"Cantidad de palabras que comienzan con consonante: {consonante}")
    elif opcion == 5:
        palabra = input("Ingrese una palabra: ")
        print(f"La palabra {palabra} aparece {buscar_palabra(texto, palabra)} veces en el texto")
    elif opcion == 6:
        print("Cantidad de palabras que comienzan con mayúscula:", cantidad_palabras_mayuscula(texto))
    elif opcion == 7:
        print("Cantidad de caracteres que son números:", cantidad_numeros(texto))
    elif opcion == 8:
        vocal, consonante = cantidad_palabras_vocal_consonante(texto)
        print(f"Cantidad de palabras que comienzan con vocal: {vocal}")
        print(f"Cantidad de palabras que comienzan con consonante: {consonante}")
    elif opcion == 9:
        print("Palabras que terminan en infinitivo:", palabras_infinitivo(texto))

def main():
    #texto = input("Ingrese un texto: ")
    texto = 'Hola buenas! Esto es EDD. UNAB! Universidad'
    imprimir_menu()
    opcion = int(input("Ingrese una opción (0 para salir): "))
    while opcion != 0:
        procesar_opcion(opcion, texto)
        opcion = int(input("Ingrese una opción: "))
    print("Fin del programa")
    
main()

###############################################33

""" 
# Definiciones de las funciones
#- La longitud total del texto.
def longitud(texto):
    return len(texto)

def cantidad_palabras(texto):
    # Obtengo una lista interna separando (split) el texto a través del espacio en blanco
    lista = texto.split(' ')
    return len(lista)

# - La cantidad de oraciones que componen el texto.
def cantidad_oraciones(texto):
    cont = 0
    # Incremento el contador para el caso en el que el texto no esta bien terminado
    if not(texto[-1] in ['.', '!', '?']):
        texto = texto + '.'

    # Recorre el texto y pregunto por el caracter si es uno de los buscados
    for c in texto:
        if c in ['.', '!', '?']:
            cont = cont + 1

    return cont

def imprimir_menu():
    print()
    print('Menú')
    print('1. Longitud del texto')
    print('2. Cantidad de palabras')
    print('3. Cantidad de oraciones')
    print('4. Finalizar')

# programa
t = input('Ingrese un texto: ')
#t = "Hola buenas! Esto es EDD. UNAB! Universidad"

imprimir_menu()

opcion = int(input('Ingrese una opción: '))
while opcion != 4:
    if opcion == 1:
        a = longitud(t)
        print('Longitud', a)
    elif opcion == 2:
        b = cantidad_palabras(t)
        print('Cantidad de palabras', b)
    elif opcion == 3:
        c = cantidad_oraciones(t)
        print('Cantidad de oraciones', c)
    else:
        print('Ha ingresado una opción incorrecta.')    
    
    imprimir_menu()    
    opcion = int(input('Ingrese una opción: '))

print('Gracias por usar nuestro software!') 
"""