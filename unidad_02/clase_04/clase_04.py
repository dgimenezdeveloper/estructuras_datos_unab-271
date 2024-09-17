class Persona1:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def info(self):
        print(self.apellido, ",", self.nombre)


x = Persona1("Juan", "Gomez")
x.info
()


# otra forma
class Persona2:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def info_persona(persona):
    print(persona.apellido, ",", persona.nombre)


x = Persona2("Juan", "Gomez")
info_persona(x)


# otra forma mas
class Persona3:
    nombre = ""
    apellido = ""


def info_persona3(persona):
    print(persona.apellido, ",", persona.nombre)


x = Persona3()
x.nombre = "Juan"
x.apellido = "Gomez"
info_persona3(x)


