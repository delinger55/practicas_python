class Dog:
    def __init__(self, name, raza, age):
        self.name = name
        self.raza = raza
        self.age = age
        
    def ladrar(self):
        print(f"El perro {self.name}, de {self.age} años ladra así Gau Gau y es de raza {self.raza}")
        
    def salir_a_pasear(self):
        print(f"El perro {self.name}, raza {self.raza}, de {self.age} años sale a pasear al campo")
        
    def comer(self):
        print(f"El perro {self.name}, de raza {self.raza}, de {self.age} años come tres veces al día")    
    
#Principal o main
perro = Dog("Jefazo", "labrador", 3)
perro.ladrar()
perro.salir_a_pasear()
perro.comer()
    