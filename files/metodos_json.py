import json

with open("practicas_python/files/json/employees.json", "r") as file:
    data = json.load(file)
    
#Operaciones básicas
#Mostrar lista de empleados
print("====== Lista de empleados =======")
for employees in data["employees"]:
    print(f"Nombre:{employees["name"]}, Edad: {employees["age"]}, Ciudad: {employees["city"]}")

#Obtener la edad promedio de los empleados
total_age = sum(employee["age"] for employee in data["employees"])
average_age = total_age / len(data["employees"])
print(f"La edad promedio de los empleados es: {average_age}")

#Encontrar empleado de una ciudad específica
city = "London"
employees_in_city = [emp["name"] for emp in data["employees"] if emp["city"] == city]
print(f"\n Empleado en la ciudad {city}:{",".join(employees_in_city)}")
print(f"\n Empleado en la ciudad {city}:{(employees_in_city)}")

#Agregar nuevo empleado
new_employee = {"name": "Roberto", "age": 38, "city": "Tlaxcala"}
data["employees"].append(new_employee)
#Guardar los cambios
with open("practicas_python/files/json/employees.json", "w") as file:
    json.dump(data, file, indent=4)
    
print(f"Nuevo empleado agregado: {new_employee["name"]}")