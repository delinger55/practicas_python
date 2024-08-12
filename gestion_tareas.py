"""
[11:23] Roberto Hernandez
Simulador de Gestión de Tareas Personales"
Descripción:
En este proyecto, los alumnos desarrollarán un simulador de gestión de tareas personales. El programa permitirá a los usuarios agregar, 
eliminar, marcar como completadas, y listar tareas pendientes. El proyecto integrará conceptos clave como if, for, while, funciones, 
estructuras de datos (listas y diccionarios), sentencias condicionales, control de flujo, y operadores lógicos.
Objetivos:
Utilizar estructuras de control de flujo (if, for, while).
Definir y organizar el código en funciones.
Manipular listas y diccionarios para almacenar y gestionar datos.
Aplicar operadores lógicos en la toma de decisiones.
Instrucciones:
Crear el Menú Principal:
El programa debe mostrar un menú con las siguientes opciones:
Agregar una tarea.
Marcar una tarea como completada.
Eliminar una tarea.
Listar todas las tareas.
Salir.
Agregar una Tarea:
Solicitar al usuario ingresar la descripción de la tarea y la fecha de vencimiento.
Almacenar la tarea en una lista como un diccionario con las claves: descripcion, fecha, y completada (inicialmente False).
Marcar una Tarea como Completada:
Permitir al usuario seleccionar una tarea de la lista para marcarla como completada (completada = True).
Usar un bucle for para encontrar la tarea en la lista.
Eliminar una Tarea:
Permitir al usuario seleccionar una tarea para eliminarla de la lista.
Verificar si la tarea existe y, de ser así, eliminarla de la lista.
Listar Todas las Tareas:
Recorrer la lista de tareas utilizando un bucle for.
Mostrar la descripción, fecha de vencimiento y estado (completada o pendiente) de cada tarea.
Salir:
Terminar la ejecución del programa cuando el usuario selecciona la opción de salida
 
"""
tareas = []
def agregar_tarea():
    descripcion = input("Ingresa la descripción de la tarea: ")
    fecha = input("Ingresa la fecha de vencimiento(dd/mm/aaaa): ")
    tarea = {"descripcion":descripcion, "fecha":fecha, "completada":False}
    tareas.append(tarea)
    print(f"Tarea de: {descripcion} agregada con éxito")

def marcarCompletada():
    descripcion = input("Ingresa la descripción de la tarea a marcar completada: ")  
    for tarea in tareas:
        if tarea["descripción"].lower() == descripcion.lower():
            if not tarea["Completada"]:  
                tarea["Completada"] = True
                print(f"Tarea marcada completada exitosamente")
            else:
                print(f"La tarea {descripcion} ya estaba completada")               
    print("La tarea no fue encontrada")                  

def eliminar_tarea():
    descripcion = input("Ingresa la descripcion de la tarea a marcar completada")
    for tarea in tareas:
        if tarea["descripcion"].lower() == descripcion.lower():
            tareas.remove(tarea)
            print(f"Tarea eliminada con éxito")
    print("La tarea no fue encontrada")  

def listar_tareas():
    if not tareas:
        print("No hay tareas en la lista")     
    else:
        for tarea in tareas:
            print(f"Descripción: {tarea["descripcion"]}, fecha: {tarea["fecha"]}, Completada: {tarea["completada"]}")   
            
def mostrar_menu():
    print("\n------- Menú de Gestión de Tareas -------")
    print("1.Agregar un tarea: ")  
    print("2.Marcar tarea como completada")
    print("3.Eliminar tarea")
    print("4.Listar tarea")    
    print("5.Salir") 
    
def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            marcarCompletada()  
        elif opcion == 3:
            eliminar_tarea()
        elif opcion == 4:
            listar_tareas()
        elif opcion == 5:
            print("Gracias por usar nuestro sistema") 
            break
        else:
            print("Opción no válida") 
            
#Main
ejecutar_programa()                       
             