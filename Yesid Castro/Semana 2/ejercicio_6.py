###Escribe un programa que recorra una cadena de texto utilizando un ciclo for. 
# Durante la iteración, si el carácter es una vocal (mayúscula o minúscula), 
# debe imprimir "Vocal" y continuar con el siguiente carácter. 
# Si el carácter es un espacio en blanco, el ciclo debe detenerse con la instrucción. 
# Al final, el programa debe mostrar la cantidad total de vocales encontradas en la cadena de texto.
cont_vocal=0
for i in "hola mundo":
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cont_vocal += 1
        print("Vocal")
        continue
    if i == " ":
        break
print("Vocales encontradas: ", cont_vocal)