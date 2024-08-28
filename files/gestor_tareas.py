# Reto Completo: Gestor de Tareas con Archivos
# Descripción:
# Crea un programa en Python que gestione una lista de tareas utilizando archivos. El programa permitirá al usuario 
# realizar las siguientes operaciones:
# 1.	Añadir nuevas tareas.
# 2.	Mostrar todas las tareas guardadas.
# 3.	Contar cuántas tareas hay en total.
# 4.	Buscar y reemplazar una palabra en todas las tareas.
# 5.	Copiar las tareas a un nuevo archivo de respaldo.
# Instrucciones:
# 1.	Añadir Tareas:
# -	El programa pedirá al usuario que ingrese una nueva tarea.
# -	Si el usuario escribe "salir", el programa dejará de pedir tareas.
# -	Cada tarea se guardará en un archivo de texto llamado tareas.txt.
# 2.	Mostrar Tareas:
# -	El programa leerá y mostrará todas las tareas guardadas en tareas.txt, una por línea.
# 3.	Contar Tareas:
# -	El programa contará cuántas líneas (tareas) hay en el archivo tareas.txt y mostrará el número total.
# 4.	Buscar y Reemplazar:
# -	El programa pedirá al usuario una palabra a buscar y otra con la que reemplazarla.
# -	Buscará la palabra en todas las tareas y la reemplazará.
# -	Guardará las tareas modificadas en un archivo llamado tareas_modificadas.txt.
# 5.	Copiar Tareas:
# -	El programa copiará el contenido de tareas.txt a un nuevo archivo llamado respaldo_tareas.txt.
# Pistas:
# •	Usa funciones para organizar el código, cada operación puede ser una función diferente.
# •	Maneja las excepciones para asegurarte de que el programa no falle si el archivo no existe o si ocurre algún otro error.
# •	Recuerda cerrar los archivos después de leer o escribir para evitar problemas de acceso a archivos.
# Ejemplo de Flujo del Programa:
# 1.	Menú Inicial:
# 1. Añadir nueva tarea
# 2. Mostrar todas las tareas
# 3. Contar el número de tareas
# 4. Buscar y reemplazar palabra en tareas
# 5. Copiar tareas a un archivo de respaldo
# 6. Salir

class GestorTareas:
    def __init__(self, archivo_tareas= "tareas.txt"):
        self.archivo_tareas = archivo_tareas
        
    def abrir_archivo(self, tarea):
        pass
        
    def anadir_tareas(self, tarea):
        with open(self.archivo_tareas, "a") as archivo:
            archivo.write(tarea + "\n")
        print("Tarea agregada exitosamente")
        
    def mostrar_tareas(self, tarea):
        with open(self.archivo_tareas, "r") as archivo:
            archivo.read(tarea)
            print("Mostrar tarea")
            
    def contar_tareas(self):
        pass
    
    def buscar_reemplazar(self, palabra_buscar, palabra_reemplazar):
        pass
    
    def hacer_respaldo(self):
        pass
#Completar los metodos, agregar excepciones
    
            

def main():
    gestor = GestorTareas()
    while True:
        print("\n------------Menú----------")
        print("1.Añadir tarea")
        print("2.Mostrar tareas")
        print("3.Contar número de Tareas")
        print("4.Buscar y reemplazar")
        print("5.Hacer respaldo")
        print("6.Salir")
        
        opcion = int(input("Elige una opción: "))
        if  (opcion == 1):
            tarea = input("Ingrese una nueva tarea: ")
            gestor.anadir_tareas(tarea)
        elif (opcion == 2):
            gestor.mostrar_tareas(tarea)
        elif (opcion == 6):
            print("Saliendo del programa") 
            break
            
        else:
            print("Opción no válida")   
