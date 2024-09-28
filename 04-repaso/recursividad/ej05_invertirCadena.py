#5. **Inversión de una cadena**: Escribe una función recursiva que invierta una cadena de caracteres.
def invertir_cadena(string):
    if len(string)==1:
        return string[0]
    else:
        return invertir_cadena(string[1:]) + string[0]

print(invertir_cadena('hola'))