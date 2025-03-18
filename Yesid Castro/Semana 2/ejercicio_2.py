###Dada una lista de números enteros, escribe un programa que recorra la lista con un ciclo while.
#  Si un número es par, imprímelo. 

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cont = 0

while cont < len(numeros):
    if numeros[cont] % 2 == 0:
        print(numeros[cont], end=" ")
    cont += 1