
    # Añadir productos:
    #     Cada producto debe estar definido por su nombre, precio y cantidad disponible
    #     Esta información será almacenada de modo que el inventario pueda crecer dinámicamente
    # Consultar productos:
    #     Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
    #     Si el producto no está en el inventario, se debe notificar adecuadamente
    # Actualizar precios:
    #     El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario
    # Eliminar productos:
    #     El programa debe permitir al usuario eliminar productos del inventario de manera segura
    # Calcular el valor total del inventario:
    #     El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
    #     Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.

from os import system

def imprimir_registros(lista, diccionario):  #Funcion que muestra la tabla de los registros en la lista
    print(f"{'ID':<5} {'Nombre Producto':<20}")
    print("-" * 23)
    for diccionario in lista:
        id_producto = diccionario["ID"]
        nombre_producto = diccionario["nombre"]
        print(f"{id_producto:<5} {nombre_producto:<20}")

def menu():  #Funcion que muestra el menu
    print("""\nOPCIONES INVENTARIO
        \nSeleccione una opción:\n
    1. Añadir Productos.
    2. Consultar Productos.
    3. Actualizar Precios.
    4. Eliminar Productos.
    5. Calcular el valor total del inventario.
        \nEnter any key for exit. """)

def numero_valido(numero): #Validacion de numero
    try:
        numero = float(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
        return False

def numero_correcto(msg): #Validacion de entrada, parameptros: mensaje para pedir el numero
     while True: 
        numero = input(msg) #Entrada de datos: El usuario digita el ID para poder realizar la busqueda
        if numero_valido(numero):
            return float(numero)
        else:
            print("\nPor favor, ingrese un numero valido.")

def mostrar_listaa(diccionario, listas, numero):
    system("clear")
    imprimir_registros(listas, diccionario)
    sw = False
    while True:
        if numero  == diccionario["ID"]:
            id_producto = diccionario["ID"]
            nombre_producto = diccionario["nombre"]
            precio_producto = diccionario["precio"]
            stok_producto = diccionario["stock"]
            print("\nDETALLES DEL PRODUCTO:\n")
            print("-" * 67)
            print(f"{'ID':<5} {'Nombre Producto':<20} {'Precio Unitario':<20}{'Cantidad disponible':<20}")
            print("-" * 67)
            print(f"{id_producto:<5} {nombre_producto:<20} {precio_producto:<20} {stok_producto:<20}")
            print("-" * 67)
            sw = True
            return sw, nombre_producto
        else: 
            print("Producto no encontrado, intente nuevamente")
            break

### Creacion de variables
productos = []
producto = {}
ir_inicio = 's'
contador = 0
num_valido = True
valor_total = 0

### opciones del aplicativo interaccional

while True: 
    try:
        system("clear")
        menu()
        opcion = int(input())
        
        if opcion == 1: #OPCION 1: Añadir productos

            while True:
                system("clear")
                print("Agregar Producto\n")
                
                nombre = input("Nombre:")
                precio = numero_correcto("Precio:")
                stock = numero_correcto("Cantidades:")
                contador += 1

                producto = {"ID": contador, "nombre": nombre, "precio": precio, "stock": stock}
                productos.append(producto)

                print("Producto ingresado con EXITO")
                ir_inicio = input("Desea ingresar otro producto? S / N(volver al MENU)")
                ir_inicio.lower #Todo texto ingresado es parceado a minusculas

                if ir_inicio == 's': #Salida del punto
                    continue
                break
                
        elif opcion == 2: #OPCION 2: Consultar producto
            if len(productos) == 0:
                system("clear")
                print("No hay Productos ingresados, Por favor ingrese Productos en el menú principal en la opcion '1'")
                preciona_ok = input("\fPresione ENTER para regresar al menu")
            else:
                while True:   
                    system("clear")

                    
                    imprimir_registros(productos, producto)

                    consulta_producto = numero_correcto("\nDigite numero de ID para consultar un producto:") #Entrada de datos: El usuario digita el ID para poder realizar la busqueda
                            
                    producto_encontrado, nombre_producto = mostrar_listaa(producto, productos, consulta_producto)

                    if producto_encontrado == False:
                        print("No Existe ese ID, consulte otro")
                    ir_inicio = input("\nDesea consultar otro producto? s / n(volver al MENU)")
                    ir_inicio.lower #Todo texto ingresado es parceado a minusculas
                    producto_encontrado = False

                    if ir_inicio == 's': #Salida del punto
                        continue
                    break

        elif opcion == 3: #OPCION 3: Listas mayores a un valor de entrada.
            if len(productos) == 0:
                system("clear")
                print("No hay Productos ingresados, Por favor ingrese Productos en el menú principal en la opcion '1'")
                preciona_ok = input("\fPresione ENTER para regresar al menu")
            else:
                system("clear")
                imprimir_registros(productos, producto) # Imprime los registros de la lista 
                while True:   
                    
                    consulta_producto = numero_correcto("\nDigite numero de ID para consultar un producto:")
                      
                    producto_encontrado, nombre_producto = mostrar_listaa(producto, productos, consulta_producto)
                    

                    cambio_precio = numero_correcto(f"Ingrese el nuevo precio del producto '{nombre_producto}':")
                    producto["precio"] = cambio_precio
                    
                    ir_inicio = input("\nDesea consultar otro producto? s / n(volver al MENU)")
                    ir_inicio.lower #Todo texto ingresado es parceado a minusculas
                    producto_encontrado = False

                    if ir_inicio == 's': #Salida del punto
                        continue
                    break
            
        elif opcion == 4: #OPCION 4: Calcular el valor total del inventario

            if len(productos) == 0:
                system("clear")
                print("No hay Productos ingresados, Por favor ingrese Productos en el menú principal en la opción '1'")
                input("Presione ENTER para regresar al menu")
            else:
                # Usamos lambda y map() para calcular el valor total
                valor_total = sum(map(lambda x: x["precio"] * x["stock"], productos))

                print(f"\nEl valor total del inventario es: {valor_total}")
                input("\nPresione ENTER para volver al menú.")
        
        elif opcion == 5: #OPCION 4: Calcular el valor total del inventario

            if len(productos) == 0:
                system("clear")
                print("No hay Productos ingresados, Por favor ingrese Productos en el menú principal en la opción '1'")
                input("Presione ENTER para regresar al menu")
            else:
                # Usamos lambda y map() para calcular el valor total
                valor_total = sum(map(lambda x: x["precio"] * x["stock"], productos))

                print(f"\nEl valor total del inventario es: {valor_total}")
                input("\nPresione ENTER para volver al menú.")
            
    except:
        break
# system("clear")
# print("Has Salido del programa!")
