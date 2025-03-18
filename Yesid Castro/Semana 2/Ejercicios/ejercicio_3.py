###Crea un programa que reciba una lista de números enteros y utilice un 
# ciclo while para recorrerlos. Si se encuentra un número negativo, se debe imprimir 
# un mensaje y detener el ciclo utilizando la instrucción break. Si el número es mayor que 100, 
# se debe continuar con el siguiente número utilizando continue. Al final, 
# debe imprimir la cantidad de números procesados que son mayores que 50.

numeros_lista = int(input("Ingrese cantidad de numeros:"))
i = 0; j = 0; cont_mayores_50 = 0
lista_numeros = []
while i < numeros_lista:
    numero = int(input("Agrega numero en la lista:"))
    lista_numeros.append(numero)
    i += 1

print("Su lista es :",lista_numeros)
procesar_lista = input("Desea precesar numeros?:")
if procesar_lista == 'S' or procesar_lista == 's':
    while j < len(lista_numeros):

        if lista_numeros[j] < 0:
            print("Numero negativo! Saliendo...")
            break
        if lista_numeros[j] > 100:
            print("Numero mayor a 100, continue...")
            j += 1
            continue
        if lista_numeros[j] > 50:
            cont_mayores_50 += 1

        j += 1
    print("Programa procesado con exito")
mensaje = "Programa terminado"
print(f"{mensaje}" if cont_mayores_50 == 0 else f"{mensaje}, Mayores de 50:{cont_mayores_50}")