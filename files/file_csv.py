import csv

with open("practicas_python/files/cvs/alumnos.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
        
#Escribir un archivo csv
datos = [["Nombre", "edad"], ["Edgar", 34], ["Gonzalo", 33]]

    
with open("practicas_python/files/cvs/nuevo_datos.csv", "w", newline="") as archivo_csv:
    escribir = csv.writer(archivo_csv)
    for fila in datos:
        escribir.writerow(fila)