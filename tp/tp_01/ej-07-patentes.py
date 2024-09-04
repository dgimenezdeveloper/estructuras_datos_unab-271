""" 
Escriba  un  programa  que  ingrese  datos  de  patentes.  El  usuario  deberá  ingresar  la
cantidad de datos a ingresar.  Los datos de patente son: Nombre, Apellido, fecha de Inscripción,
patente.
"""

def obtener_datos():
    patentes = []
    cantidad = int(input('Ingrese la cantidad de patentes a registrar: '))
    while cantidad>0:
        nombre = input('Ingrese el Nombre: ')
        apellido = input('Ingrese el Apellido: ')
        fecha_inscripcion = input('Ingrese el fecha de inscripción (DD-MM-AAAA): ')
        patente = input('Ingrese el patente: ')
        patentes.append({'nombre': nombre, 'apellido': apellido, 'fecha_inscripcion': fecha_inscripcion, 'patente': patente})
        cantidad -=1
    return patentes

def mostrar(patentes):
    for patente in patentes:
        print(f"{patente['nombre']} {patente['apellido']} - Patente: {patente['patente']} - Fecha de inscripción: {patente['fecha_inscripcion']}")

def main():
    patentes = obtener_datos()
    mostrar(patentes)