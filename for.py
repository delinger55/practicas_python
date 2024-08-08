# Recorriendo una lista
frutas = ["Platano", "Manzana", "Sandia", "Pera"]
print(frutas)

for fr in frutas:
    print(f"El nombre de la fruta es: {fr}")
# Recorriendo una palabra
palabra = "Python"
for letra in palabra:
    print(
        f" Esta es una letra de la palabra {letra.upper()}"
    )  # upper para trasformar las letras en mayusculas

# Recorriendo un diccionario
estudiantes = {"Matias": 10, "Roberto": 7, "Axel": 9}
for nombre in estudiantes:
    print(nombre)

# metodo items recibe un diccionario y lo pasa a cadena
for nombre, nota in estudiantes.items():
    print(f"{nombre} tiene una calificacion de {nota}")

numeros = [23, 76, 34, 89, 90, 100]
suma = 0
for numero in numeros:
    suma += numero  # suma= numero + suma
print(f"La suma de los numeros es: {suma}")

media = suma / len(numeros)
print(f"La media es: {media}")
print(f"Numero de elementos en numeros: {len(numeros)}")

# Suma valores de un diccionario
ventas = {"enero": 1000, "febrero": 1500, "marzo": 1200}
total_ventas = 0
for mes, cantidad in ventas.items():
    total_ventas += cantidad  # total_ventas = cantidad + total
print(f"El total de ventas es: {total_ventas}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pares = []
for number in numbers:
    if number % 2 == 0:  # para buscar los numeros pares
        pares.append(number)
print(f"Numeros pares {pares}")

# usando break
nums = [10, 20, 30, -5, 50, 20]
for num in nums:
    if num <= 0:
        print(f"El numero {num} no es positivo")
        break
else:
    print("todos los numeros son positivos")
