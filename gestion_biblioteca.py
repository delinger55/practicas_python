"""
Proyecto Práctico en Python: "Gestión de una Biblioteca Digital"
Descripción:
En este proyecto, los alumnos desarrollarán un programa para gestionar una biblioteca digital. El programa permitirá agregar, 
buscar, y listar libros. Además, contará con funcionalidades para llevar un registro de los libros prestados y devueltos. 
El proyecto integrará varios conceptos clave como if, for, while, funciones, estructuras de datos (listas y diccionarios), 
sentencias condicionales, control de flujo y operadores lógicos.
Objetivos:
Aplicar estructuras de control de flujo (if, for, while).
Definir y utilizar funciones.
Manipular estructuras de datos como listas y diccionarios.
Implementar operadores lógicos para la toma de decisiones.
Instrucciones:
Crear el Menú Principal:
El programa debe mostrar un menú con las siguientes opciones:
Agregar un libro.
Buscar un libro.
Listar todos los libros.
Registrar un préstamo.
Registrar una devolución.
Salir.
Agregar un Libro:
Solicitar al usuario ingresar el título del libro, autor, y el año de publicación.
Almacenar la información en una lista de diccionarios.
Cada libro debe ser representado como un diccionario con las claves: titulo, autor, año, y prestado (inicialmente  False).
Buscar un Libro:
Permitir buscar un libro por título.
Utilizar un bucle for para recorrer la lista de libros y encontrar coincidencias.
Mostrar los detalles del libro si se encuentra, o un mensaje indicando que no existe.
Listar Todos los Libros:
Recorrer la lista de libros utilizando un bucle for.
Mostrar el título, autor, año de publicación y si está prestado o disponible.
Registrar un Préstamo:
Solicitar el título del libro que se desea prestar.
Verificar si el libro está disponible (prestado == False).
Si está disponible, marcarlo como prestado (prestado = True).
Si no está disponible, mostrar un mensaje indicando que ya está prestado.
Registrar una Devolución:
Solicitar el título del libro que se desea devolver.
Verificar si el libro está prestado (prestado == True).
Si está prestado, marcarlo como disponible (prestado = False).
Si no está prestado, mostrar un mensaje indicando que no se encontraba prestado.
Salir:
Terminar la ejecución del programa cuando el usuario selecciona la opción de salida.
Extensiones Sugeridas:
Agregar un sistema de usuarios: Crear una lista de usuarios que puedan prestar libros.
Implementar un límite de préstamos: Establecer un máximo de libros que un usuario puede prestar a la vez.
Historial de préstamos: Registrar y mostrar un historial de los libros prestados y devueltos por cada usuario.
"""

libros = []

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    year = input("Ingrese el año de publicación: ")
    libro = {"titulo":titulo, "autor":autor, "year":year}
    libros.append(libro)
    
#def buscar_libro():

#def listar_libros():
    
    
#def registrar_prestamo():
    
#def registrar_devolucion(): 
      
    
    
def mostrar_menu():
    print("\n------- Gestión de una biblioteca Digital -------")
    print("1.Agregar un libro: ")  
    print("2.Buscar un libro: ")
    print("3.Listar todos los libros")
    print("4.Registrar un prestamo: ")    
    print("5.Registrar una devolución: ") 
    print("6.Salir") 
    
def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            buscar_libro()  
        elif opcion == 3:
            listar_libros()
        elif opcion == 4:
            registrar_prestamo()
        elif opcion == 5:
            registrar_devolucion        
        elif opcion == 6:
            print("Gracias por usar nuestro sistema") 
            break
        else:
            print("Opción no válida")    
      
#Main   