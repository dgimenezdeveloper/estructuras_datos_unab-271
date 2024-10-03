""" ## Ejercicio 5: Sistema de gestión de cursos y estudiantes
Imagina un sistema de gestión de una escuela que debe gestionar Cursos y Estudiantes.

Un Curso tiene ID, nombre, profesor, cupo máximo, estudiantes inscritos.
Un Estudiante tiene ID, nombre, apellido, edad, cursos inscritos.
Requisitos:

Inscribir un estudiante en un curso, si hay cupos disponibles.
Cancelar la inscripción de un estudiante en un curso.
Modificar el profesor de un curso.
Consultar los estudiantes inscritos en un curso.
Generar un informe de todos los cursos y los estudiantes inscritos en cada uno. """

class Escuela:
    def __init__(self):
        self.cursos = []
        self.estudiantes = []
    
    def __str__(self):
        return f"Cursos: {self.cursos}, Estudiantes: {self.estudiantes}"
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def _agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def inscribir(self, curso, estudiante):
        if curso.cupo_maximo > 0:
            curso.cupo_maximo -= 1
            estudiante.cursos_inscritos.append(curso)
            curso.estudiantes_inscritos.append(estudiante)
            print(f"Inscripción realizada con éxito. Cupo actualizado.")
        else:
            print("No hay cupos disponibles para inscribir al estudiante.")
    
    def cancelar_inscripcion(self, curso, estudiante):
        if curso in estudiante.cursos_inscritos:
            curso.cupo_maximo += 1
            estudiante.cursos_inscritos.remove(curso)
            curso.estudiantes_inscritos.remove(estudiante)
            print(f"Inscripción cancelada con éxito. Cupo actualizado.")
        else:
            print("El estudiante no está inscrito en el curso.")
    
    def modificar_profesor(self, curso, profesor):
        curso.profesor = profesor
        print(f"Profesor del curso actualizado.")
    
    def consultar_estudiantes(self, curso):
        for estudiante in curso.estudiantes_inscritos:
            print(estudiante)
    
    def informe_cursos(self):
        for curso in self.cursos:
            print(f"Curso: {curso.nombre}")
            if curso in self.cursos:
                for estudiante in curso.estudiantes_inscritos:
                    print(f"  - {estudiante.nombre} {estudiante.apellido}")
            else:
                print("  - No hay estudiantes inscritos en este curso.")
    
class Curso:
    def __init__(self, id, nombre, profesor, cupo_maximo):
        self.id = id
        self.nombre = nombre
        self.profesor = profesor
        self.cupo_maximo = cupo_maximo
        self.estudiantes_inscritos = []
    
    def __str__(self):
        estudiantes = ', '.join([estudiante.nombre for estudiante in self.estudiantes_inscritos])
        return f"ID: {self.id}, Nombre: {self.nombre}, Profesor: {self.profesor}, Cupo máximo: {self.cupo_maximo}, Estudiantes inscritos: {estudiantes}"

class Estudiante:
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cursos_inscritos = []
    
    def __str__(self):
        cursos = ', '.join([curso.nombre for curso in self.cursos_inscritos])
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Cursos inscritos: {cursos}"


if __name__ == '__main__':
    escuela = Escuela()
    
    curso1 = Curso(1, "Matemáticas", "Profesor1", 30)
    curso2 = Curso(2, "Física", "Profesor2", 25)
    curso3 = Curso(3, "Química", "Profesor3", 20)
    
    estudiante1 = Estudiante(1, "Estudiante1", "Apellido1", 20)
    estudiante2 = Estudiante(2, "Estudiante2", "Apellido2", 21)
    estudiante3 = Estudiante(3, "Estudiante3", "Apellido3", 22)
    
    escuela.agregar_curso(curso1)
    escuela.agregar_curso(curso2)
    escuela.agregar_curso(curso3)
    
    escuela._agregar_estudiante(estudiante1)
    escuela._agregar_estudiante(estudiante2)
    escuela._agregar_estudiante(estudiante3)
    
    escuela.inscribir(curso1, estudiante1)
    escuela.inscribir(curso1, estudiante2)
    escuela.inscribir(curso1, estudiante3)
    
    escuela.cancelar_inscripcion(curso1, estudiante2)
    
    escuela.modificar_profesor(curso1, "Profesor4")
    
    escuela.consultar_estudiantes(curso1)
    
    escuela.informe_cursos()