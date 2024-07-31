# Desafío: Evaluación de Información Personal
# Descripción:

# Vas a crear un programa que obtiene información personal de tres personas desde la consola 
# y realiza algunos cálculos utilizando esta información. El programa debe:

# Obtener los nombres, edades y alturas de tres personas desde la consola.
# Calcular el promedio de las edades y alturas(flotante).
# Calcular el total de caracteres en los nombres.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa la función input() para obtener el nombre, edad y altura de tres personas.
# Calcular Promedios y Totales:

# Calcula el promedio de las edades.
# Calcula el promedio de las alturas.
# Calcula el total de caracteres en los nombres.
# Mostrar Resultados:

# Imprime el promedio de las edades y alturas.
# Imprime el total de caracteres en los nombres.

nombre1 = input("ingresa tu nombre: ")
edad1 = int(input("ingresa tu edad: "))
altura1 = float(input("ingresa tu altura: "))

nombre2 = input("ingresa tu nombre: ")
edad2 = int(input("ingresa tu edad: "))
altura2 = float(input("ingresa tu altura: "))

nombre3 = input("ingresa tu nombre: ")
edad3 = int(input("ingresa tu edad: "))
altura3 = float(input("ingresa tu altura: "))

#Sacar promedios
promedio_edad = (edad1 + edad2 + edad3)/3
promedio_altura =(altura1 + altura2 + altura3)/3
total_caracteres = (len(nombre1) + len(nombre2) + len(nombre3))

#imprimir
print("Promedio de edades: {:.2f}".format(promedio_edad))
print("promedio de alturas: {:.2f} ".format( promedio_altura))
print("Total de caracteresde en los nombres es: ", total_caracteres)