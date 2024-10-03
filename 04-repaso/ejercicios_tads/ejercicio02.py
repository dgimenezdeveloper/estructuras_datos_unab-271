""" Ejercicio 2: Biblioteca y gestión de préstamos
Desarrolla un sistema de gestión para una Biblioteca que maneje Libros y Préstamos.

Un Libro tiene ISBN, título, autor, año de publicación y ejemplares disponibles.
Un Préstamo tiene número de préstamo, libro prestado, usuario, fecha de préstamo, fecha de devolución y estado (si fue devuelto o no).
Requisitos:

Realizar un préstamo de un libro, si hay ejemplares disponibles.
Registrar la devolución de un libro.
Consultar los préstamos activos.
Consultar la disponibilidad de un libro.
Generar un informe de los libros prestados y su estado actual. """
libro1 = [1234567890123, 'algoritmos 1', 'Walter Bell', 2018, 2]
prestamo1 = [1, libro1, 'daseg', '26-09-2024', '27-09-2024', True]

class Libro:
    def __init__(self, isbn, titulo, autor, anio_publicacion, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.ejemplares = ejemplares
        
    def __str__(self):
        return f'ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio_publicacion}, Ejemplares disponibles: {self.ejemplares}'
    

class Prestamo:
    def __init__(self, num_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion = None, estado = True):
        self.num_prestamo = num_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        return f'Número de préstamo: {self.num_prestamo}, Libro: {self.libro}, Usuario: {self.usuario}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}, Prestado: {self.estado}'


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def prestar(self, libro, usuario, fecha_prestamo):
        if libro.ejemplares > 0:
            libro.ejemplares -= 1
            prestamo = Prestamo(len(self.prestamos) + 1, libro, usuario, fecha_prestamo)
            self.prestamos.append(prestamo)
    
    def consultar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)
    
    def disponible(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn and libro.ejemplares > 0:
                return f'El libro {libro.titulo} está disponible'
            else:
                return f'El libro {libro.titulo} no está disponible'
    
    def devolver(self,isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn:
                prestamo.libro.ejemplares += 1
                prestamo.estado = False
    
    def informe(self):
        for prestamo in self.prestamos:
            print(prestamo.libro)

libro1 = Libro(1234567890123, 'algoritmos 1', 'Walter Bell', 2018, 2)
libro2 = Libro(1234567890124, 'algoritmos 2', 'Walter Bell', 2019, 1)
libro3 = Libro(1234567890125, 'algoritmos 3', 'Walter Bell', 2020, 3)
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.prestar(libro1, 'daseg', '26-09-2024')
biblioteca.prestar(libro2, 'daseg', '26-09-2024')
biblioteca.consultar_prestamos()
biblioteca.disponible(1234567890124)
biblioteca.informe()
biblioteca.devolver(1234567890124)
biblioteca.informe()