#función par aplicar descuentos con manejo de errores try catch
def descuentos():
    precio = 50.0

    cantidad = int(input("Ingresa la cantidad de licencias que necesitas (precio 50$)"))
    total_compra = precio * cantidad
    try:
        if cantidad >= 3:
            descuento = (total_compra * 20) / 100
            precio_final = total_compra - descuento
            print(f"Se aplico un descuento de un 20% por un monto de {descuento}. total a pagar :{precio_final}")
        elif cantidad >= 5:
            descuento = (total_compra * 30) / 100
            precio_final = total_compra - descuento
            print(f"Se aplico un descuento de un 30% por un monto de {descuento}. total a pagar :{precio_final}")
        else:
            print(f"total a pagar {total_compra}")
    except ValueError:
        print("Error! recuerda que debes ingresar la cantidad en numeros ")

#función para calcular área de una esfera
def volumen_esfera():
    pi = 3.1416
    try:
        radio = float(input("ingresa el valor del radio :"))
        volumen = (4/3) *pi*(radio*radio*radio)
        print(f"El vomlumen de tu circulo es de :{volumen:.3f}")
    except ValueError:
        print("Error! ingresa numeros validos por favor ")

#meú de opciones con manejo de errores try catch
def menu():
    print ("Bien venido al menú!")
    print("")
    print("1 calcular descuentos de compras")
    print("2 calcular volumen de una esfera ")
    print("3 Salir")
    print("")
    while True:
        try:
            opcion = int(input("ingrese una opcion del 1 al 3 :"))
            if opcion == 1:
                descuentos()
            elif opcion == 2:
                volumen_esfera()
            elif opcion == 3:
                print("Saliendo del sistema. Hasta pronto!")
                break
        except ValueError:
            print("Error! ingresa numeros enteros del 1 al 3")

#función principal 
if __name__ == "__main__":
    menu()
            
