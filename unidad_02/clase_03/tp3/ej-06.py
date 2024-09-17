""" Definir la clase Rectangulo. Un rectangulo pude ser definido de varias maneras, por 
ejemplo: 
4 puntos: las 4 esquinas (sirve para cualquier poligono). 
2 puntos: Idem anterior, pero usamos dos. 
1 punto de referencia, base y altura. 
(Elejir solo una e implementarla) 
La clase debe contener los siguientes métodos: 
Calcular el perimetro del rectangulo. 
Clacular el area del rectangulo. 
Chequear si el rectangulo es un cuadradro """
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, punto):
        a = (self.x - punto.x)**2
        b = (self.y - punto.y)**2
        distancia = (a + b)**(1/2)
        return distancia
    
    def __str__(self):
        return f'({self.x}, {self.y})'

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.base = abs(p2.x - p1.x)
        self.altura = abs(p2.y - p1.y)
    
    def perimetro(self):
        perimetro = 2 * (self.base * self.altura)
        return perimetro
    
    def area(self):
        area = self.base * self.altura
        return area
    
    def es_cuadrado(self):
        return self.altura == self.base
    
    def __str__(self):
        pass


p1= Punto(10,20)
p2= Punto(14,16)

r1 = Rectangulo(p1,p2)
print(r1.perimetro())
print(r1.area())
print(r1.es_cuadrado())