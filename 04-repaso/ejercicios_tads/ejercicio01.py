""" Ejercicio 1: Sistema de gestión de empleados y proyectos
Se desea crear un sistema de gestión de empleados que trabaje con Empleados y Proyectos.

Cada Empleado tiene los siguientes atributos: ID, nombre, apellido, salario, cargo y proyectos_asignados.
Un Proyecto tiene los siguientes atributos: ID, nombre, fecha_inicio, fecha_fin, presupuesto.
Requisitos:

Agregar un empleado a un proyecto.
Eliminar un empleado de un proyecto.
Modificar el salario de un empleado.
Consultar todos los empleados asignados a un proyecto.
Generar un informe de todos los empleados y los proyectos en los que están trabajando. """

class Empleado:
    def __init__(self, id, nombre, apellido, salario, cargo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.cargo = cargo
        self.proyectos_asignados = []
    
    def asignar_proyecto(self, proyecto):
        if proyecto not in self.proyectos_asignados:
            self.proyectos_asignados.append(proyecto)
    
    def eliminar_proyecto(self, proyecto):
        if proyecto in self.proyectos_asignados:
            self.proyectos_asignados.remove(proyecto)
    
    def modificar_salario(self, nuevo_salario):
        self.salario = nuevo_salario

class Proyecto:
    def __init__(self, id_proyecto, nombre, fecha_inicio, fecha_fin, presupuesto):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.presupuesto = presupuesto
    
class SistemaGestion:
    def __init__(self):
        self.empleados = []
        self.proyectos = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
    
    def buscar_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id_proyecto == id_proyecto:
                return proyecto
        return None
    
    def agregar_empleado_proyecto(self, empleado, id_proyecto):
        proyecto = self.buscar_proyecto(id_proyecto)
        if proyecto:
            empleado.asignar_proyecto(proyecto)
        #     print(f"Proyecto {proyecto.nombre} asignado a {empleado.nombre}.")
        # else:
        #     print(f"El proyecto con ID {id_proyecto} no existe.")
    
    def eliminar_empleado_proyecto(self, empleado, id_proyecto):
        proyecto = self.buscar_proyecto(id_proyecto)
        if proyecto:
            empleado.eliminar_proyecto(proyecto)
        else:
            return None
    
    def consultar_empleados_proyecto(self, id_proyecto):
        proyecto = self.buscar_proyecto(id_proyecto)
        empleados_asignados = []
        if proyecto:
            for empleado in self.empleados:
                if proyecto in empleado.proyectos_asignados:
                    empleados_asignados.append(f"Empleado: {empleado.nombre} {empleado.apellido}")
        for empleado in empleados_asignados:
            print(empleado)
        return empleados_asignados
    
    def generar_informe(self):
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre} {empleado.apellido}")
            for proyecto in empleado.proyectos_asignados:
                print(f"Proyecto: {proyecto.nombre} - Presupuesto: {proyecto.presupuesto} - Fecha de inicio: {proyecto.fecha_inicio} - Fecha de fin: {proyecto.fecha_fin}")
            print("")    
    
# Creación del sistema
sistema = SistemaGestion()

# Creación de empleados
empleado1 = Empleado(123, 'Daro', 'Gomez', 1234565688, 'Trainee')
empleado2 = Empleado(321, 'Maria', 'Gonzalez', 12345, 'Senior')

# Creación de proyectos
proyecto1 = Proyecto('A12', 'Frontend', '12-01-2023', '13-04-2024', 1000000)
proyecto2 = Proyecto('A13', 'Backend', '12-01-2023', '13-07-2024', 1000000)

# Agregar empleados al sistema
sistema.agregar_empleado(empleado1)
sistema.agregar_empleado(empleado2)

# Agregar proyectos al sistema
sistema.agregar_proyecto(proyecto1)
sistema.agregar_proyecto(proyecto2)

# Asignar empleados a proyectos
sistema.agregar_empleado_proyecto(empleado1, 'A12')
sistema.agregar_empleado_proyecto(empleado1, 'A13')
sistema.agregar_empleado_proyecto(empleado2, 'A12')

# Modificar salario
empleado2.modificar_salario(150000)

# Eliminar proyecto
#sistema.eliminar_empleado_proyecto(empleado1, 'A13')

# Consultar empleados por proyecto
sistema.consultar_empleados_proyecto('A12')

# Generar informe completo
sistema.generar_informe()