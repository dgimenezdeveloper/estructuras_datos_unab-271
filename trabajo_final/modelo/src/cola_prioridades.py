# src/cola_prioridades.py

class ColaPrioridades:
    def __init__(self):
        self.elementos = []

    def agregar_paciente(self, prioridad, paciente):
        self.elementos.append((prioridad, paciente))
        self.elementos.sort(key=lambda x: x[0])

    def obtener_paciente(self):
        if self.elementos:
            return self.elementos.pop(0)[1]
        return None
    
    def __str__(self):
        resultado = ''
        for prioridad, paciente in self.elementos:
            resultado += f'{paciente} - Prioridad: {prioridad}\n'
        return resultado