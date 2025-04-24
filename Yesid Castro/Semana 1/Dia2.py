"""Ingresar los 4 tipos de datos (Sgtring, int, float, bool) y validar sin usar el metodo try."""

# Definicion de funciones
def validar_string(mensaje):
    """Validar si el dato es un string."""
    dato = input(mensaje)
    if dato.isalpha():
        return dato
    else:
        print("Error: El dato ingresado no es un string.")
        return validar_string(mensaje)
    
def validar_int(mensaje):
    """Validar si el dato es un entero."""
    dato = input(mensaje)
    if dato.isdigit():
        return int(dato)
    else:
        print("Error: El dato ingresado no es un entero.")
        return validar_int(mensaje)
    
def validar_float(mensaje):
    """Validar si el dato es un float."""
    dato = input(mensaje)
    if dato.replace(".", "").isdigit() and dato.count(".") <= 1:
        return float(dato)
    else:
        print("Error: El dato ingresado no es un float.")
        return validar_float(mensaje)
    
def validar_bool(mensaje):
    """Validar si el dato es un booleano."""
    dato = input(mensaje)
    if dato.lower() in ["true", "false"]:
        return dato.lower() == "true"
    else:
        print("Error: El dato ingresado no es un booleano.")
        return validar_bool(mensaje)

# Programa principal
if __name__ == "__main__":
    print("Ingrese los datos a validar:")
    string = validar_string("Ingrese un string: ")
    entero = validar_int("Ingrese un entero: ")
    decimal = validar_float("Ingrese un float: ")
    booleano = validar_bool("Ingrese un booleano (true/false): ")

    print(f"String: {string}")
    print(f"Entero: {entero}")
    print(f"Float: {decimal}")
    print(f"Booleano: {booleano}")
