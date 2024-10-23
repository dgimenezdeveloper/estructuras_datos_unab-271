def suma_pares(lista):
    suma = 0
    if lista == []:
        return 0
    elif lista[0]%2==0:
        suma+= lista[0] + suma_pares(lista[1:])
    else:
        suma += suma_pares(lista[1:])
    return suma

def main():
    print(suma_pares([1,2,3,4,5,6,7,8,9,10]))

main()