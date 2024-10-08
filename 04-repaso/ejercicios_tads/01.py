""" Utilizando TADs se deberá representar y programar la siguiente información:
Definir el tad alumno, de cada alumno se conoce legajo, nombre, apellido, contraseña.
Definir el tad facultad que tiene, nombre, alumnos, cantidad de alumnos
a) Realice una función que procesa la información de alumnos de la UNAB. De cada alumno se
conoce legajo, nombre, apellido, contraseña. El procesamiento termina cuando se ingresa el
número de legajo 0. La función deberá retornar la facultad creada con los alumnos.
b) Realice una función llamada imprimir_alumnos que recibe como parámetro una facultad
e imprime por pantalla los datos de la facultad:
c) Realice una función llamada legajo_menor que recibe como parámetro una facultad, la
función debe buscar cuál es el alumno con el menor legajo dentro de la facultad y retornarlo.
Resolver la práctica aplicando los siguientes conceptos cuando sea necesario:
d) Realice una función llamada nombre_mas_largo que recibe como parámetro una facultad y
retorna el nombre más largo entre los alumnos.
e) Realice una función llamada controlar_clave que recibe como parámetro una facultad y
retorna los alumnos que no cumplen con las pautas de una contraseña segura. La función debe
controlar si la contraseña es mayor a 6 caracteres y termina con un número, deberá imprimir
un mensaje especificando el error cometido en caso de no cumplir las condiciones o bien
imprimir los datos del alumno si la clave cumple con todas las condiciones.
Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir del
menú,
el resto de las opciones permiten:
- imprimir los datos de todos los alumnos con el formato pedido en el punto a)
- imprimir los datos del alumno que tiene el legajo más chico.
- imprimir los datos del alumno que tiene el nombre más largo.
- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6
caracteres y terminan con un número. """

class Alumno:
    def __init__(self, leg, nom, ape, clave):
        self.leg = leg
        self.nom = nom
        self.ape = ape
        self.clave = clave
    
    def __str__(self):
        return  f"Legajo: {self.leg}, Nombre: {self.nom}, Apellido: {self.ape}\n"
class Facultad:
    def __init__(self, nombre, alumnos = [], cant_alumnos = 0):
        self.nombre = nombre
        self.alumnos = alumnos
        self.cant_alumnos = cant_alumnos
    
    def __str__(self):
        return f'La  facultad {self.nombre} tiene {self.cant_alumnos} alumnos.'
    
""" Realice una función que procesa la información de alumnos de la UNAB. De cada alumno se
conoce legajo, nombre, apellido, contraseña. El procesamiento termina cuando se ingresa el
número de legajo 0. La función deberá retornar la facultad creada con los alumnos. """
def procesar_alumnos():
    facultad = Facultad("UNAB")
    leg = int(input("Ingrese el legajo del alumno: "))
    while leg != 0:
        nom = input("Ingrese el nombre del alumno: ")
        ape = input("Ingrese el apellido del alumno: ")
        clave = input('Ingrese la contraseña del alumno: ')
        facultad.alumnos.append(Alumno(leg,nom, ape, clave))
        facultad.cant_alumnos  += 1
        leg = int(input("Ingrese el legajo del alumno: "))
    return facultad

""" Realice una función llamada imprimir_alumnos que recibe como parámetro una facultad
e imprime por pantalla los datos de la facultad: """
#facultad1 = Facultad('UNAB',[(12,'Daro','gmnz','asdf'), (123,'vic','gmnz','asdf')] , 12)
def imprimir_alumnos(facultad):
    print(facultad)
    print(f'Listado de Alumnos:')
    for alumno in facultad.alumnos:
        print(alumno)

""" Realice una función llamada legajo_menor que recibe como parámetro una facultad, la
función debe buscar cuál es el alumno con el menor legajo dentro de la facultad y retornarlo. """
def legajo_menor(facultad):
    menor = facultad.alumnos[0]
    for alumno in facultad.alumnos:
        if alumno.leg < menor.leg:
            menor = alumno
    return menor

""" Realice una función llamada nombre_mas_largo que recibe como parámetro una facultad y
retorna el nombre más largo entre los alumnos. """
def nombre_mas_largo(facultad):
    largo = facultad.alumnos[0]
    for alumno in facultad.alumnos:
        if len(alumno.nom) > len(largo.nom):
            largo = alumno
    return largo

""" Realice una función llamada controlar_clave que recibe como parámetro una facultad y
retorna los alumnos que no cumplen con las pautas de una contraseña segura. La función debe
controlar si la contraseña es mayor a 6 caracteres y termina con un número, deberá imprimir
un mensaje especificando el error cometido en caso de no cumplir las condiciones o bien
imprimir los datos del alumno si la clave cumple con todas las condiciones. """
def controlar_clave(facultad):
    for alumno in facultad.alumnos:
        if len(alumno.clave) <= 6:
            print(f'La contraseña de {alumno.ape},  {alumno.nom} debe ser mayor a 6 caracteres.')
        elif  not alumno.clave[-1].isdigit():
            print(f'La contraseña de {alumno.ape},  {alumno.nom} no termina con un número.')
        else:
            print('\nAlumnos:')
            print(alumno)


""" Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir del
menú,
el resto de las opciones permiten:
- imprimir los datos de todos los alumnos con el formato pedido en el punto a)
- imprimir los datos del alumno que tiene el legajo más chico.
- imprimir los datos del alumno que tiene el nombre más largo.
- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6
caracteres y terminan con un número """

def mostrar_menu():
    print('1. Imprimir los datos de todos los alumnos')
    print('2. Imprimir los datos del alumno que tiene el legajo más chico')
    print('3. Imprimir los datos del alumno que tiene el nombre más largo')
    print('4. Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número')
    print('0. Salir')
    opcion = int(input('Ingrese una opción: '))
    return opcion

def main():
    facultad = procesar_alumnos()
    opcion = mostrar_menu()
    while opcion != 0:
        if opcion == 1:
            imprimir_alumnos(facultad)
        elif opcion == 2:
            print(legajo_menor(facultad))
        elif opcion == 3:
            print(nombre_mas_largo(facultad))
        elif opcion == 4:
            controlar_clave(facultad)
        else:
            print('Opción incorrecta')
        opcion = mostrar_menu()
    print('Fin del programa')

main()