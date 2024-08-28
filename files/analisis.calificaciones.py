"""
Reto: Análisis de Calificaciones Estudiantiles
Descripción:
Crea un programa en Python que gestione y analice las calificaciones de los estudiantes utilizando un 
archivo CSV. El programa permitirá al usuario realizar las siguientes operaciones:
1.	Añadir un nuevo registro de calificación.
2.	Mostrar todos los registros de calificaciones.
3.	Calcular y mostrar el promedio general de calificaciones.
4.	Identificar y mostrar las calificaciones más altas y más bajas.
5.	Buscar y mostrar las calificaciones de un estudiante específico.
6.	Contar el número de estudiantes aprobados y reprobados.
Estructura del CSV:
El archivo CSV se llamará calificaciones.csv y tendrá el siguiente formato:
Copiar código
Nombre,Materia,Calificación
•	Nombre: Nombre del estudiante.
•	Materia: Nombre de la materia.
•	Calificación: Calificación obtenida por el estudiante.

Instrucciones:
1.	Añadir Registro de Calificación:
o	El programa pedirá al usuario el nombre del estudiante, la materia y la calificación.
o	Añadirá el registro al archivo calificaciones.csv.
2.	Mostrar Registros de Calificaciones:
o	El programa leerá y mostrará todos los registros de calificaciones guardados en calificaciones.csv.
3.	Calcular Promedio General:
o	El programa calculará y mostrará el promedio general de las calificaciones registradas.
4.	Identificar Calificaciones Más Altas y Más Bajas:
o	El programa buscará y mostrará la calificación más alta y la más baja.
5.	Buscar Calificaciones por Estudiante:
o	El programa pedirá al usuario un nombre de estudiante y buscará todas las calificaciones relacionadas 
con ese estudiante.
6.	Contar Estudiantes Aprobados y Reprobados:
o	El programa contará y mostrará cuántos estudiantes han aprobado y cuántos han reprobado. Se considerará 
que una calificación es aprobatoria si es mayor o igual a 60 (o el criterio que se defina).
"""
import csv
class AnalisisCalificaciones:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.datos = []

    def agregar_nuevo_registro_clificacion(self):
        pass
    
    def mostrar_registro(self):
        "Lee los datos de los archivos"
        with open(self.archivo_entrada, mode="r") as file:
            reader = csv.DictReader(file)
            self.datos = [fila for fila in reader]

    def calcular_promedio_general(self):
        total_promedio = sum(float(estudiante['Calificacion']) for estudiante in self.datos)
        cantidad_estudiante = len(self.datos)
        return total_promedio / cantidad_estudiante if cantidad_estudiante > 0 else 0
    
    def calificacion_baja_alta(self):
        pass
    
    def mostrar_calificaciones_estudiante(self):
        pass
    
    def numReprobado_numAprobado(self):
        pass