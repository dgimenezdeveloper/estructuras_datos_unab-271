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
    

class Prestamo:
    def __init__(self, num_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion, estado):
        self.num_prestamo = num_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
    
    def prestar_libro(self, libro):
        if libro.ejemplares == 0:
            pass