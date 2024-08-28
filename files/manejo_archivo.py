#Sobreescribiendo archivo txt
with open("practicas_python/files/ejemplo.txt", "w") as archivo:
    archivo.write("Hola desde Tlaxcala Mexico\n")
    archivo.write("Esta es un linea nueva\n")
    archivo.write("Aqui estuvo Ivan\n")
    archivo.write("Ya son casi las vacaciones\n")
    
#Leer archivo
with open("practicas_python/files/ejemplo.txt", "r") as lectura:
    contenido = lectura.read()
    print(contenido)

 #Añadir un contenido al final del archivo   
with open("practicas_python/files/ejemplo.txt", "a") as f:
    f.write("Esta linea la estamos agregando al final") 
 
#Leer archivo   
with open("practicas_python/files/ejemplo.txt", "r") as lectura:
    contenido = lectura.read()
    print(contenido)  
    
#Manejo de errores
with open("practicas_python/files/ejemplo2.txt", "r") as file:
    try:
        contenido = file.read()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra el archivo")
        
with open("practicas_python/files/ejemplo.txt", "r") as archivo:
    contador = 0
    for linea in archivo:
        contador += 1
        #print(f"El archivo tiene: {linea.strip()} lineas")  
    print(f"El total de lineas es: {contador}")      
    