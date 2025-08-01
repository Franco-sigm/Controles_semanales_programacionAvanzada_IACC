from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from db_config import create_connection

# ---------------------- FUNCIONES ---------------------- #

def agregar_videojuego():
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    clasificacion = entry_clasificacion.get()
    plataforma = entry_plataforma.get()

    if not (titulo and genero and clasificacion and plataforma):
        messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO videojuegos (titulo, genero, clasificacion, plataforma) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (titulo, genero, clasificacion, plataforma))
    conn.commit()
    conn.close()

    limpiar_campos()
    mostrar_videojuegos()

def mostrar_videojuegos():
    listbox.delete(0, tk.END)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videojuegos")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    conn.close()

def eliminar_videojuego():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Selección requerida", "Selecciona un videojuego para eliminar.")
        return

    item = listbox.get(seleccion)
    id_vj = item.split(" | ")[0]

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM videojuegos WHERE id = %s", (id_vj,))
    conn.commit()
    conn.close()
    mostrar_videojuegos()

def actualizar_videojuego():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Selección requerida", "Selecciona un videojuego para actualizar.")
        return

    item = listbox.get(seleccion)
    id_vj = item.split(" | ")[0]

    nuevo_titulo = entry_titulo.get()
    nuevo_genero = entry_genero.get()
    nueva_clasificacion = entry_clasificacion.get()
    nueva_plataforma = entry_plataforma.get()

    if not (nuevo_titulo and nuevo_genero and nueva_clasificacion and nueva_plataforma):
        messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos para actualizar.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    query = """
        UPDATE videojuegos 
        SET titulo = %s, genero = %s, clasificacion = %s, plataforma = %s 
        WHERE id = %s
    """
    cursor.execute(query, (nuevo_titulo, nuevo_genero, nueva_clasificacion, nueva_plataforma, id_vj))
    conn.commit()
    conn.close()
    mostrar_videojuegos()
    limpiar_campos()

def limpiar_campos():
    entry_titulo.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_clasificacion.delete(0, tk.END)
    entry_plataforma.delete(0, tk.END)

# ---------------------- INTERFAZ ---------------------- #

root = tk.Tk()
root.title("🎮 Gestión de Videojuegos")
root.configure(bg="#2c3e50")
root.geometry("800x600")  # Ventana inicial más amplia

# Permitir expansión al redimensionar
for i in range(2):
    root.columnconfigure(i, weight=1)
for i in range(8):
    root.rowconfigure(i, weight=1)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2c3e50", foreground="white", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"), padding=6)

# Título
titulo = ttk.Label(root, text="Gestión de Videojuegos", font=("Arial", 16, "bold"), anchor="center")
titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

# Campos
ttk.Label(root, text="🎮 Título:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_titulo = ttk.Entry(root)
entry_titulo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(root, text="📁 Género:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_genero = ttk.Entry(root)
entry_genero.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(root, text="🎯 Clasificación:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_clasificacion = ttk.Entry(root)
entry_clasificacion.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(root, text="🕹️ Plataforma:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_plataforma = ttk.Entry(root)
entry_plataforma.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Botones
frame_botones = tk.Frame(root, bg="#2c3e50")
frame_botones.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

btn_agregar = ttk.Button(frame_botones, text="Agregar", command=agregar_videojuego)
btn_agregar.pack(side="left", expand=True, fill="x", padx=5)

btn_actualizar = ttk.Button(frame_botones, text="Actualizar", command=actualizar_videojuego)
btn_actualizar.pack(side="left", expand=True, fill="x", padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=eliminar_videojuego)
btn_eliminar.pack(side="left", expand=True, fill="x", padx=5)

btn_limpiar = ttk.Button(frame_botones, text="Limpiar", command=limpiar_campos)
btn_limpiar.pack(side="left", expand=True, fill="x", padx=5)

# Lista
listbox = tk.Listbox(root, font=("Courier New", 10))
listbox.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Scroll para la lista
scrollbar = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
scrollbar.grid(row=6, column=2, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)

# Cargar datos al iniciar
mostrar_videojuegos()

root.mainloop()
