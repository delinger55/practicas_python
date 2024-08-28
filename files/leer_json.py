import json

with open("practicas_python/files/json/data.json", "r") as file:
    datos = json.load(file)
    nombre = datos["nombre"]
    edad = datos["edad"]
    correo = datos["correo"]
    hobbies = datos["hobbies"]
    trabajo = datos["trabajo"]
    
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Correo: {correo}")
    print(f"Hobbies: {hobbies}")
    print(f"Trabajo: {trabajo}")
    

#1. Mostrar dato empresa y puesto del empleado   
    print(f"Empresa: {trabajo["empresa"]}, Puesto:{trabajo["puesto"]}")
