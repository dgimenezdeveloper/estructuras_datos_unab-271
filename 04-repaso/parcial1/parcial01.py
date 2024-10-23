class Autor:
    def __init__(self, nombre, apellido, libros = []):
        self.nombre = nombre
        self.apellido = apellido
        self.libros = libros
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def borrar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
    
    def imprimir_libro(self, anio_publicacion, titulo):
        #print(f'Libros Publicados por {self.autor}')
        for libro in self.libros:
            if libro.anio == anio_publicacion and libro.titulo == titulo:
                print(libro)

class Libro:
    def __init__(self, titulo, anio, editorial):
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
    
    def __str__(self):
        return f'Titulo: {self.titulo}, Año: {self.anio}, Editorial: {self.editorial}'

def main():
    autor1 = Autor('Jorge', 'Borges')
    libro1 = Libro('Ficciones', 1944, 'Sur')
    autor1.agregar_libro(libro1)
    autor1.imprimir_libro(1944,'Ficciones')
    autor1.imprimir_libro

main()