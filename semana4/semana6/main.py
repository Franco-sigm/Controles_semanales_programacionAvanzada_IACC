from autores import Autor
from libros import Libro
from libros_autores import guardar_libro, mostrar_libros, guardar_autores, mostrar_autores

def menu():
    while True:
        try:
            print("\nMenú de opciones:")
            print("1. Agregar libro")
            print("2. agregar autor")
            print("3. ver libros")
            print("4. ver autores")
            print("5. salir")

            

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                nuevo_libro = Libro.crear_libro()
                guardar_libro(nuevo_libro)
            elif opcion == 2:
                nuevo_autor = Autor.crear_autor()
                guardar_autores(nuevo_autor)
            elif opcion == 3:
                mostrar_libros()
            elif opcion == 4:
                mostrar_autores()
            elif opcion == 5:
                print("Saliendo del programa Hata pronto!!!.")
                break
        except ValueError:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        except ValueError as e:
            print(f" Error: {e}")



if __name__ == "__main__":    menu()