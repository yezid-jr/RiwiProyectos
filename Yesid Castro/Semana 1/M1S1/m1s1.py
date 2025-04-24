"""Crear un programa que calcule el costo total de una compra
debe solicitar: nombre del producto, precio unitario, cantidad de productos
y un porcentaje de descuento si aplica.
El programa debe calcular el costo total de la compra primero sin descuento y luego sin descuento
y mostrar el resultado al usuario. este costo debe ser mostrado junto con el nombre del producto 
y utilizando valores con dos decimales para mayor claridad."""

# INICIO PROGRAMA

# Importar librerias
from os import system
system("clear")
# Definicion de funciones

def menu():
    print("Bienvenido al programa de Tiendas Ara\n\n")
    print("Por favor ingrese los siguientes datos:\n")
    print("1. Ingresar compra")
    print("2. generar factura")
    print("3. Salir")

def ingresar_compra():
    nombre_producto = input("Nombre del producto: ")
    precio_unitario = numero_valido(input("Precio unitario: "))
    cantidad_productos = numero_valido(input("Cantidad de productos: "))
    pregunta_descuento = input("¿Aplica descuento? (si/no): ").strip().lower()
    
    if pregunta_descuento == "si":
        while True:
            porcentaje_descuento = numero_valido(input("Porcentaje de descuento: "))
            if porcentaje_descuento < 0 or porcentaje_descuento > 100:
                print("El porcentaje de descuento debe estar entre 0 y 100.")
            else:
                break
    else:
        porcentaje_descuento = 0.0
        print("No aplica descuento\n\n")
    
    return nombre_producto, precio_unitario, cantidad_productos, porcentaje_descuento

def mostrar_factura(nombre_producto, precio_unitario, cantidad_productos, porcentaje_descuento):
    total_sin_descuento = precio_unitario * cantidad_productos
    total_con_descuento = (100 - porcentaje_descuento) * total_sin_descuento
    if porcentaje_descuento == 0:
        descuento_mensaje = "No aplica"
    else:
        descuento_mensaje = f"{porcentaje_descuento}%"

    print("--" * 30)
    print("Bienvenido a Tiendas Ara".center(60))
    print(f"{'Factura de compra':^60}")
    print("-" * 60)
    print(f"{'Producto:':<20} {nombre_producto:<30}")
    print(f"{'Precio unitario:':<20} ${precio_unitario:.2f}")
    print(f"{'Cantidad:':<20} {cantidad_productos:<30}")
    print(f"{'Total sin descuento:':<20} ${total_sin_descuento:.2f}")
    print(f"{'Descuento aplicado:':<20} {descuento_mensaje}")
    print(f"\n{'Total con descuento:':<20} ${total_con_descuento:.2f}")
    print("-" * 60)
    print("Gracias por su compra".center(60))
    print("--" * 30)

def limpiar():
    system("clear")

def numero_valido(numero):
    while True:
        try:
            numero = float(numero)
            if numero < 0:
                raise ValueError
            return numero
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número positivo.")
            numero = input("Ingrese nuevamente el número: ")
            continue



# Inicio del programa
while True:
    menu()
    opcion = input("\n\nSeleccione una opción: ")
    
    if opcion == "1":
        limpiar()
        nombre_produ, precio, cantidad, porcentaje_des = ingresar_compra()
    elif opcion == "2":
        try:
            mostrar_factura(nombre_produ, precio, cantidad, porcentaje_des)
            salir = input("\nEnter para salir")
            while True:
                if salir == "":
                    limpiar()
                    print("Cerrado!")
                    break
        except NameError:
            limpiar()
            print("No se han ingresado datos de compra. Por favor ingrese primero una compra.\n\n")
    elif opcion == "3":
        limpiar()
        print("Saliendo del programa... cerrado!")
        break
    else:
        limpiar()
        print("Opción no válida por favor intente nuevamente\n\n")











#FIN PROGRAMA