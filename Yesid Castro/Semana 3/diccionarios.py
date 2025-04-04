# lista = []

# for i in range(2):
#     nombre = input("Nombre:")
#     precio = input("Precio:")
#     stock = input("Stock:")
#     dicc = {"nombre": nombre, "precio": precio, "stock": stock}
#     lista.append(dicc)

# # dicc["nombre"] = input("Digite nombre de producto")
# print(lista)

# for dicc in lista:
#     dicc["precio"] = input("Agregar nuevo precio:")

# print(lista)
def numero_valido(numero): #Validacion de numero
    try:
        numero = float(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
        return False

def numero_correcto(msg): #Validacion de entrada, parameptros: mensaje para pedir el numero
     while True: 
        numero = input(msg) #Entrada de datos: El usuario digita el ID para poder realizar la busqueda
        if numero_valido(numero):
            return float(numero)
        else:
            print("Por favor, ingrese un numero valido.")

numero = numero_correcto("Digite un numero valido:")
print(numero)