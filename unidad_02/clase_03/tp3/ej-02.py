""" Realizar un programa que pida al usuario ingresar el nombre de un empleado, los años 
de antigüedad, el sueldo y el área de trabajo Por ejemplo: [ “Juan Pérez”, 14, 890000, “Contabilidad] 
El programa deberá mostrar el nuevo sueldo del empleado incrementado en un 15% """


def ingresar_empleado():
    empleados = []
    nom_ape = input("Ingresa el nombre y apellido del empleado - 0 para salir: ")
    while nom_ape != "0":
        antiguedad = int(input("Ingresa la antigüedad: "))
        sueldo = int(input("Ingresa el sueldo: "))
        area = input("Ingresa el área de trabajo: ")
        empleados.append([nom_ape, antiguedad, sueldo, area])
        nom_ape = input("Ingresa el nombre y apellido del empleado - 0 para salir: ")
    return empleados


def mostrar_aumento(empleados):
    for empleado in empleados:
        aumento = empleado[2] + empleado[2] * 0.15
        print(f"El sueldo del empleado {empleado[0]} será de {aumento}")


empleados = ingresar_empleado()
mostrar_aumento(empleados)
