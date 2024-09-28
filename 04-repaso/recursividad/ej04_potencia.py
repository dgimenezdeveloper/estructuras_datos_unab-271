""" 4. **Potencia**: Escribe una función recursiva que calcule la potencia de un número dado una base y un exponente. """
def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base * (potencia(base, exponente - 1))

print(potencia(3,3))