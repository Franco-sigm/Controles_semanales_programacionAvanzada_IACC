import pickle

@staticmethod
def guardar_autores(autor):
    datos_autor = {
        "nombre": autor.nombre,
        "edad": autor.edad,
        "nacionalidad": autor.nacionalidad
    }
    try:
        with open("autores.pkl", "rb") as archivo:
            autores_existentes = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        autores_existentes = []

    autores_existentes.append(datos_autor)

    with open("autores.pkl", "wb") as archivo:
        pickle.dump(autores_existentes, archivo)

@staticmethod
def mostrar_autores():
    try:
        with open("autores.pkl", "rb") as archivo:
            autores = pickle.load(archivo)
            print("\n📚 Autores registrados:")
            for autor in autores:
                print(f"👤 Nombre: {autor['nombre']} | Edad: {autor['edad']} | Nacionalidad: {autor['nacionalidad']}")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'autores.pkl'. Aún no hay autores guardados.")
    except EOFError:
        print("⚠️ El archivo 'autores.pkl' está vacío.")

@staticmethod
def guardar_libro(libro):
    datos_libro = {
        "titulo": libro.titulo,
        "anio_publicacion": libro.anio_publicacion
    }
    try:
        with open("libros.pkl", "rb") as archivo:
            libros_existentes = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        libros_existentes = []

    libros_existentes.append(datos_libro)

    with open("libros.pkl", "wb") as archivo:
        pickle.dump(libros_existentes, archivo)

@staticmethod
def mostrar_libros():
    try:
        with open("libros.pkl", "rb") as archivo:
            libros = pickle.load(archivo)
            print("\n📚 Libros guardados:")
            for libro in libros:
                print(f"📖 Título: {libro['titulo']} | Año: {libro['anio_publicacion']}")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'libros.pkl'. Aún no hay libros guardados.")
    except EOFError:
        print("⚠️ El archivo 'libros.pkl' está vacío.")