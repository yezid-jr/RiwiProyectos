def validar_numero(numero): #Funcion que retorna T/F para verificar que es un caracter numerico
    try:
        numero = float(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
            return False
    
lista_se_rompe = False


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
    print("lista ingresada correctamente")