""" 
Realizar un  programa que  imprima los apellidos de las personas que no pagarán el
impuesto de patente.  Tener en cuenta que los autos cuyas patentes empiezan con R, S y T no pagan
impuestos
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


##################### EJERCICIO 8 ########################
# MODULARIZADA #
def es_exento(patente):
    return patente.upper().startswith('R') or patente.upper().startswith('S') or patente.upper().startswith('T')

def imprimir_exentos(patentes):
	for patente in patentes:
		if es_exento(patente['patente']):
			print(f'Apellido: {patente['apellido']}')
   
##########################################################
def main():
    patentes = obtener_datos()
    mostrar(patentes)
    imprimir_exentos(patentes)

main()