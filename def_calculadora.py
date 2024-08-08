#Metodos
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

"""
def imprimir_resultado(a, b, resultado):
    print(f"El resultado")
"""

    

def calculadora():
    print("-----------Bienbenido a la calculadora 0077--------")
    while True:
        print("\nSeleccione una operación")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")
        opcion = int(input("Ingresa tu opción del 1 al 5: "))
        
        if opcion ==1:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma de {num1} y {num2} es: {resultado}")
        elif opcion ==2:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = restar(num1, num2)
            print(f"El resultado de la resta de {num1} y {num2} es: {resultado}")   
        elif opcion ==3:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación de {num1} y {num2} es: {resultado}")   
        elif opcion ==4:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
            print(f"El resultado de la division de {num1} y {num2} es: {resultado}") 
        elif opcion ==5:
            print("Hasta la proxima")
            break 
        else:
            print("Opcion no valida") 
             
calculadora()    
               
            
            
             
#Main


