import tkinter as tk
from tkinter import ttk
from models.paciente_model import Paciente
from controllers.pacientes_controller import agregar_paciente, obtener_pacientes, actualizar_paciente, eliminar_paciente, limpiar_campos
from services.informes import generar_informe_pdf

def iniciar_gui():
    
    # Inicializar ventana
    ventana = tk.Tk()
    ventana.title("Registro de Pacientes - SaludTotal")
    ventana.geometry("1000x650")
    ventana.resizable(True, True)
    ventana.configure(bg="#e0f2f1")  # Fondo suave
 
    # grid responsivo
    for i in range(4):
        ventana.columnconfigure(i, weight=1)
    for i in range(9):
        ventana.rowconfigure(i, weight=0)
    ventana.rowconfigure(8, weight=1)  # Fila para la tabla de pacientes

    # Estilo de etiquetas y entradas
    label_style = {"bg": "#E2F4F4", "fg": "#004d40", "font": ("Segoe UI", 10, "bold")}
    entry_style = {"font": ("Segoe UI", 10)}

    # Título de la ventana
    tk.Label(
    ventana,
    text="🩺 Registro Clínico de Pacientes",
    anchor="w",
    bg="#e0f2f1",
    fg="#004d40",
    font=("Segoe UI", 16, "bold")
    ).grid(row=0, column=0, columnspan=4, pady=15, sticky="w", padx=20)

    # Formulario
    campos = [
        ("👤 Nombre:", "nombre"),
        ("🎂 Edad:", "edad"),
        ("🚻 Género:", "genero"),
        ("📋 Historial Médico:", "historial"),
        ("📞 Contacto:", "contacto")
    ]

    entries = {}
    for i, (label_text, key) in enumerate(campos, start=1):
        tk.Label(ventana, text=label_text, **label_style).grid(row=i, column=0, sticky="e", padx=10, pady=5)

        if key == "historial":
            entry = tk.Text(ventana, width=40, height=4, wrap="word", font=("Segoe UI", 10))
            entry.grid(row=i, column=1, columnspan=2, sticky="we", padx=10, pady=5)
        else:
            entry = tk.Entry(ventana, **entry_style)
            entry.grid(row=i, column=1, sticky="we", padx=10, pady=5)

        entries[key] = entry

# Funciones CRUD
    def guardar():
        paciente = Paciente(
            entries["nombre"].get(),
            int(entries["edad"].get()),
            entries["genero"].get(),
            entries["historial"].get("1.0", tk.END),
            entries["contacto"].get()
         )
        agregar_paciente(paciente)
        mostrar_pacientes()
        limpiar_campos(entries)
       


    def modificar_paciente(item):
        if not item:
            return
        id_paciente = tabla.item(item, "values")[0]
        paciente = Paciente(
            entries["nombre"].get(),
            int(entries["edad"].get()),
            entries["genero"].get(),
            entries["historial"].get("1.0", tk.END),
            entries["contacto"].get()
        )
        actualizar_paciente(id_paciente, paciente)
        mostrar_pacientes()
        limpiar_campos(entries)
        

    
    def eliminar_paciente_gui():
        seleccion = tabla.selection()
        if not seleccion:
            return
        id_paciente = tabla.item(seleccion[0], "values")[0]
        eliminar_paciente(id_paciente)
        mostrar_pacientes()

    
    boton_style = {"font": ("Segoe UI", 10, "bold"), "bg": "#00796b", "fg": "white", "activebackground": "#004d40", "width": 18}

    tk.Button(ventana, text="💾 Guardar Paciente", command=guardar, **boton_style).grid(row=6, column=0, pady=10, padx=5)
    tk.Button(ventana, text="🔁 Actualizar Paciente", command=lambda: modificar_paciente(tabla.selection()), **boton_style).grid(row=6, column=1, pady=10, padx=5)
    tk.Button(ventana, text="🗑️ Eliminar Paciente", command=eliminar_paciente_gui, **boton_style).grid(row=6, column=2, pady=10, padx=5)
    tk.Button(ventana, text="Generar informe PDF", command=generar_informe_pdf, **boton_style).grid(row=6, column=3, pady=10, padx=5)
    # Separador

    ttk.Separator(ventana, orient='horizontal').grid(row=7, column=0, columnspan=4, sticky="ew", pady=10)

    # Tabla de pacientes
    columnas = ("ID", "Nombre", "Edad", "Género", "Historial", "Contacto")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=12)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
    estilo.configure("Treeview", font=("Segoe UI", 9), rowheight=25)

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150, stretch=True)
    tabla.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def mostrar_pacientes():
        for fila in tabla.get_children():
            tabla.delete(fila)
        for p in obtener_pacientes():
            tabla.insert("", tk.END, values=p)
    mostrar_pacientes()
    ventana.mainloop()
