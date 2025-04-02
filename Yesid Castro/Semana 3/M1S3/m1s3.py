
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
    print("\nOPCIONES INVENTARIO")
    print("\nSeleccione una opción:\n")

    print("1. Añadir Productos.")
    print("2. Consultar Productos.")
    print("3. Actualizar Precios.")
    print("4. Calcular el valor total del inventario.")
    print("\nEnter any key for exit.")

def numero_valido(numero): #Validacion de numero
    try:
        numero = float(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
        return False
    
def msj_numero_valido_o_no (swich):
    if swich == False:
        print("Por favor, ingrese un numero valido.")


### Creacion de variables
productos = []
producto = {}
ir_inicio = 's'
contador = 0
producto_encontrado = False
num_valido = True

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

                while True: #Validacion de entrada
                    msj_numero_valido_o_no(num_valido)
                    precio = input("Precio:")
                    num_valido = numero_valido(precio)
                    if num_valido:
                        float(precio)
                        break
                
                while True: #Validacion de entrada
                    msj_numero_valido_o_no(num_valido)
                    stock = input("Cantidades:")
                    num_valido = numero_valido(stock)
                    if num_valido:
                        float(stock)
                        break

                contador += 1
                producto = {"ID": contador, "nombre": nombre, "precio": precio, "stock": stock}
                productos.append(producto)

                print("Producto ingresado con EXITO")
                ir_inicio = input("Desea ingresar otro producto? S / N(volver al MENU)")
                ir_inicio.lower #Todo texto ingresado es parceado a minusculas

                if ir_inicio == 's': #Salida del punto
                    continue
                break
                
        elif opcion == 2: #OPCION 2: Consultar productos
            while True:   
                system("clear")
                
                # Imprime los registros de la lista 
                imprimir_registros(productos, producto)

                consulta_producto = int(input("\nDigite numero de ID para consultar un producto:")) #Entrada de datos: El usuario digita el ID para poder realizar la busqueda

                for producto in productos:
                    if consulta_producto == producto["ID"]:
                        producto_encontrado == True
                        break
                    
                ir_inicio = input("Desea consultar otro producto? s / n(volver al MENU)")
                ir_inicio.lower #Todo texto ingresado es parceado a minusculas

                if ir_inicio == 's': #Salida del punto
                    continue
                break

        elif opcion == 3: #OPCION 3: Listas mayores a un valor de entrada.
            
            
            ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
            if ir_inicio.lower() == "s":
                continue
            raise ValueError
        
        elif opcion == 4: #OPCION 4: Ingresar nuevamente calificaciones

            ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
            if ir_inicio.lower() == "s":
                continue
            raise ValueError
            
    except:
        break
# system("clear")
# print("Has Salido del programa!")
