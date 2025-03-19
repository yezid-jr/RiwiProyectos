#Desarrolla un programa en Python que gestione una serie de calificaciones y estadísticas 
# de manera interactiva.
    # 1. Determinar el estado de aprobación:
    #     a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    #     b. Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
    # 2. Calcular el promedio:
    #     a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #     b. Calcular y mostrar el promedio de las calificaciones en la lista
    # 3. Contar calificaciones mayores:
    #     a. Preguntar al usuario por un valor específico
    #     b. Contar cuántas calificaciones en la lista son mayores que este valor
    # 4. Verificar y contar calificaciones específicas:
    #     a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #     b. Calcular y mostrar el promedio de las calificaciones en la lista

#Inicio: Programa de gestion de Calificaciones
###importaciones
from os import system

###Declaracion e inicializador de variables


# def validar_numero(numero):
#     try:
#         if :
#             calificacion = int(calificacion)
#             if calificacion >= 0 and calificacion <= 100:
#                 system("clear")
#                 print("\nAprobaste!\n" if calificacion > 60 else "\nNo aprobaste :(\n")
#             else:
#                 system("clear")
#                 print("\nHas ingresado una calificación NEGATIVA, Intenta de nuevo.\n")
#     except:
#             system("clear")
#             print("\nValor no valido\n")

while True:
    try:
        system("clear") #limpieza de la terminal 
        print("Programa Calificaciones")
        print("\nSeleccione una opción:\n")

        print("1. Verifica si estás aprobado.")
        print("2. Calcula tu promedio.")
        print("3. Contador de calificaciones mayores.")
        print("4. Validacion y contador de calificaciones especificas.")
        print("\nEnter any key for exit.")

        opcion = int(input())
        if opcion == 1:
            while True:
                print("Enter 's' para Ir al Menú")
                    #Validacion de input: no numeros negativos o no caracteres
                try:
                    calificacion = input("Ingrese una Calificion de 0 a 100:")
                    if calificacion == 's':
                        break
                    else:
                        calificacion = int(calificacion)
                        if calificacion >= 0 and calificacion <= 100:
                            system("clear")
                            print("\nAprobaste!\n" if calificacion > 60 else "\nNo aprobaste :(\n")
                        else:
                            system("clear")
                            print("\nHas ingresado una calificación NEGATIVA, Intenta de nuevo.\n")
                except:
                        system("clear")
                        print("\nValor no valido\n")

        elif opcion == 2:
            while True:
                system("clear")
                #Validacion de input: no numeros negativos o no caracteres
                try:
                    calificacion = int(input("Ingrese Calificacion:"))
                    if calificacion >= 0 and calificacion <= 100:
                        print("\nAprobaste!\n" if calificacion > 60 else "\nNo aprobaste :(\n")
                    else:
                        print("\nHas ingresado una calificación NEGATIVA, Intenta de nuevo.\n")
                except:
                    print("\nValor no valido\n")
        elif opcion == 3:
            while True:
                system("clear")
                #Validacion de input: no numeros negativos o no caracteres
                try:
                    calificacion = int(input("Ingrese una Calificion de 0 a 100:"))
                    if calificacion >= 0 and calificacion <= 100:
                        print("Aprobaste!" if calificacion > 60 else "No aprobaste :(")
                    else:
                        print("Has ingresado una calificación NEGATIVA, Intenta de nuevo.")
                except:
                    print("\aValor no valido")
        elif opcion == 4:
            while True:
                system("clear")
                #Validacion de input: no numeros negativos o no caracteres
                try:
                    calificacion = int(input("Ingrese una Calificion de 0 a 100:"))
                    if calificacion >= 0 and calificacion <= 100:
                        print("Aprobaste!" if calificacion > 60 else "No aprobaste :(")
                    else:
                        print("Has ingresado una calificación NEGATIVA, Intenta de nuevo.")
                except:
                    print("\aValor no valido")
    except:
        break