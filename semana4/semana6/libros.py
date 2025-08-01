

class Libro:
    def __init__(self, titulo, anio_publicacion):
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion

    @classmethod
    def crear_libro(cls):
        while True:
            try:
                print("----------------------------------")
                titulo = input("Ingrese el título del libro: ")
                anio_publicacion = int(input("Ingrese el año de publicación del libro: "))
                return Libro(titulo, anio_publicacion)
            except ValueError:
                print("Error: El año de publicación debe ser un número entero.")

   