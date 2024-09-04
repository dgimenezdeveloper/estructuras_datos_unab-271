""" 
Se tiene Información de los Docentes de un Instituto de Enseñanza: 
Código de la Materia, Apellido del Docente, cantidad de alumnos inscriptos en la materia, cantidad de alumnos que aprobaron la materia.

Ejemplo:

Docentes= [ [ 121, “Perez”, 30, 3],  [121, “López”, 20, 20], [404, “Ronald”, 40,20] ,  [333,  “Gomez”, 50, 25], [ 333, “Dahan”, 10, 2]]

Realizar un programa que imprima, la siguiente lista:

[121,”Perez”,  10]  

[121,“Lopez”, 100]

[404, “Ronald” , 50]

[333, “Gomez”, 50]

[ 333, “Dahan”, 20 ]

El último dato corresponde al % de alumnos que aprobaron la materia.
"""
def obtener_porcentaje_aprobados(docente):
    return docente[3] * 100 / docente[2]

def main():
    docentes = [ [ 121, "Perez", 30, 3],  [121, "López", 20, 20], [404, "Ronald", 40,20] ,  [333,  "Gomez", 50, 25], [ 333, "Dahan", 10, 2]]
    for docente in docentes:
        print(f'[{docente[0]}, {docente[1]}, {obtener_porcentaje_aprobados(docente)}]')

main()