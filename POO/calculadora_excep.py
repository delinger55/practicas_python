def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error entrada no valida")
            
def realizar_operaciones(a, b, operador):
    try:
        if operador == "+":
            return a + b  
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("Error: no se puede dividir por cero") 
            return a / b
        else:
            raise ValueError("Operación no válida")
  
    except ValueError as e:
        print(f"Error: {e}") 
        return None
            
#Main
num1 = solicitar_numero("Introduce el primer número: ")   
num2 = solicitar_numero("Introduce el segundo número: ") 

operacion = input("Introduce el operador a usar (+, -, *, /):")   
resultado = realizar_operaciones(num1, num2, operacion)
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")