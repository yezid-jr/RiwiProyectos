"""
4. Descuento en tienda según monto y tipo de cliente
    • Enunciado:
Un cliente ingresa el monto de su compra y si es VIP (“S”/“N”). Aplica el siguiente descuento:
        ◦ VIP:
            ▪ 20 % si monto ≥ 500.
            ▪ 10 % si monto < 500.
        ◦ No VIP:
            ▪ 5 % si monto ≥ 500.
            ▪ 0 % si monto < 500.
"""
###INICIO
#contraseña VIP: 1234
valor_compra = float(input("Ingrese monto de su compra:"))
es_vip = input("Digite su clave de VIP para descuentos especiales, sino precione enter.")

if es_vip == "1234":
    if valor_compra >= 500:
        total_pagar = ((100 - 20)/100) * valor_compra
        print("Su compra es mayor a $499 tiene un descuento del 20%")
        print("Total a pagar:", total_pagar)
    else:
        total_pagar = ((100 - 10)/100) * valor_compra
        print("Su compra es menor a $499 tiene un descuento del 10%")
        print("Total a pagar:", total_pagar)
else:
    print("usted no es VIP:\n")
    if valor_compra >= 500:
        total_pagar = ((100 - 5)/100) * valor_compra
        print("Su compra es mayor a $499 tiene un descuento del 5%")
        print("Total a pagar:", total_pagar)
    else:
        total_pagar = valor_compra
        print("Su compra es menor a $499 usted no tiene descuento")
        print("Total a pagar:", total_pagar)

###FIN