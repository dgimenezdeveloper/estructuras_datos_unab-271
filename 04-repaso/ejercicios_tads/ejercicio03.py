""" ## Ejercicio 3: Sistema de reservas de vuelos
Imagina un sistema de reservas para una aerolínea. El sistema debe gestionar Vuelos y Reservas.

Un Vuelo tiene número de vuelo, origen, destino, fecha y hora, capacidad total, y asientos disponibles.
Una Reserva tiene número de reserva, pasajero, vuelo, fecha de reserva y estado (confirmado o cancelado).
Requisitos:

Realizar una reserva para un pasajero en un vuelo disponible.
Cancelar una reserva.
Consultar la disponibilidad de asientos en un vuelo.
Modificar la fecha de un vuelo.
Generar un informe de todas las reservas confirmadas para un vuelo en particular. """
class Vuelos:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, capacidad):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.capacidad_total = capacidad
        self.asientos_disponibles = capacidad
    
    def __str__(self):
        return f'Número de vuelo: {self.num_vuelo}, Origen: {self.origen}, Destino: {self.destino}, Fecha y hora: {self.fecha_hora}, Capacidad total: {self.capacidad_total}, Asientos disponibles: {self.asientos_disponibles}'
    
    def asientos(self):
        return self.asientos_disponibles
    
    def cambiar_fecha(self, fecha_hora):
        self.fecha_hora = fecha_hora

class Reservas:
    def __init__(self, num_reserva, pasajero, vuelo, fecha_reserva, confirmado = True):
        self.num_reserva = num_reserva
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva
        self.confirmado = confirmado
        self.reservas = []
    
    def __str__(self):
        return f'Número de reserva: {self.num_reserva}, Pasajero: {self.pasajero}, Vuelo: {self.vuelo}, Fecha de reserva: {self.fecha_reserva}, Confirmado: {self.confirmado}'
    
class Aerolinea:
    def __init__(self):
        self.vuelos = []
        self.reservas = []
    
    def __str__(self):
        return f'Vuelos: {self.vuelos}, Reservas: {self.reservas}'
    
    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
    
    def _agregar_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def reservar(self, vuelo, pasajero, fecha_reserva):
        if vuelo.asientos_disponibles > 0:
            vuelo.asientos_disponibles -= 1
            reserva = Reservas(len(self.reservas) + 1, pasajero, vuelo, fecha_reserva)
            self._agregar_reserva(reserva)
    
    def cancelar_reserva(self, reserva):
        reserva.confirmado = False
        reserva.vuelo.asientos_disponibles += 1
    
    def consultar_disponibilidad(self, vuelo):
        print(f'Asientos disponibles en el vuelo {vuelo.num_vuelo}: {vuelo.asientos_disponibles}')
    
    def modificar_fecha(self, vuelo, fecha_hora):
        vuelo.cambiar_fecha(fecha_hora)
    
    def informe_reservas(self, vuelo):
        for reserva in self.reservas:
            if reserva.vuelo == vuelo and reserva.confirmado:
                print(reserva)


# Vuelos
vuelo1 = Vuelos(1, 'Madrid', 'Barcelona', '2021-06-01 10:00', 100)
a1 = Aerolinea()
a1.reservar(vuelo1, 'Juan', '2021-05-01')
a1.informe_reservas(vuelo1)
