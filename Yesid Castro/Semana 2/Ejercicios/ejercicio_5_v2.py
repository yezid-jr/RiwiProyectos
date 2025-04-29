"""
5. Validación de contraseña simple
El usuario crea una contraseña que debe cumplir dos requisitos:
        1. Tener al menos 8 caracteres.
        2. Contener al menos el carácter @.
*Si la longitud es insuficiente, informar “Contraseña muy corta”. 
*Si la longitud es correcta pero falta @, informar “La contraseña debe incluir al menos un '@'”. 
*Sólo cuando ambos requisitos se cumplan, mostrar “Contraseña válida”.
"""
###INICIO
while True:
    lista_contraseña = []
    cont = 0
    largo = False
    caracter_especial = False
    contrasena = input("Ingrese contraseña:")
    for letra in contrasena:
        # lista_contraseña.append(contrasena[i])
        if letra == '@':
            caracter_especial = True
        cont += 1

    if cont >= 8:
        largo = True

    if caracter_especial == False and largo == False:
        print("Contraseña no valida, debes de agregar un '@' en la contraseña y es corta")
    elif caracter_especial == True and largo == False:
        print("Contraseña no valida, es demasiado corta")
    elif caracter_especial == False and largo == True:
        print("Contraseña no valida, debes de agregar un '@' en la contraseña")
    else:
        print("\nContraseña ingresada correctamente")
        break

###FIN