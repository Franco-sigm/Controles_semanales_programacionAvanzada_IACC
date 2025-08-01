import empleados
import calculoBonos
import mostrarResultados


def main():
    empleado_registro = empleados.Empleado.registrar_empleado()
    beneficios = calculoBonos.calcular_bono(empleado_registro)
    resultado = mostrarResultados.mostrarResultado(empleado_registro, beneficios)

    print(resultado)

if __name__ == "__main__":
    main()