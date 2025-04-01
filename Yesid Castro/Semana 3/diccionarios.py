lista = []

for i in range(2):
    nombre = input("Nombre:")
    precio = input("Precio:")
    stock = input("Stock:")
    dicc = {"nombre": nombre, "precio": precio, "stock": stock}
    lista.append(dicc)

# dicc["nombre"] = input("Digite nombre de producto")
print(lista)

for dicc in lista:
    dicc["precio"] = input("Agregar nuevo precio:")

print(lista)
    