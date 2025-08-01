from datetime import datetime

class Empleado:
    def __init__(self, nombre, fecha_de_ingreso, salario):
        self.nombre = nombre
        self.fecha_de_ingreso = fecha_de_ingreso
        self.salario = salario
        self.fecha_de_ingreso = fecha_de_ingreso
    

    @classmethod
    def registrar_empleado(cls):
        while True:
            try:
                print("*----------------------------------------------*\n")
                print("🟠 Bienvenido al sistema de Orange Solutions 🟠\n")
                nombre = input("Nombre: ")
                if not nombre.strip():
                    raise ValueError("El nombre no puede estar vacío.")
                fecha_str = input("Fecha de ingreso (YYYY-MM-DD): ")
                if not fecha_str.strip():
                    raise ValueError("La fecha de ingreso no puede estar vacía.")
                salario = float(input("Salario: "))
                if not salario or salario < 0:
                    raise ValueError("El salario debe ser un número positivo.")
                fecha_de_ingreso = datetime.strptime(fecha_str, "%Y-%m-%d")
                if fecha_de_ingreso > datetime.now():
                    raise ValueError("La fecha de ingreso no puede ser futura.")
                empleado = cls(nombre, fecha_de_ingreso, salario)
                return empleado
            except ValueError as e:
                print(f"Error al registrar el empleado: {e}. Inténtalo de nuevo.")
