# Vas a crear un programa para obter informacion de un contacto. El programa debe:

# Obtener información del contacto desde la consola.
# Almacenar la información en un diccionario.
# Realizar algunas operaciones básicas con los datos almacenados.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa input() para obtener el nombre,  el correo electrónico y el número de teléfono del contacto.
# Almacenar Datos:

# Almacena la información en un diccionario.
# Operaciones Básicas:

# Calcula el número total de caracteres en el nombre del contacto.
# Imprime la información completa del contacto.

nombre = input("ingresa tu nombre: ")
email = input("ingresa tu email: ")
telefono = int(input("ingresa tu numero de telefono: "))

#Almacenar informacion del contacto
contacto = {"nombre":nombre, "email":email, "telefono":telefono}

#Obtener número caracteres nombre
total_caracteres = (len(nombre))
print("número de caracteres nombre: ", total_caracteres)

#Imprimir informacion del contacto
print("Información del contacto: ", contacto)