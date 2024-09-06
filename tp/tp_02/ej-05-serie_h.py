""" Desarrollar un algoritmo que permita calcular la siguiente serie: h(n) =
1+1/2+1/3+...+1/n """

def serie_h(n):
    if n == 1:
        return 1
    else:
        return 1/n + serie_h(n-1)

def main():
    print(serie_h(5))

main()