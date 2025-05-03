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

#Inicio: Programa de gestion de Calificaciones:
###importaciones
from os import system

###Declaracion e inicializador de variables globales
contador = 0
lista_se_rompe = True

### Declaracion de Funciones:
def validar_numero(numero): #Funcion que retorna T/F para verificar que es un caracter numerico
    try:
        numero = float(numero)
        if numero >= 0 and numero <=100:
            return True
        else:
            return False
    except ValueError:
            return False

def menu():  #Funcion que muestra el menu
    print("\nOPCIONES CALIFICACIONES")
    print("\nSeleccione una opción:\n")

    print("1. Verifica si aprobaste.")
    print("2. Calcula tu promedio.")
    print("3. Contador de calificaciones mayores.")
    print("4. Ingresar nuevamente las calificaciones.")
    print("\nEnter any key for exit.")

def procesamiento_lista(lista, opcion): #Funcion para calcular el promedio de la lista
    suma_calificaciones = 0
    aprobaste = False
    tamaño_lis = len(lista)

    for i in range(tamaño_lis):
        numero = float(lista[i])
        suma_calificaciones += numero

    promedio = suma_calificaciones / tamaño_lis

    if promedio >= 60:
        aprobaste = True

    if opcion == 1:
        if aprobaste:
            return True
        else:
            return False
    if opcion == 2:
        return promedio

def print_lista (lista):
    print("Tu Lista De Calificaciones:",lista)

def limpiar_terminal(): #Limpia la terminal
    system("clear")
    system("cls")

def lista_califica(sw):
    while sw == True:
        sw = False
        print("Bienvenido al programa de gestion de calificaciones")
        print("\nIngrese calificaciones separadas por ','(Coma) EJEMPLO: 80, 90, 100")
        print("Recuerde que las calificaciones deben estar entre 0 y 100")
        numero_calificaciones = input("\nIngrese sus calificaciones:")
        lista_calificaciones_filtro = numero_calificaciones.split(",")
        tamaño_lista = len(lista_calificaciones_filtro)

        for i in range(tamaño_lista): #Recorre la lista

            es_valido = validar_numero(lista_calificaciones_filtro[i])
            if es_valido == False:
                limpiar_terminal()
                print(f"El programa a detectado un valor NO valido. '{lista_calificaciones_filtro[i]}' Saliendo de la lista...\n")
                sw = True
                print("Intente Nuevamente")
                break
    return lista_calificaciones_filtro, sw, tamaño_lista

### Primer ingreso de la lista de calificaciones

limpiar_terminal()

lista_calificaciones, lista_se_rompe, tamaño_lista = lista_califica(lista_se_rompe) #Llama a la funcion para ingresar la lista de calificaciones   


### opciones del aplicativo interaccional

if lista_se_rompe == False:
    limpiar_terminal()
    print(f"lista ingresada Correctamente.\nCalificaciones ingresadas: {lista_calificaciones}")
    while True: 
        try:
            menu()
            opcion = int(input())

            if opcion == 1: #OPCION 1: Verifica si está aprobado
                
                limpiar_terminal()
                aprobado = procesamiento_lista(lista_calificaciones, opcion) #pasa la lista y la opcion = 1 y manda el return definido en la funcion
                print("\nAprobaste!\n" if aprobado else "\nNo Aprobaste :(\n")

                ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
                if ir_inicio.lower() == "s":
                    continue
                raise ValueError

            elif opcion == 2: #OPCION 2: Calcula el promedio de una secuencia de numeros dadas por ',' coma

                limpiar_terminal()
                promedio = procesamiento_lista(lista_calificaciones, opcion) #pasa la lista y la opcion = 2 y manda el return definido en la funcion
                print("Tu promedio es: ",promedio)

                ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
                if ir_inicio.lower() == "s":
                    continue
                raise ValueError

            elif opcion == 3: #OPCION 3: Listas mayores a un valor de entrada.
                
                limpiar_terminal()
                numero_usuario = float(input("Digite un numero a comprar con sus calificaciones: "))
                lista_califi_altas = [] #Nueva lista para ingresar las notas correspondientes

                for i in range(tamaño_lista): #Recorre la lista
                    numero = float(lista_calificaciones[i])
                    if numero >= numero_usuario:
                        contador += 1 #Cuenta de 1 en 1 aquellas mayores o igual al numero ingresado
                        lista_califi_altas.append(numero)
                print(f"Tienes {contador} calificaciones mayoeres a {numero_usuario}\nAcá tienes las calificaciones:{lista_califi_altas}")

                ir_inicio = input("Enter 's' para Ir al Menú") #'s' para salir de la opcion
                if ir_inicio.lower() == "s":
                    continue
                raise ValueError
            
            elif opcion == 4: #OPCION 4: Ingresar nuevamente calificaciones
                lista_se_rompe = True
                limpiar_terminal()
                print("Ingrese nuevamente las calificaciones")
                lista_calificaciones, lista_se_rompe, tamaño_lista = lista_califica(lista_se_rompe)
        except:
            break
limpiar_terminal()
print("Has Salido del programa!")

