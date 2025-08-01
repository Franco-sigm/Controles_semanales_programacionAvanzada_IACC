print("calculador de precio de llantas")

numero_llantas = int(input("ingrese la cantidad de llantas que desea comprar: "))

if numero_llantas < 5:
    precio = numero_llantas * 35000
elif numero_llantas >= 5:
    precio = numero_llantas * 40000
else:
    precio = numero_llantas * 45000

print(f"el precio final es de {precio}")
