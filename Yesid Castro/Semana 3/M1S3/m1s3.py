
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

def menu():  #Funcion que muestra el menu
    print("\n\nOPCIONES INVENTARIO")
    print("\nSeleccione una opción:\n")

    print("1. Añadir Productos.")
    print("2. Consultar Productos.")
    print("3. Actualizar Precios.")
    print("4. Calcular el valor total del inventario.")
    print("\nEnter any key for exit.")

system("clear")

### Creacion de variables
productos = []
producto = {}
### opciones del aplicativo interaccional

while True: 
    try:
        menu()
        opcion = int(input())
        system("clear")
        if opcion == 1: #OPCION 1: Verifica si está aprobado
            print("Agregar Producto\n")
            nombre = input("Nombre:")
            precio = input("Precio:")
            stock = input("Cantidades:")
            
            ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
            if ir_inicio.lower() == "s":
                continue
            raise ValueError

        elif opcion == 2: #OPCION 2: Calcula el promedio de una secuencia de numeros dadas por ',' coma

            
            ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
            if ir_inicio.lower() == "s":
                continue
            raise ValueError

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
system("clear")
print("Has Salido del programa!")
