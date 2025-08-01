import json
import os

# Rutas de los archivos JSON
ARCHIVO_AUTORES = "autores.json"
ARCHIVO_LIBROS = "libros.json"

# Crear archivos si no existen
def inicializar_archivos():
    if not os.path.exists(ARCHIVO_AUTORES):
        with open(ARCHIVO_AUTORES, "w", encoding="utf-8") as f:
            json.dump([], f)

    if not os.path.exists(ARCHIVO_LIBROS):
        with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as f:
            json.dump([], f)

# Cargar datos desde archivo
def cargar_datos(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# Guardar datos en archivo
def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Agregar un autor
def agregar_autor():
    nombre = input("Nombre del autor: ").strip()
    nacionalidad = input("Nacionalidad: ").strip()

    if not nombre or not nacionalidad:
        print("⚠️  Todos los campos son obligatorios.")
        return

    autores = cargar_datos(ARCHIVO_AUTORES)
    nuevo_autor = {"nombre": nombre, "nacionalidad": nacionalidad}
    autores.append(nuevo_autor)
    guardar_datos(ARCHIVO_AUTORES, autores)
    print("✅ Autor agregado con éxito.")

# Agregar un libro
def agregar_libro():
    titulo = input("Título del libro: ").strip()
    genero = input("Género: ").strip()
    anio = input("Año de publicación: ").strip()
    autor = input("Nombre del autor: ").strip()

    if not titulo or not genero or not anio or not autor:
        print("⚠️  Todos los campos son obligatorios.")
        return

    libros = cargar_datos(ARCHIVO_LIBROS)
    nuevo_libro = {
        "titulo": titulo,
        "genero": genero,
        "anio": anio,
        "autor": autor
    }
    libros.append(nuevo_libro)
    guardar_datos(ARCHIVO_LIBROS, libros)
    print("✅ Libro agregado con éxito.")

# Mostrar la información almacenada
def mostrar_informacion():
    print("\n📚 LIBROS REGISTRADOS:")
    libros = cargar_datos(ARCHIVO_LIBROS)
    if libros:
        for i, libro in enumerate(libros, 1):
            print(f"\nLibro #{i}")
            print(f"  Título: {libro['titulo']}")
            print(f"  Género: {libro['genero']}")
            print(f"  Año: {libro['anio']}")
            print(f"  Autor: {libro['autor']}")
    else:
        print("No hay libros registrados.")

    print("\n✍️ AUTORES REGISTRADOS:")
    autores = cargar_datos(ARCHIVO_AUTORES)
    if autores:
        for i, autor in enumerate(autores, 1):
            print(f"\nAutor #{i}")
            print(f"  Nombre: {autor['nombre']}")
            print(f"  Nacionalidad: {autor['nacionalidad']}")
    else:
        print("No hay autores registrados.")

# Menú principal
def menu():
    inicializar_archivos()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Mostrar información")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_autor()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_informacion()
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Ejecutar programa
if __name__ == "__main__":
    menu()
