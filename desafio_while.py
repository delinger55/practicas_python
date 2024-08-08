# Desafío: Adivina el Número Secreto
# Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100. 
# El programa debe indicar si el número ingresado es mayor o menor al número secreto y continuar preguntando hasta que el usuario lo adivine.

# Instrucciones:
# Generar un número secreto aleatorio entre 1 y 100.
# Pedir al usuario que adivine el número secreto.
# Comparar el número ingresado por el usuario con el número secreto:
# Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
# Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
# Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
# Continuar pidiendo al usuario que adivine hasta que acierte el número secreto.



import random
numero_secreto = random.randint(1, 100)
# print(numero_secreto)  
numero = int(input("Adivine un número entre 1 y 100: "))

while numero != numero_secreto:
    if numero < numero_secreto:
        print(f"El número {numero} es menor al número secreto.")
    elif numero > numero_secreto:
        print(f"El número {numero} es mayor al número secreto.")
    
    # Pedir al usuario que intente de nuevo
    numero = int(input("Inténtalo de nuevo: "))

# Mensaje de éxito fuera del bucle
print("¡Felicidades! Has adivinado el número secreto.")
