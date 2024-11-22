# src/arbol_binario.py
from paciente import Paciente, GestionPacientes

class NodoArbol:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.

    Atributos:
        paciente (Paciente): Objeto de la clase Paciente.
        izquierda (Nodo): Nodo hijo izquierdo.
        derecha (Nodo): Nodo hijo derecho.
    """
    def __init__(self, paciente):
        """
        Inicializa un nodo con el identificador del paciente y el objeto paciente.

        Args:
            paciente (Paciente): Objeto de la clase Paciente.
        """
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    """
    Clase que representa un árbol binario de búsqueda.

    Atributos:
        raiz (Nodo): Nodo raíz del árbol.
    """
    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.raiz = None

    def insertar(self, paciente):
        """
        Inserta un nuevo nodo en el árbol binario de búsqueda.

        Args:
            paciente (Paciente): Objeto de la clase Paciente.
        """
        if self.raiz is None:
            self.raiz = NodoArbol(paciente)
        else:
            self._insertar_recursivo(self.raiz, paciente)

    def _insertar_recursivo(self, nodo, paciente):
        """
        Inserta un nuevo nodo en el árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (Nodo): Nodo actual en el que se está realizando la inserción.
            paciente (Paciente): Objeto de la clase Paciente.
        """
        if paciente.id < nodo.paciente.id:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(paciente)
            else:
                self._insertar_recursivo(nodo.izquierda, paciente)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(paciente)
            else:
                self._insertar_recursivo(nodo.derecha, paciente)

    def buscar(self, id):
        """
        Busca un nodo en el árbol binario de búsqueda por el identificador del paciente.

        Args:
            id (int): Identificador del paciente.

        Returns:
            Paciente: Objeto de la clase Paciente que contiene el identificador del paciente, o None si no se encuentra.
        """
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, nodo, id):
        """
        Busca un nodo en el árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (Nodo): Nodo actual en el que se está realizando la búsqueda.
            id (int): Identificador del paciente.

        Returns:
            Paciente: Objeto de la clase Paciente que contiene el identificador del paciente, o None si no se encuentra.
        """
        if nodo is None or nodo.paciente.id == id:
            return nodo
        if id < nodo.paciente.id:
            return self._buscar_recursivo(nodo.izquierda, id)
        return self._buscar_recursivo(nodo.derecha, id)

    def eliminar(self, id):
        """
        Elimina un nodo del árbol binario de búsqueda por el identificador del paciente.

        Args:
            id (int): Identificador del paciente.
        """
        self.raiz = self._eliminar_recursivo(self.raiz, id)

    def _eliminar_recursivo(self, nodo, id):
        """
        Elimina un nodo del árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (Nodo): Nodo actual en el que se está realizando la eliminación.
            id (int): Identificador del paciente.

        Returns:
            Nodo: Nodo actualizado después de la eliminación.
        """
        if nodo is None:
            return nodo
        if id < nodo.paciente.id:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, id)
        elif id > nodo.paciente.id:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, id)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo_valor_nodo(nodo.derecha)
            nodo.paciente = temp.paciente
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.paciente.id)
        return nodo

    def _minimo_valor_nodo(self, nodo):
        """
        Encuentra el nodo con el valor mínimo en el árbol binario de búsqueda.

        Args:
            nodo (Nodo): Nodo desde el cual se empieza la búsqueda.

        Returns:
            Nodo: Nodo con el valor mínimo.
        """
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def __str__(self):
        """
        Devuelve una representación en cadena del árbol binario de búsqueda en orden.

        Returns:
            str: Representación en cadena del árbol.
        """
        nodos = []
        self._in_order(self.raiz, nodos)
        return "\n".join(f"ID: {nodo.id_paciente}, Paciente: {nodo.paciente}" for nodo in nodos)

    def _in_order(self, nodo, nodos):
        """
        Realiza un recorrido en orden del árbol binario de búsqueda y almacena los nodos en una lista.

        Args:
            nodo (Nodo): Nodo actual en el que se está realizando el recorrido.
            nodos (list): Lista para almacenar los nodos en orden.
        """
        if nodo is not None:
            self._in_order(nodo.izquierda, nodos)
            nodos.append(nodo)
            self._in_order(nodo.derecha, nodos)
    
    
def main():
    # Crear pacientes
    paciente1 = Paciente(1, "Juan Pérez", "1990-01-01", ["Gripe", "Fiebre"], ["Paracetamol", "Ibuprofeno"])
    paciente2 = Paciente(2, "Ana López", "1985-05-10", ["Covid-19", "Asma"], ["Remdesivir", "Salbutamol"])
    paciente3 = Paciente(3, "Luis García", "1975-03-22", ["Diabetes", "Hipertensión"], ["Insulina", "Lisinopril"])
    paciente4 = Paciente(4, "María Fernández", "2000-07-15", ["Alergia", "Migraña"], ["Loratadina", "Sumatriptán"])

    # Crear una colección de pacientes usando GestionPacientes
    gestion_pacientes = GestionPacientes()
    gestion_pacientes.agregar_paciente(paciente1)
    gestion_pacientes.agregar_paciente(paciente2)
    gestion_pacientes.agregar_paciente(paciente3)
    gestion_pacientes.agregar_paciente(paciente4)

    # Crear un árbol binario de búsqueda
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(1, paciente1)
    arbol.insertar(2, paciente2)
    arbol.insertar(3, paciente3)
    arbol.insertar(4, paciente4)

    # Mostrar la colección de pacientes usando GestionPacientes
    print("Colección de pacientes (GestionPacientes):")
    print(gestion_pacientes)

    # Mostrar la colección de pacientes usando ArbolBinarioBusqueda
    print("\nColección de pacientes (ArbolBinarioBusqueda):")
    print(arbol)

    # Obtener y mostrar un paciente usando GestionPacientes
    print("\nObtener paciente con ID 2 (GestionPacientes):")
    paciente = gestion_pacientes.obtener_paciente(2)
    print(paciente)

    # Obtener y mostrar un paciente usando ArbolBinarioBusqueda
    print("\nObtener paciente con ID 2 (ArbolBinarioBusqueda):")
    paciente = arbol.buscar(2)
    print(paciente)

    # Actualizar un paciente usando GestionPacientes
    print("\nActualizar paciente con ID 3 (GestionPacientes):")
    gestion_pacientes.actualizar_paciente(3, nombre="Luis Pérez", historial_enfermedades=["Diabetes", "Hipertensión", "Colesterol"], medicamentos=["Insulina", "Lisinopril", "Atorvastatina"])
    paciente = gestion_pacientes.obtener_paciente(3)
    print(paciente)

    # Eliminar un paciente usando GestionPacientes
    print("\nEliminar paciente con ID 1 (GestionPacientes):")
    gestion_pacientes.eliminar_paciente(1)
    print(gestion_pacientes)

    # Eliminar un paciente usando ArbolBinarioBusqueda
    print("\nEliminar paciente con ID 1 (ArbolBinarioBusqueda):")
    arbol.eliminar(1)
    print(arbol)

    # Mostrar cómo el árbol binario de búsqueda puede ser útil para operaciones de rango
    print("\nPacientes en el rango de ID 2 a 4 (ArbolBinarioBusqueda):")
    pacientes_en_rango = obtener_pacientes_en_rango(arbol, 2, 4)
    for paciente in pacientes_en_rango:
        print(paciente)

# Caso de uso cuando se requiere usar una busqueda  binaria en lugar de la clase  GestionPacientes
def obtener_pacientes_en_rango(arbol, id_min, id_max):
    """
    Obtiene una lista de pacientes cuyos IDs están en el rango [id_min, id_max].

    :param arbol: El árbol binario de búsqueda.
    :param id_min: El ID mínimo del rango.
    :param id_max: El ID máximo del rango.
    :return: Una lista de pacientes en el rango especificado.
    """
    resultado = []
    _obtener_pacientes_en_rango_recursivo(arbol.raiz, id_min, id_max, resultado)
    return resultado

def _obtener_pacientes_en_rango_recursivo(nodo, id_min, id_max, resultado):
    """
    Función auxiliar recursiva para obtener pacientes en un rango de IDs.

    :param nodo: El nodo actual del árbol binario de búsqueda.
    :param id_min: El ID mínimo del rango.
    :param id_max: El ID máximo del rango.
    :param resultado: La lista de resultados para almacenar los pacientes.
    """
    if nodo is None:
        return
    if id_min <= nodo.id_paciente <= id_max:
        resultado.append(nodo.paciente)
    if id_min < nodo.id_paciente:
        _obtener_pacientes_en_rango_recursivo(nodo.izquierda, id_min, id_max, resultado)
    if nodo.id_paciente < id_max:
        _obtener_pacientes_en_rango_recursivo(nodo.derecha, id_min, id_max, resultado)

if __name__ == "__main__":
    main()