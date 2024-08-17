class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def descripcion(self):
        return f"El nombre es: {self.nombre} y tiene la edad: {self.edad}"
    
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
        
    def descripcion(self):
        return f"{super().descripcion()} y gana {self.salario} dolares al mes"

#Main
empleado = Empleado("Roberto", 38, 500)
print(empleado.descripcion())    
     