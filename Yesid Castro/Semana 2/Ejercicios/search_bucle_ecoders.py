coders = {
    123 : "Yesid Castro",
    456 : "Dalexa Dayana",
    789 : "Tony Pacheco"
}
tuplaitems = print(coders.items())
flag = False
for llave, value in coders.items():
    if value == "Dalexa Dayana":
        flag = True
        print(f"El coder de nombre {value} con id: {llave}")
else:
    print("Se ha finalizado la busqueda")
    if flag:
        print("Se encontro el coder")
    else:
        print("No se encontro el coder")