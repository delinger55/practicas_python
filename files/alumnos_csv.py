import csv
#Escribe un csv incluyendo cabecera y los datos
def escribir_csv(filename, datos):
    with open(filename, mode="w", newline="") as file:
        escritor_csv = csv.writer(file)#Invocar la función escribir de la librería csv
        escritor_csv.writerow(["Nombre", "Apellido", "Notas"])#Cabecera
        for fila in datos:#Recorremos los datos recibidos
            escritor_csv.writerow(fila)
        print("Archivo csv creado con exito")

#Leer archivo csv       
def leer_csv(filename):
    print("=========== Contenido del archivo csv ===========")
    with open(filename, mode="r", newline="") as file:
        lector_csv = csv.reader(file)
        for fila in lector_csv:
            print(fila)
#Agregar un registro al final del archivo            
def agregar_csv(filename, registro):
    with open(filename, mode="a", newline="") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(registro)
        print("Nuevo registro agregado")
            
        
datos_iniciales = [["Moises", "Barrera", "Santiago"], ["Edgar", "Carrion", "Osorno"], ["Crhistofer", "Sanchez", "Santiago"]]
nombre_archivo = "practicas_python/files/csv/students2.csv"
registro_agregar = ["Armin", "Cano", "Villarrica"]
registro_agregar2 = ["Jose", "Vinuela", "Santiago"]
escribir_csv(nombre_archivo, datos_iniciales)
leer_csv(nombre_archivo)
agregar_csv(nombre_archivo, registro_agregar)
leer_csv(nombre_archivo)
agregar_csv(nombre_archivo, registro_agregar2)

