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
contador = 0
lista_se_rompe = False
lista_usuario = []

### Declaracion de Funciones:
def validar_numero(numero): #Funcion que retorna T/F para verificar que es un caracter numerico
    try:
        numero = float(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
            return False

def menu():  #Funcion que muestra el menu
    system("clear") #limpieza de la terminal 
    print("Programa Calificaciones")
    print("\nSeleccione una opción:\n")

    print("1. Verifica si estás aprobado.")
    print("2. Calcula tu promedio.")
    print("3. Contador de calificaciones mayores.")
    print("4. Validacion y contador de calificaciones especificas.")
    print("\nEnter any key for exit.")

def lista_usuarios(): #Funcion que guarda la lista del usuario
    while True:
        numero_calificaciones = input("Ingrese sus calificaciones separadas por ','(Coma):")
        lista_calificaciones = numero_calificaciones.split(",")
        tamaño_lista = len(lista_calificaciones)
        for i in range(tamaño_lista):
            es_valido = validar_numero(lista_calificaciones[i])
            if es_valido == False:
                print(f"El programa a detectado un numero invalido. '{lista_calificaciones[i]}' Saliendo de la lista...")
                lista_se_rompe = True
                break

        if lista_se_rompe == False:
            lista_usuario = lista_calificaciones

### opciones del aplicativo interaccional
while True:
    try:
        menu()
        opcion = int(input())
        system("clear")
        if opcion == 1: #OPCION 1: Verifica si está aprobado
            while True:
                print("Enter 's' para Ir al Menú")
                calificacion = input("Ingrese una Calificion de 0 a 100:")
                es_valido = validar_numero(calificacion)
                if (es_valido and float(calificacion) <= 100) or calificacion == 's':
                    if calificacion == 's':
                        menu()
                        break
                    else:
                        system("clear")
                        print("Tu calificacion: ",calificacion)
                        print("\nAprobaste!\n" if float(calificacion) > 60 else "\nNo Aprobaste :(\n")
                        
                else:
                    system("clear")
                    print("\ningresa numero valido\n")

        elif opcion == 2: #OPCION 2: Calcula el promedio de una secuencia de numeros dadas por ',' coma
            while True:
                numero_calificaciones = input("Ingrese sus calificaciones separadas por ','(Coma):")
                lista_calificaciones = numero_calificaciones.split(",")
                tamaño_lista = len(lista_calificaciones)
                for i in range(tamaño_lista):
                    es_valido = validar_numero(lista_calificaciones[i])
                    if es_valido == False:
                        print(f"El programa a detectado un numero invalido. '{lista_calificaciones[i]}' Saliendo de la lista...")
                        lista_se_rompe = True
                        break
                    else:
                        contador += float(lista_calificaciones[i])
                        resultado_promedio = contador / tamaño_lista

                if lista_se_rompe == False:
                    
                    print("Su promedio es de: ", resultado_promedio)      
                    print("Lista ingresada: ",lista_calificaciones)

                De_nuevo = input("\nDesea calcular nuevamente el promedio? 's' para continuar o cualquiera para SALIR:")
                if De_nuevo == 's':
                    system("clear")
                    continue
                else:
                    break
            menu()

        elif opcion == 3: #OPCION 3: Listas mayores a un valor de entrada.
            while True:
                valor_a_comparar = input("Ingrese numero para comparar sus calificaciones: ")
                es_valido = validar_numero(valor_a_comparar)
                if es_valido:
                    lista1 = lista_usuario()
                    tamaño_lista = len(lista1)
                    for i in range(tamaño_lista):



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

system("clear")
print("Has Salido del programa!")