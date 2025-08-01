
class Autor:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    @classmethod
    def crear_autor(cls):
        while True:
            try:
                nombre = input("ingresa el nombre del autor :")
                edad = int(input("ingresa la edad del autor :"))
                nacionalidad = input("ingrese la nacionalidad del autor :")
                return Autor(nombre, edad, nacionalidad)
            except ValueError:
                print("error, ingresa datos validos")
