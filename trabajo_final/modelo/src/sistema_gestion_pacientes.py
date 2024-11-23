# src/sistema_gestion_pacientes.py

from paciente import GestionPacientes
from arbol_binario import ArbolBinarioBusqueda

class SistemaGestionPacientes:
    def __init__(self):
        self.gestion_pacientes = GestionPacientes()
        self.arbol = ArbolBinarioBusqueda()

    def agregar_paciente(self, paciente):
        if self.gestion_pacientes.agregar_paciente(paciente):
            self.arbol.insertar(paciente)
            return True
        return False

    def eliminar_paciente(self, id):
        if self.gestion_pacientes.eliminar_paciente(id):
            self.arbol.eliminar(id)
            return True
        return False

    def obtener_paciente(self, id):
        return self.gestion_pacientes.obtener_paciente(id)

    def actualizar_paciente(self, id, nombre=None, fecha_nac=None, historial_enfermedades=None, medicamentos=None):
        if self.gestion_pacientes.actualizar_paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos):
            paciente = self.gestion_pacientes.obtener_paciente(id)
            self.arbol.eliminar(id)
            self.arbol.insertar(paciente)
            return True
        return False

    def __str__(self):
        return str(self.gestion_pacientes)