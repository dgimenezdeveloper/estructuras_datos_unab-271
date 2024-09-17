""" Definir  un  TDA  llamada  fracción.  Debe  entenderse  como  fracción:    ¾  .  Como  lo 
representaría?  Pensar los métodos definen el comportamiento de la fracción. """


class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar(self, fraccion):
        num = (self.numerador * fraccion.denominador) + (self.denominador * fraccion.numerador)
        den = self.denominador * fraccion.denominador
        return Fraccion(num,den)

    def restar(self, fraccion):
        num = (self.numerador * fraccion.denominador) - (self.denominador * fraccion.numerador)
        den = self.denominador * fraccion.denominador
        return Fraccion(num,den)

    def multiplicar(self, fraccion):
        num = self.numerador * fraccion.numerador
        den = self.denominador * fraccion.denominador
        return Fraccion(num,den)

    def dividir(self, fraccion):
        num = self.numerador * fraccion.denominador
        den = self.denominador * fraccion.numerador
        return Fraccion(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


f1 = Fraccion(1, 3)
f2 = Fraccion(1,4)
print(f1)
print(f1.sumar(f2))
print(f1.restar(f2))
print(f1.multiplicar(f2))
print(f1.dividir(f2))