from datetime import datetime

mensajebonoMayor = "bono anual de $1000"
mensajebonoMenor = "5 días extra de vacaciones"
#clacular bono segun antiguedad

def calcular_bono(empleado):
    fecha_actual = datetime.now()
    antiguedad = (fecha_actual - empleado.fecha_de_ingreso).days // 365

    if antiguedad >= 5:
        beneficio = mensajebonoMayor
    elif antiguedad >= 3:
        beneficio = mensajebonoMenor
    else:
        beneficio = "No hay beneficios asignados"

    return f"Antigüedad: {antiguedad} años\n" \
           f"Beneficios asignados: {beneficio}"