# src/input_utils.py

from datetime import datetime

def solicitar_dni():
    while True:
        try:
            return int(input("Ingrese DNI: "))
        except ValueError:
            print("Error: El DNI debe ser un número entero.")

def solicitar_nombre():
    return input("Nombre: ")

def solicitar_fecha_nacimiento():
    while True:
        fecha_nac = input("Fecha de Nacimiento (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha_nac, "%Y-%m-%d")
            return fecha_nac
        except ValueError:
            print("Error: La fecha de nacimiento debe estar en el formato YYYY-MM-DD.")

def solicitar_lista(mensaje):
    return input(mensaje).split(",")