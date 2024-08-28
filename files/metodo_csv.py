import csv
#Leer un archivo
with open("practicas_python/files/csv/people.csv", mode="r", newline="") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
        
#Escribir un archivo csv
with open("practicas_python/files/csv/people2.csv", mode="w", newline="") as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerow(["Nombre", "Apellido", "Ciudad"])
    escritor_csv.writerow(["Fernando", "Ruiz", "Osorno"])
    escritor_csv.writerow(["Eduardo", "Valencia", "Antofagasta"])
    escritor_csv.writerow(["Nicole", "Rodriguez", "Temuco"])
    
with open("practicas_python/files/csv/people.csv", mode="a", newline="") as f:
    escritor_csv = csv.writer(f)
    escritor_csv.writerow(["Cristian", "Castillo", "Concepcion"])
     