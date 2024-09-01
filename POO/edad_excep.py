class EdadValidaError(Exception):
    pass
def verificarEdad(edad):
    if edad < 18:
        raise ValueError("Debes ser mayor de 18 años para registrarse")
    return "Registro exitoso"

try:
    mensaje = verificarEdad(15)
    print(mensaje)
except ValueError as e:
    print(f"Error: {e}")