# #Objetivo: Crear un programa que permita al usuario adivinar un número secreto. 
# El programa debe dar una sola oportunidad al usuario para adivinar 
# y debe indicar si el usuario adivinó correctamente o no.

# Instrucciones:

# Genera un número secreto.
# Pide al usuario que adivine el número.
# Usa estructuras if y else para comparar 
# la adivinanza del usuario con el número secreto.
# Indica al usuario si su adivinanza es correcta o no.

import random 

numero_secreto = random.randint(1, 10)
print(numero_secreto)

x= int(input("Adivine un número, introduzca un número del 1 al 10: "))
if x == numero_secreto:
    print("Usted adivinó el número")    
else:
    print("Usted no adivinó el número")    