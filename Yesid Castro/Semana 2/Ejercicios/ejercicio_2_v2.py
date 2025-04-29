#Enunciado
"""
2. Una persona ingresa su edad. Clasifica esa edad en una de las siguientes categorías:
    • Menor de edad (<18).
    • Adulto joven (18, 30).
    • Adulto maduro (31, 65).
    • Adulto mayor (>65).
"""
###INICIO PROGRAMA
edad_usuario = int(input("Digite su edad:"))

if edad_usuario < 18:
    print("Menor de edad")
elif edad_usuario >= 18 and edad_usuario <= 30:
    print("Adulto Joven")
elif edad_usuario >= 31 and edad_usuario <= 65:
    print("Adulto Maduro")
elif edad_usuario > 65:
    print("Adulto Mayor")
###FIN PROGRAMA