#**Permutaciones de una cadena**: Escribe una función recursiva que genere todas las permutaciones posibles 
# de una cadena de caracteres.

def permutar(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        resultado = []
        for permutacion in permutar(cadena[1:]):
            for i in range(len(permutacion)+1):
                resultado.append(permutacion[:i] + cadena[0] + permutacion[i:])
        return resultado