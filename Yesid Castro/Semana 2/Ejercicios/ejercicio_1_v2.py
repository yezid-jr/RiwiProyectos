#Enunciado
"""
1. Determinar signo y paridad
Dado un número entero proporcionado por el usuario, determina primero si es positivo, 
negativo o cero. Si el número no es cero, establece además si es par o impar.
"""
###INICIO PROGRAMA
numero_usuario = float(input("Digite un numero:"))

if numero_usuario == 0:
    print("El numero ingresado es 0")
elif numero_usuario < 0:
    print(f"El numero {numero_usuario} es negativo")
else:
    paridad = "impar"
    if numero_usuario % 2 == 0:
        paridad = "par"
    print(f"El numero {numero_usuario} es positivo y además es {paridad}")
###FIN PROGRAMA