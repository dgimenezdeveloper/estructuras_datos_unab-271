""" Ejercicio 1: Criaturas Mágicas y Magos (TADs)

Enunciado

En el universo mágico, los magos y brujas pueden criar criaturas mágicas. Para este ejercicio deberá
implementar dos clases en Python: CriaturaMagica y Mago.

Clases a Implementar

1. Clase CriaturaMagica:

• Atributos:

• nombre: (str) Nombre de la criatura.

• tipo: (str) Tipo de criatura mágica (por ejemplo, Fénix, Hipogrifo, Thestral).
 
• nivel_magico: (int) Nivel de magia de la criatura (debe estar entre 1 y 100).

• Métodos:

• __init__ (): Constructor que inicializa los atributos de la criatura.

• aumentar_nivel(): Método que incrementa el nivel mágico de la criatura en 1, siempre que no supere el nivel 100.

• __str__(): Método que devuelve una representación en cadena de la criatura en el formato: "Criatura: [Nombre], Tipo: [Tipo], Nivel Mágico: [Nivel]".


2. Clase Mago:

• Atributos:

• nombre: (str) Nombre del mago o bruja.

• criaturas: (lista) Lista que contiene instancias de la clase CriaturaMagica


• Métodos:

• __init__(): Constructor que inicializa el nombre del mago y crea una lista vacía para las criaturas mágicas.

• agregar_criatura(): Método que agrega una criatura al grupo. Si ya hay 6 criaturas en el grupo, debe mostrar un mensaje indicando que no se pueden tener más criaturas.

• mostrar_criaturas(): Método que imprime todas las criaturas del grupo utilizando el método __str_ de la clase CriaturaMagica.

• nivel_magico_promedio(): Método que calcula y devuelve el nivel promedio de magia de las criaturas en el grupo. Si no hay criaturas, debe devolver 0.
 """
class CriaturaMagica:
    def __init__(self, nombre, tipo, nivel_magico):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = nivel_magico

    def aumentar_nivel(self):
        if self.nivel_magico < 100:
            self.nivel_magico += 1

    def __str__(self):
        return f"Criatura: {self.nombre}, Tipo: {self.tipo}, Nivel Mágico: {self.nivel_magico}"

class Mago:
    def __init__(self, nombre):
        self.nombre = nombre
        self.criaturas = []

    def agregar_criatura(self, criatura):
        if len(self.criaturas) < 6:
            self.criaturas.append(criatura)
        else:
            print("No se pueden tener más criaturas")

    def mostrar_criaturas(self):
        for criatura in self.criaturas:
            print(criatura)

    def nivel_magico_promedio(self):
        if len(self.criaturas) == 0:
            return 0
        return sum([criatura.nivel_magico for criatura in self.criaturas]) / len(self.criaturas)