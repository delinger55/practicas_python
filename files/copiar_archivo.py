#Copiar el contenido de un archivo a otro
def copiar_archivo(archivo_origen, archivo_destino):
    try:
        #Abrimos el archivo origen en modo lectura
        with open(archivo_origen, "r") as origen:
            contenido = origen.read() #Leemos el contenido origen
            
        #Abir el archivo destino en modo escritura
        with open(archivo_destino, "w") as destino:
            destino.write(contenido) #Escribir el contenido nuevo archivo
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no existe")
        
#Contar palabra de un archivo
def contar_palabra(archivo):
    try:
        with open(archivo, "r") as f:
            contenido = f.read() #Leemos todo el archivo
            palabras = contenido.split()
            print(f"El archivo {archivo} contiene {len(palabras)} palabras")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe")

#Remplazar palabras en un archivo        
def remplazar_palabra(archivo_origen, palabra_buscar, palabra_remplazo, archivo_destino):
    try:
        with open(archivo_origen, "r") as origen:
            contenido = origen.read()
            
        #remplazar la palabra
        contenido_modificado = contenido.replace(palabra_buscar, palabra_remplazo)
        
        #guarda el contenido modificado en un nuevo archivo
        with open(archivo_destino, "w") as destino:
            destino.write(contenido_modificado)
            print("Palabra cambiada")
        
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no existe")


#Main
copiar_archivo("practicas_python/files/ejemplo.txt", "practicas_python/files/ejemplo2.txt")
contar_palabra("practicas_python/files/ejemplo.txt")
remplazar_palabra("practicas_python/files/ejemplo.txt", "Tlaxcala", "Temuco", "practicas_python/files/ejemplo2.txt")