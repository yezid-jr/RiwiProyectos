###Crea un programa que pida al usuario que ingrese números enteros hasta que ingrese el número 0. 
# Utiliza un ciclo while para pedir los números, y dentro del ciclo, 
# }utiliza una condicional if para verificar si el número es negativo. 
# Si el número es negativo, se debe imprimir un mensaje y continuar pidiendo nuevos números 
# con continue. Si el número ingresado es cero, el ciclo debe terminar usando break y mostrar 
# la cantidad de números positivos ingresados.
numero_usuario = 1
while numero_usuario != 0:
    numero_usuario = int(input("Digite numero entero:"))
