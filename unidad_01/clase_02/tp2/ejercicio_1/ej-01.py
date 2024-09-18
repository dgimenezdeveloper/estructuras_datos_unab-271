def ingresar_alumnos():
    alumnos = []
    legajo = int(input("Ingrese el legajo del alumno (0 para terminar): "))
    while legajo != 0:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        contraseña = input("Ingrese la contraseña del alumno: ")
        alumnos.append([legajo, nombre, apellido, contraseña])
        legajo = int(input("Ingrese el legajo del alumno (0 para terminar): "))
    return alumnos


def imprimir_alumno(alumno):
    print("Legajo:", alumno[0])
    print("Nombre:", alumno[1])
    print("Apellido:", alumno[2])
    print("Contraseña:", alumno[3])


def legajo_menor(alumnos):
    menor = alumnos[0]
    for alumno in alumnos:
        if alumno[0] < menor[0]:
            menor = alumno
    return menor


def nombre_mas_largo(alumnos):
    largo = 0
    nombre = None
    for alumno in alumnos:
        if len(alumno[1]) > largo:
            largo = len(alumno[1])
            nombre = alumno[1]
    return nombre


def controlar_clave(alumno):
    if len(alumno[3]) > 6 and alumno[3][-1].isdigit():
        print(f"La contraseña de {alumno[1]} {alumno[2]} es válida")
    else:
        print(
            f"Error: La contraseña de {alumno[1]} {alumno[2]} no es válida: debe tener más de 6 caracteres y terminar en un número."
        )


def verificar_claves(alumnos):
    for alumno in alumnos:
        controlar_clave(alumno)


def imprimir_menu():
    print("\nMenú de Opciones:")
    print("1. Imprimir los datos de todos los alumnos")
    print("2. Imprimir los datos del alumno con el legajo más chico")
    print("3. Imprimir los datos del alumno con el nombre más largo")
    print("4. Verificar si las contraseñas cumplen con los requisitos")
    print("0. Salir\n")


def menu(alumnos):
    imprimir_menu()
    opcion = int(input("Ingrese una opción: "))
    while opcion != 0:
        if opcion == 1:
            for alumno in alumnos:
                imprimir_alumno(alumno)
        elif opcion == 2: 
            menor = legajo_menor(alumnos)
            imprimir_alumno(menor)
        elif opcion == 3:
            nombre = nombre_mas_largo(alumnos)
            print("El nombre más largo es:", nombre)
        elif opcion == 4:
            verificar_claves(alumnos)
        else:
            print("Opción incorrecta")
        imprimir_menu()
        opcion = int(input("Ingrese una opción: "))


def main():
    alumnos = ingresar_alumnos()
    menu(alumnos)

main()