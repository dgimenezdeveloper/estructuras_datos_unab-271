""" Definir la clase Punto. Sus atributos serán las coodenadas en x e y del plano cartesiano. 
Un Punto reconoce las siguientes operaciones (métodos): 
distancia(p1, p2): distancia entre los puntos (devuleve un número) 
resta(p1, p2): resultado de la resta de dos puntos (devuelve un punto) 
norma(p): módulo del vector desde el origen hacia el punto p """


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, punto):
        a = (self.x - punto.x)**2
        b = (self.y - punto.y)**2
        distancia = (a + b)**(1/2)
        return distancia

    def resta(self, punto):
        x = self.x - punto.x
        y = self.y - punto.y
        return Punto(x,y)

    def norma(self):
        a = (self.x)**2
        b = (self.y)**2
        norma = (a + b)**(1/2)
        return norma
    
    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Punto(3,4)
p2 = Punto(2,3)
print(p1.distancia(p2))
print(p1.resta(p2))
print(p1.norma())