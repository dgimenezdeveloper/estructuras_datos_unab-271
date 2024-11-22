# src/paciente.py
from datetime import datetime

class Paciente:
    """
    Clase que representa a un paciente.
    """

    def __init__(self, id, nombre, fecha_nac, historial_enfermedades=None, medicamentos=None):
        """
        Inicializa una nueva instancia de la clase Paciente.

        - Args:
            * Id (int): Identificador único del paciente.
            * nombre (str): Nombre del paciente .
            * fecha_nac (str): Fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * edad (int): Edad del paciente.
            * historial_enfermedades (list, opcional): Lista de enfermedades del paciente. Por defecto es una lista vacía.
            * medicamentos (list, opcional): Lista de medicamentos del paciente. Por defecto es una lista vacía.
        """
        self.id = id
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

    def buscar_en_historial(self, clave):
        """
        Función recursiva para buscar una enfermedad o medicamento clave en el historial de tratamientos de un paciente.
        - Args
            * clave (str): Enfermedad o medicamento clave a buscar.
            
        :return: True si se encuentra la clave, False en caso contrario.
        """
        try:
            return self._buscar_en_historial_recursivo(self.historial_enfermedades + self.medicamentos, clave)
        except Exception as e:
            print(f"Error al buscar en el historial: {e}")
            return False

    def _buscar_en_historial_recursivo(self, historial, clave):
        """
        Función auxiliar recursiva para buscar una enfermedad o medicamento clave en el historial.
        . Args
            * historial (list): Lista de enfermedades y medicamentos del paciente.
            * clave (str): Enfermedad o medicamento clave a buscar.
            
        :return: True si se encuentra la clave, False en caso contrario.
        """
        try:
            # Caso base: si el historial está vacío, no se encontró la clave
            if not historial:
                return False
            
            # Verificar si la clave está en el tratamiento actual
            tratamiento_actual = historial[0]
            if tratamiento_actual == clave:
                return True
            
            # Llamada recursiva con el resto del historial
            return self._buscar_en_historial_recursivo(historial[1:], clave)
        except Exception as e:
            print(f"Error en la búsqueda recursiva: {e}")
            return False

    def __lt__(self, otro):
        """
        Compara dos objetos Paciente basándose en su ID.

        - Args:
            * otro (Paciente): Otro objeto Paciente a comparar.

        - Retorna:
            * (bool): True si el ID del paciente es menor que el ID del otro paciente, False en caso contrario.
        """
        return self.id < otro.id
    
    def __str__(self):
        """
        Devuelve una representación en cadena del paciente.

        - Retorna:
            * (str): Una cadena que representa al paciente.
        """
        return f"Nombre Paciente: {self.nombre}\nEdad: {self.edad}\nEnfermedades: {self.historial_enfermedades}\nMedicamentos: {self.medicamentos}"


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

    def agregar_paciente(self, paciente):
        """
        Agrega un nuevo paciente a la colección.

        - Args:
            * paciente (Paciente): Instancia de la clase Paciente a agregar.

        - Raises:
            * ValueError: Si el paciente con el ID dado ya existe.
        """
        try:
            if paciente.id in self.pacientes:
                raise ValueError(f"El paciente con ID {paciente.id} ya existe.")
            self.pacientes[paciente.id] = paciente
        except ValueError as e:
            print(e)

    def eliminar_paciente(self, id):
        """
        Elimina un paciente de la colección.

        - Args:
            * id (int): ID único del paciente a eliminar.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id}.")
            del self.pacientes[id]
        except KeyError as e:
            print(e)

    def obtener_paciente(self, id):
        """
        Obtiene un paciente de la colección.

        - Args:
            * id (int): ID único del paciente a obtener.

        - Retorna:
            * Paciente: La instancia de la clase Paciente correspondiente al ID dado, o None si no se encuentra.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id}.")
            return self.pacientes[id]
        except KeyError as e:
            print(e)

    def actualizar_paciente(self, id, nombre=None, fecha_nac=None, historial_enfermedades=None, medicamentos=None):
        """
        Actualiza la información de un paciente en la colección.

        - Args:
            * id (int): ID único del paciente a actualizar.
            * nombre (str, opcional): Nuevo nombre del paciente.
            * fecha_nac (str, opcional): Nueva fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * historial_enfermedades (list, opcional): Nuevo historial de enfermedades del paciente.
            * medicamentos (list, opcional): Nueva lista de medicamentos del paciente.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        try:
            if id not in self.pacientes:
                raise KeyError(f"No se encontró un paciente con ID {id}.")
            paciente = self.pacientes[id]
            if nombre is not None:
                paciente.nombre = nombre
            if fecha_nac is not None:
                paciente.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
                paciente.edad = paciente.calcular_edad()
            if historial_enfermedades is not None:
                paciente.historial_enfermedades = historial_enfermedades
            if medicamentos is not None:
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


if __name__ == "__main__":
    # Crear pacientes
    paciente1 = Paciente(1,"Juan", "1990-01-01", ["Gripe", "Fiebre"], ["Paracetamol", "Ibuprofeno"])
    paciente2 = Paciente(2,"Ana", "1985-05-10", ["Covid-19", "Asma"], ["Remdesivir", "Salbutamol"])
    paciente3 = Paciente(3,"Luis", "1975-03-22", ["Diabetes", "Hipertensión"], ["Insulina", "Lisinopril"])
    paciente4 = Paciente(4,"Maria", "2000-07-15", ["Alergia", "Migraña"], ["Loratadina", "Sumatriptán"])

    # Crear una colección de pacientes
    gestion_pacientes = GestionPacientes()
    gestion_pacientes.agregar_paciente(paciente1)
    gestion_pacientes.agregar_paciente(paciente2)
    gestion_pacientes.agregar_paciente(paciente3)
    gestion_pacientes.agregar_paciente(paciente4)

    # Mostrar la colección de pacientes
    print("Colección de pacientes:")
    print(gestion_pacientes)

    # Obtener y mostrar un paciente
    print("\nObtener paciente con ID 2:")
    paciente = gestion_pacientes.obtener_paciente(2)
    print(paciente)

    # Actualizar un paciente
    print("\nActualizar paciente con ID 3:")
    gestion_pacientes.actualizar_paciente(3, nombre="Luis Pérez", historial_enfermedades=["Diabetes", "Hipertensión", "Colesterol"], medicamentos=["Insulina", "Lisinopril", "Atorvastatina"])
    paciente = gestion_pacientes.obtener_paciente(3)
    print(paciente)

    # Eliminar un paciente
    print("\nEliminar paciente con ID 1:")
    gestion_pacientes.eliminar_paciente(1)
    print(gestion_pacientes)

    # Probar la función de búsqueda recursiva
    print("\nBuscar 'Insulina' en el historial del paciente con ID 3:")
    encontrado = paciente.buscar_en_historial("Insulina")
    print(f"¿Se encontró 'Insulina'? {'Sí' if encontrado else 'No'}")

    print("\nBuscar 'Covid-19' en el historial del paciente con ID 4:")
    encontrado = gestion_pacientes.obtener_paciente(4).buscar_en_historial("Covid-19")
    print(f"¿Se encontró 'Covid-19'? {'Sí' if encontrado else 'No'}")

    print("\nBuscar 'Migraña' en el historial del paciente con ID 4:")
    encontrado = gestion_pacientes.obtener_paciente(4).buscar_en_historial("Migraña")
    print(f"¿Se encontró 'Migraña'? {'Sí' if encontrado else 'No'}")