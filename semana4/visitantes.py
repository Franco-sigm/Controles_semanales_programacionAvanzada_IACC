
# Ejercicio: Crear un programa que permita gestionar una lista de visitantes a una sala.
# El programa debe permitir agregar visitantes, mostrar la lista de visitantes y vaciar la lista.
visitantes = []
def agregar_visitante():

    while True:
        try:
            nombre = input("Ingrese el nombre del visitante: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            sala = input("Ingrese la sala que visita: ").strip()
            if not sala:
                raise ValueError("La sala no puede estar vacía.")
            visitantes.append({"nombre": nombre, "sala": sala})
            
            opcion = input("¿Desea agregar otro visitante? (si/no): ").strip().lower() != "si"
            if opcion:
                print("Visitante agregado exitosamente.")
                break

        except ValueError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")
        
def mostrar_visitantes():
    if not visitantes:
        print("No hay visitantes registrados.")
    else:
        print("Lista unica de visitantes:")
        for visitante in visitantes:
            print(f"Nombre: {visitante['nombre']}, Sala: {visitante['sala']}")

def vaciar_lista():
    visitantes.clear()
    print("Lista de visitantes vaciada.")
# Función para mostrar el menú y manejar las opciones del usuario
def menu():
    while True:
        try:
            print("\nMenú de opciones:")
            print("1. Agregar visitante")
            print("2. Mostrar visitantes")
            print("3. Vaciar lista de visitantes")
            print("4. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                agregar_visitante()
            elif opcion == 2:
                mostrar_visitantes()
            elif opcion == 3:
                vaciar_lista()
            elif opcion == 4:
                print("Saliendo del programa.")
                break
        except ValueError:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        except ValueError as e:
            print(f" Error: {e}")



if __name__ == "__main__":
    menu()