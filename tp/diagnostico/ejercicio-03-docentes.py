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
class Docente:
    """
    Inicializa un objeto Docente con el código de la materia, el apellido del docente, la cantidad de alumnos inscriptos y la cantidad de alumnos que aprobaron la materia.
        :param codigo_materia: El código de la materia.
        :param apellido: El apellido del docente.
        :param alumnos_inscriptos: La cantidad de alumnos inscriptos en la materia.
        :param alumnos_aprobados: La cantidad de alumnos que aprobaron la materia.
    """
    def __init__(self, cod_materia, ape_docente, cant_inscriptos, cant_aprobados):
        self.codigo_materia = cod_materia
        self.apellido = ape_docente
        self.cant_inscriptos = cant_inscriptos
        self.cant_aprobados = cant_aprobados
    
    def calcular_porcentaje_aprobados(self):
        """ 
        Calcula el porcentaje de alumnos que aprobaron la materia.
            :return: El porcentaje de alumnos que aprobaron la materia.
        """
        if self.cant_inscriptos == 0:
            return 0
        return int((self.cant_aprobados / self.cant_inscriptos) * 100)
    
    def obtener_informacion(self):
        """ 
        Obtiene la información del docente.
            :return: Una lista con el código de la materia, el apellido del docente y el porcentaje de alumnos que aprobaron la materia.
        """
        return [self.codigo_materia, self.apellido, self.calcular_porcentaje_aprobados()]
    
def obtener_datos():
    """ Solicita al usuario los datos de los docentes para crear una lista de docentes
            :return: una lista de docentes.
    """
    docentes = []
    while True:
        try:
            cantidad_docentes = int(input('Ingrese la cantidad de docentes: '))
            for _ in range(cantidad_docentes):
                cod_materia = int(input('Ingrese el código de la materia: '))
                apellido = input('Ingrese el apellido del docente: ')
                cant_inscriptos = int(input('Ingrese la cantidad de alumnos inscriptos: '))
                cant_aprobados = int(input('Ingrese la cantidad de alumnos que aprobaron: '))
                docente = Docente(cod_materia, apellido, cant_inscriptos, cant_aprobados)
                docentes.append(docente)
            return docentes
        except ValueError:
            print('El valor ingresado no es válido. Intente nuevamente')

def mostrar_resultados():
    """ Llama a las funciones necesarias para mostrar los resultados de los docentes """
    docentes = obtener_datos()
    if docentes:
        for docente in docentes:
            print(docente.obtener_informacion())

if __name__ == '__main__':
    mostrar_resultados()