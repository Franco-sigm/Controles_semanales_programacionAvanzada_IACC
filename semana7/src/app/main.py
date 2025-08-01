import tkinter as tk
from tkinter import messagebox

def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    genero = genero_var.get()
    categorias = []
    if var_novela.get(): categorias.append("Novela")
    if var_ciencia.get(): categorias.append("Ciencia")
    if var_historia.get(): categorias.append("Historia")
    estado = estado_var.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = idioma_var.get()

    print("=== Detalles del Libro Registrado ===")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año: {anio}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias)}")
    print(f"Estado: {estado}")
    print(f"Copias: {copias}")
    print(f"Resumen: {resumen}")
    print(f"Idioma: {idioma}")
    print("====================================")

def limpiar_formulario():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    genero_var.set(None)
    var_novela.set(False)
    var_ciencia.set(False)
    var_historia.set(False)
    estado_var.set(None)
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    idioma_var.set(opciones_idioma[0])

# Ventana principal
root = tk.Tk()
root.title("Biblioteca SaberX")

# Frame - Detalles del libros
frame_detalles = tk.LabelFrame(root, text="Detalles del Libro", padx=10, pady=10)
frame_detalles.pack(padx=10, pady=5, fill="x")

tk.Label(frame_detalles, text="Título:").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_detalles)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0)
entry_autor = tk.Entry(frame_detalles)
entry_autor.grid(row=1, column=1)

tk.Label(frame_detalles, text="Año:").grid(row=2, column=0)
entry_anio = tk.Entry(frame_detalles)
entry_anio.grid(row=2, column=1)

# Frame - Género y Categoría
frame_genero = tk.LabelFrame(root, text="Género y Categoría", padx=10, pady=10)
frame_genero.pack(padx=10, pady=5, fill="x")

genero_var = tk.StringVar()
tk.Radiobutton(frame_genero, text="Ficción", variable=genero_var, value="Ficción").grid(row=0, column=0)
tk.Radiobutton(frame_genero, text="No Ficción", variable=genero_var, value="No Ficción").grid(row=0, column=1)

var_novela = tk.BooleanVar()
var_ciencia = tk.BooleanVar()
var_historia = tk.BooleanVar()
tk.Checkbutton(frame_genero, text="Novela", variable=var_novela).grid(row=1, column=0)
tk.Checkbutton(frame_genero, text="Ciencia", variable=var_ciencia).grid(row=1, column=1)
tk.Checkbutton(frame_genero, text="Historia", variable=var_historia).grid(row=1, column=2)

# Frame - Estado
frame_estado = tk.LabelFrame(root, text="Estado del Libro", padx=10, pady=10)
frame_estado.pack(padx=10, pady=5, fill="x")

estado_var = tk.StringVar()
tk.Radiobutton(frame_estado, text="Disponible", variable=estado_var, value="Disponible").pack(side="left")
tk.Radiobutton(frame_estado, text="Prestado", variable=estado_var, value="Prestado").pack(side="left")

# Frame - Copias
frame_copias = tk.LabelFrame(root, text="Número de Copias", padx=10, pady=10)
frame_copias.pack(padx=10, pady=5, fill="x")

tk.Label(frame_copias, text="Copias:").pack(side="left")
entry_copias = tk.Entry(frame_copias)
entry_copias.pack(side="left")

# Frame - Resumen
frame_resumen = tk.LabelFrame(root, text="Resumen del Libro", padx=10, pady=10)
frame_resumen.pack(padx=10, pady=5, fill="x")

tk.Label(frame_resumen, text="Resumen:").pack(anchor="w")
text_resumen = tk.Text(frame_resumen, height=5)
text_resumen.pack(fill="x")

# Menú desplegable
frame_idioma = tk.LabelFrame(root, text="Idioma del Libro", padx=10, pady=10)
frame_idioma.pack(padx=10, pady=5, fill="x")

opciones_idioma = ["Español", "Inglés"]
idioma_var = tk.StringVar(value=opciones_idioma[0])
menu_idioma = tk.OptionMenu(frame_idioma, idioma_var, *opciones_idioma)
menu_idioma.pack()

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Registrar Libro", command=registrar_libro).pack(side="left", padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario).pack(side="left", padx=5)

root.mainloop()
