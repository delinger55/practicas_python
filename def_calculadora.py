#Metodos
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def imprimir_resultado(a,b,resultado):
    print(f"El Resulado de la suma de: {a} y {b} es: {resultado}")
    
def imprimir_resultado2(a,b,resultado):
    print(f"El Resulado de la Resta de: {a} y {b} es: {resultado}")
    
    
def solicitar_numeros(num1,num2):
    num1=float(input("ingresa el primer numero: "))
    num2=float(input("ingresa el segundo numero: "))
    return num1,num2

    

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
            imprimir_resultado(num1,num2,resultado)
        elif opcion ==2:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = restar(num1, num2)
            imprimir_resultado2(num1,num2,resultado)   
        elif opcion ==3:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicar(num1, num2)
            imprimir_resultado(num1,num2,resultado) 
        elif opcion ==4:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
            imprimir_resultado(num1,num2,resultado) 
        elif opcion ==5:
            print("Hasta la proxima")
            break 
        else:
            print("Opcion no valida") 
             
calculadora()    
               
            
            
             
#Main


