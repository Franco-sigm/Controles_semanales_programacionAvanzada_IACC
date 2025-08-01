import os
import platform
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from tkinter import messagebox
from datetime import datetime
from database.conexion import conectar  # Asegúrate de que esté bien configurado

def generar_informe_pdf():
    try:
        # Conectar a la base de datos
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        registros = cursor.fetchall()

        if not registros:
            messagebox.showinfo("Informe", "No hay datos en la tabla pacientes.")
            return

        # Preparar archivo PDF
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"informe_pacientes_{timestamp}.pdf"
        ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)

        c = canvas.Canvas(ruta_archivo, pagesize=letter)
        width, height = letter

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Informe de Pacientes")
        c.setLineWidth(1)
        c.line(50, height - 55, width - 50, height - 55)

        # Encabezados de tabla
        columnas = ["ID", "Nombre", "Edad", "Género", "Historial", "Contacto"]
        c.setFont("Helvetica-Bold", 10)
        y = height - 80
        x = 50
        col_widths = [50, 120, 50, 60, 180, 100]

        for i, col in enumerate(columnas):
            c.drawString(x, y, col)
            x += col_widths[i]

        y -= 15
        c.setFont("Helvetica", 9)

        # Filas de datos
        for fila in registros:
            x = 50
            for i, valor in enumerate(fila):
                c.drawString(x, y, str(valor))
                x += col_widths[i]
            y -= 15

            if y < 50:  # salto de página si se llega al final
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 9)

        c.save()

        # Mensaje de éxito ANTES de abrir el archivo
        messagebox.showinfo("Reporte generado con éxito", "¡Reporte generado con éxito!\nHaz clic en 'Aceptar' para visualizarlo.")

        # Abrir PDF automáticamente según el sistema
        sistema = platform.system()
        try:
            if sistema == "Windows":
                os.startfile(ruta_archivo)
            elif sistema == "Darwin":  # macOS
                os.system(f"open '{ruta_archivo}'")
            elif sistema == "Linux":
                os.system(f"xdg-open '{ruta_archivo}'")
            else:
                messagebox.showinfo("Aviso", f"Informe generado, pero no se pudo abrir automáticamente en {sistema}.")
        except Exception as abrir_error:
            messagebox.showwarning("Aviso", f"Informe generado, pero no se pudo abrir automáticamente: {abrir_error}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error en la base de datos: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el informe: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()
