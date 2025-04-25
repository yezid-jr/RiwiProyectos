#Enunciado Trabajo
"""Crear un programa que calcule el costo total de una compra
debe solicitar: nombre del producto, precio unitario, cantidad de productos
y un porcentaje de descuento si aplica.
El programa debe calcular el costo total de la compra primero sin descuento y luego sin descuento
y mostrar el resultado al usuario. este costo debe ser mostrado junto con el nombre del producto 
y utilizando valores con dos decimales para mayor claridad."""

### INICIO PROGRAMA
# Importar librerias
from os import system

###inicio de funciones

def menu(): #muestra el menu
    print("Bienvenido al programa de Tiendas Ara\n\n")
    print("Por favor seleccione alguna de las siguientes opciones:\n")
    print("1. Ingresar compra")
    print("2. generar factura")
    print("3. Salir")

def ingresar_compra(): #campos del producto para que el usuario pueda hacer el registro
    while True: #valida que el nombre no ingrese un producto sin nombre o vacio
        nombre_producto = input("Nombre del producto: ").strip() #ingreso del nombre del producto
        if len(nombre_producto) > 0:
            break
        else:
            print("El nombre del producto no puede estar vacío.") #en caso de que sea vacio se repite el ciclo

    precio_unitario = numero_valido(input("Precio unitario: ")) #ingreso del precio del producto
    cantidad_productos = numero_valido(input("Cantidad de productos: ")) #ingreso de la cantidad
    pregunta_descuento = input("¿Aplica descuento? ingrese 'SI' para agregar descuento, si ingresa otra respuesta el descuento NO aplicará: ").strip().lower() #pregunta de descuento si aplica
    
    if pregunta_descuento == "si": #validacion de la entrada en caso de no ser "si", el descuento toma valor de 0
        while True:
            porcentaje_descuento = numero_valido(input("Porcentaje de descuento: "))
            if porcentaje_descuento < 0 or porcentaje_descuento > 100: #validacion que el campo este entre 0 y 100
                print("El porcentaje de descuento debe estar entre 0 y 100.")
            else:
                break
    else:
        porcentaje_descuento = 0.0
        print("No aplica descuento\n\n")
    
    return nombre_producto, precio_unitario, cantidad_productos, porcentaje_descuento #retorno de todos los campos ingresados en un solo return

def mostrar_factura(nombre_producto, precio_unitario, cantidad_productos, porcentaje_descuento): #contiene la operacion para calcular descuento y los print para generar la factura
    total_sin_descuento = precio_unitario * cantidad_productos
    total_con_descuento = ((100 - porcentaje_descuento)/100) * total_sin_descuento
    if porcentaje_descuento == 0:
        descuento_mensaje = "No aplica"
    else:
        descuento_mensaje = f"{porcentaje_descuento}%"
    #prints:
    print("--" * 30)
    print("Bienvenido a Tiendas Ara".center(60))
    print(f"{'Factura de compra':^60}")
    print("-" * 60)
    print(f"{'Producto:':<30} {nombre_producto:<30}")
    print(f"{'Precio unitario:':<30} ${precio_unitario:.2f}")
    print(f"{'Cantidad:':<30} {cantidad_productos:<30}")
    print(f"{'Total sin descuento:':<30} ${total_sin_descuento:.2f}")
    print(f"{'Descuento aplicado:':<30} {descuento_mensaje}")
    print(f"\n{'Total con descuento:':<30} ${total_con_descuento:.2f}")
    print("-" * 60)
    print("Gracias por su compra".center(60))
    print("--" * 30)

def limpiar(): #reduce la manera de limpiar la terminal (esto es solo para darle un efecto de claridad en lo que se ve en la terminal)
    system("clear")

def numero_valido(numero): #valida si el numero ingresado corresponde a un numero entero positivo
    while True:
        try:
            numero = float(numero)
            if numero < 0:
                raise ValueError
            return numero
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número positivo.")
            numero = input("Ingrese nuevamente el número: ")
###Fin Funciones

limpiar() #limpia toda la terminal antes de empezar todo
while True:
    menu()
    opcion = input("\n\nSeleccione una opción: ") #obtiene la opcion ingresada en caso de no encontrarla se repetira
    
    if opcion == "1": #para ingresar productos
        limpiar()
        nombre_produ, precio, cantidad, porcentaje_des = ingresar_compra()
    elif opcion == "2": #para mostrar la factura
        limpiar()
        try:
            mostrar_factura(nombre_produ, precio, cantidad, porcentaje_des)
            salir = input("\nEnter para salir").strip() #opcion para salir de la visualizacion de la factura
            while True:
                if salir == "":
                    limpiar()
                    print("Cerrado!")
                    break
        except NameError:
            limpiar()
            print("No se han ingresado datos de compra. Por favor ingrese primero una compra.\n\n")
    elif opcion == "3": #opcion para salir del programa
        limpiar()
        print("Saliendo del programa... cerrado!")
        break
    else:
        limpiar()
        print("Opción no válida por favor intente nuevamente\n\n")
#FIN PROGRAMA