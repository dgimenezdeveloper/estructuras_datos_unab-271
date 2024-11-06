# src/paciente.py
from datetime import datetime

class Paciente:
    """
    Clase que representa a un paciente.
    """

    def __init__(self, nombre, fecha_nac, historial_enfermedades=None, medicamentos=None):
        """
        Inicializa una nueva instancia de la clase Paciente.

        - Args:
            * nombre (str): Nombre del paciente .
            * fecha_nac (str): Fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * edad (int): Edad del paciente.
            * historial_enfermedades (list, opcional): Lista de enfermedades del paciente. Por defecto es una lista vacía.
            * medicamentos (list, opcional): Lista de medicamentos del paciente. Por defecto es una lista vacía.
        """
        self.nombre = nombre
        self.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")  # Convierte la cadena a datetime
        self.edad = self.calcular_edad()
        self.historial_enfermedades = historial_enfermedades if historial_enfermedades else []
        self.medicamentos = medicamentos if medicamentos else []

    def calcular_edad(self):
        """
        Calcula la edad del paciente a partir de la fecha de nacimiento.

        Retorna:
            * (int): La edad del paciente.
        """
        hoy = datetime.today()
        edad = hoy.year - self.fecha_nac.year
        if hoy.month < self.fecha_nac.month or (hoy.month == self.fecha_nac.month and hoy.day < self.fecha_nac.day):
            edad -= 1
        return edad

    def agregar_enfermedad(self, enfermedad):
        """
        Agrega una enfermedad al historial de enfermedades del paciente.

        - Args:
            * enfermedad (str):  La enfermedad a agregar.
        """
        self.historial_enfermedades.append(enfermedad)

    def agregar_medicamento(self, medicamento):
        """
        Agrega un medicamento a la lista de medicamentos del paciente.

        - Args:
            * medicamento (str): El medicamento a agregar.
        """
        self.medicamentos.append(medicamento)

    def __str__(self):
        """
        Devuelve una representación en cadena del paciente.

        - Retorna:
            * (str): Una cadena que representa al paciente.
        """
        return f"Nombre Paciente: {self.nombre}\n Edad: {self.edad}\n Enfermedades: {self.historial_enfermedades}\n Medicamentos: {self.medicamentos}."

class GestionPacientes:
    """
    Clase para gestionar una colección de pacientes.

    - Atributos:
        * pacientes (dicc): Diccionario de pacientes donde las claves son los IDs de los pacientes y los valores son instancias de la clase Paciente.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase GestionPacientes.
        """
        self.pacientes = {}

    def agregar_paciente(self, id_paciente, paciente):
        """
        Agrega un nuevo paciente a la colección.

        - Args:
            * id_paciente (str): ID único del paciente.
            * paciente (Paciente): Instancia de la clase Paciente a agregar.

        - Raises:
            * ValueError: Si el paciente con el ID dado ya existe.
        """
        try:
            if id_paciente in self.pacientes:
                raise ValueError(f"El paciente con ID {id_paciente} ya existe.")
            self.pacientes[id_paciente] = paciente
        except ValueError as e:
            print(e)

    def eliminar_paciente(self, id_paciente):
        """
        Elimina un paciente de la colección.

        - Args:
            * id_paciente (str): ID único del paciente a eliminar.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id_paciente not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id_paciente}.")
            del self.pacientes[id_paciente]
        except KeyError as e:
            print(e)

    def obtener_paciente(self, id_paciente):
        """
        Obtiene un paciente de la colección.

        - Args:
            * id_paciente (str): ID único del paciente a obtener.

        - Retorna:
            * Paciente: La instancia de la clase Paciente correspondiente al ID dado, o None si no se encuentra.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id_paciente not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id_paciente}.")
            return self.pacientes[id_paciente]
        except KeyError as e:
            print(e)
            return None

    def actualizar_paciente(self, id_paciente, nombre=None, fecha_nac=None, historial_enfermedades=None, medicamentos=None):
        """
        Actualiza la información de un paciente en la colección.

        - Args:
            * id_paciente (str): ID único del paciente a actualizar.
            * nombre (str, opcional): Nuevo nombre del paciente.
            * fecha_nac (str, opcional): Nueva fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * historial_enfermedades (list, opcional): Nuevo historial de enfermedades del paciente.
            * medicamentos (list, opcional): Nueva lista de medicamentos del paciente.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id_paciente not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id_paciente}.")
            paciente = self.pacientes[id_paciente]
            if nombre:
                paciente.nombre = nombre
            if fecha_nac:
                paciente.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
                paciente.edad = paciente.calcular_edad()
            if historial_enfermedades:
                paciente.historial_enfermedades = historial_enfermedades
            if medicamentos:
                paciente.medicamentos = medicamentos
        except KeyError as e:
            print(e)
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la colección de pacientes.

        - Retorna:
            * str: Una cadena que representa la colección de pacientes.
        """
        resultado = []
        for id_paciente, paciente in self.pacientes.items():
            resultado.append(f"Id paciente: {id_paciente}\n {paciente}")
        return "\n".join(resultado)

if __name__  == "__main__":
    # Crear un paciente
    paciente1 = Paciente("Juan", "1990-01-01", ["Gripe", "Fiebre"], ["Paracetamol", "Ibuprofeno"])
    print(paciente1)

    # Crear una colección de pacientes
    gestion_pacientes = GestionPacientes()
    gestion_pacientes.agregar_paciente(1, paciente1)
    print(gestion_pacientes)

    # Obtener un paciente
    paciente = gestion_pacientes.obtener_paciente(1)
    print(paciente)

    # Actualizar un paciente
    gestion_pacientes.actualizar_paciente(1, nombre="Juan Pérez", fecha_nac="1990-01-01", historial_enfermedades=["Gripe", "Fiebre", "Resfriado"], medicamentos=["Paracetamol", "Ibuprofeno", "Aspirina"])
    paciente = gestion_pacientes.obtener_paciente(1)
    print(paciente)

    # Eliminar un paciente
    gestion_pacientes.eliminar_paciente(1)
    
    paciente2 = Paciente("Ana", "1985-05-10", ["Gripe", "Fiebre"], ["Paracetamol", "Ibuprofeno"])
    gestion_pacientes.agregar_paciente(2, paciente2)
    print(gestion_pacientes)