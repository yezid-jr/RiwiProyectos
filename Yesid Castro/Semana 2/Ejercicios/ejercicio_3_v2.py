#Enunciado
"""
3. Tarifa de transporte según día y hora

Un usuario indica si el día es laborable (“S”/“N”) y la hora del día (0–23). Calcula la tarifa aplicable:
Día laborable:
    • PICO si la hora está entre 7–9 o 17–19 (inclusive).
    • NORMAL en cualquier otra hora. 
Fin de semana (día no laborable): 
    • FIN DE SEMANA.
"""
###INICIO
semana_laboral = {
    "lunes": "Laboral",
    "martes": "Laboral",
    "miercoles": "Laboral",
    "jueves": "Laboral", 
    "viernes": "Laboral"    
}

dia_usuario = input("Escriba el Dia de la semana:").lower()

for dia, laborable in semana_laboral.items():
    if dia_usuario == dia:
        if laborable == "Laboral":
            hora_usuario = int(input("Escriba hora: formato '24h':"))
            if (hora_usuario >= 7 and hora_usuario <= 9) or (hora_usuario >= 17 and hora_usuario <= 19):
                print("Hora Pico")
            else:
                print("Transporte con normalidad")
        break
    elif dia_usuario == "sabado" or dia_usuario == "domingo":
        print("Fin de Semana, No Laboral")
        break
###FIN