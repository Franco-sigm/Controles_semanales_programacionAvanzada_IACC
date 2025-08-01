from database.conexion import conectar
import tkinter as tk
from tkinter import ttk



#

def agregar_paciente(paciente):
    con = conectar()
    cursor = con.cursor()
    sql = "INSERT INTO Pacientes (Nombre, Edad, Genero, HistorialMedico, Contacto) VALUES (%s, %s, %s, %s, %s)"
    valores = (paciente.nombre, paciente.edad, paciente.genero, paciente.historial, paciente.contacto)
    cursor.execute(sql, valores)
    con.commit()
    con.close()
    
    
def obtener_pacientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Pacientes")
    pacientes = cursor.fetchall()
    con.close()
    return pacientes


def actualizar_paciente(id_paciente, paciente):
    con = conectar()
    cursor = con.cursor()
    sql = "UPDATE Pacientes SET Nombre=%s, Edad=%s, Genero=%s, HistorialMedico=%s, Contacto=%s WHERE ID=%s"
    valores = (paciente.nombre, paciente.edad, paciente.genero, paciente.historial, paciente.contacto, id_paciente)
    cursor.execute(sql, valores)
    con.commit()
    con.close()


def eliminar_paciente(id_paciente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pacientes WHERE ID = %s", (id_paciente,))
    conn.commit()
    conn.close()


def limpiar_campos(entries):
    for campo in entries.values():
        if isinstance(campo, tk.Entry):
            campo.delete(0, tk.END)
        elif isinstance(campo, tk.Text):
            campo.delete("1.0", tk.END)
