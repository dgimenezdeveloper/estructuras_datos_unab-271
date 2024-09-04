""" Desarrollar un algoritmo que permita calcular la siguiente serie: h(n) =
1+1/2+1/3+...+1/n """

def serie_h(n):
    suma = 0
    for i in range(1, n + 1):
        suma += 1 / i
    return suma

def main():
    print(serie_h(5)) # 2.283333333333333

main()