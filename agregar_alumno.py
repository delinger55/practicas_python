# Crea un programa en Python que gestione la información de los estudiantes de una escuela.
# El programa debe permitir
    # agregar nuevos estudiantes,
    # mostrar la lista de estudiantes
    #buscar un estudiante por su nombre.
    
# Requisitos
# Funciones:
# agregar_estudiante(nombre, edad, grado): Agrega un nuevo estudiante a la lista.
# mostrar_estudiantes(): Muestra la lista completa de estudiantes.
# buscar_estudiante(nombre): Busca un estudiante por su nombre y muestra su información.
 
# Interacción con el Usuario:
# El programa debe mostrar un menú con las opciones:
    # "Agregar estudiante",
    # "Mostrar estudiantes",
    # "Buscar estudiante" y
    # "Salir".
    
# La opción "Agregar estudiante"
    #   debe pedir el nombre,
    #   edad
    #   grado del estudiante.
 
# La opción "Mostrar estudiantes"
#   debe mostrar la lista completa de estudiantes.
# La opción "Buscar estudiante"
#   debe pedir el nombre del estudiante y mostrar su información si se encuentra en la lista.

#métodos
#La lista se declara fuera del metodo para que sea global
estudiantes = []

def agregar_estudiante(nombre, edad, grado):
    estudiante = {"nombre":nombre, "edad":edad, "grado":grado}
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    if not estudiantes:#si no hay estudiantes
        print("No hay estudiantes inscritos")
    else:
        for estudiante in estudiantes:
            print(f"El nombre del estudiante es: {estudiante["nombre"]}, su edad es: {estudiante["edad"]} y su grado es: {estudiante["grado"]}")  

def buscar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"Estudiante encontrado, sus datos son:\nnombre: {estudiante["nombre"]}, edad: {estudiante["edad"]}, el grado: {estudiante["grado"]}")
            break
        else:
            print("Estudiante no encontrado")    
 
def mostrar_menu():
    print("*****Bienvenido a gestión de estudientes 0077****") 
    print("Seleccione una opción")
    print("1.Agregar estudiante")
    print("2.Mostrar estudiante")
    print("3.Buscar estudiante")
    print("4.Salir")

def pedir_info__alumno():
    nombre = input("Dame el nombre del alumno: ")
    edad = input("Dame la edad del alumno: ")
    grado = input("Dame el grado del alumno: ")
    return nombre, edad, grado

def validar_opcion(opcion):
    return opcion
    
  
def admon_estudiantes():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            nombre, edad, grado = pedir_info__alumno()
            agregar_estudiante(nombre, edad, grado)
        elif opcion == 2:
            mostrar_estudiantes()
        elif opcion == 3:
            nombre = input("Ingresa el nombre del alumno a buscar: ")
            buscar_estudiante(nombre)  
        elif opcion == 4:
            print("Gracias por usar sistema 0077") 
            break
        else:
            print("Opción no válida")         
           
                      
#Main  
admon_estudiantes()           
        


