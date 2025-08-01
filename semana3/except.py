
try:
    frutas = int(input("ingresa la cantidad de frutas disponibles :"))
    if frutas < 0:
        raise ValueError("la cantidad de frutas no puede ser negativa")
    frutas_vendidas = int(input("ingresa la cantidad de frutas vendidas :"))
    if frutas_vendidas > frutas:
        raise ValueError("la cantidad de frutas vendidas no puede ser mayor a la cantidad de fritas disponibles")
    verduras = int(input("ingresa la cantidad de verduras disponibles :"))
    if verduras < 0:
        raise ValueError("la cantidad no puede ser negativa")
    verduras_vendidas = int(input("ingresa la cantidad de verduras vendidas :"))
    if verduras_vendidas > verduras:
        raise ValueError("la cantidad vendida no puede ser mayor a la cantidad disponible")

    total = frutas + verduras
    vendidos = frutas_vendidas + verduras_vendidas
    disponible = total - vendidos
    print (f"cantidad de frutas {frutas} ")
    print (f"cantidad de verduras {verduras}")
    print (f"total de productos  {total}")
    print (f"cantidad de productos vendidos es {vendidos}, y los productos que quedan disponibles despues de la venta es de {disponible}")

    
except ValueError as e:
    print(f"Error! {e}")
