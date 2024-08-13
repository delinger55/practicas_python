#Clase Coche
class Coche:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
    def describir(self):
        return f"Coche: {self.marca}, \nModelo: {self.modelo}, \nYear: {self.year}"
    def arrancar(self):
        return f"El {self.marca}, {self.modelo} esta arrancando"
    

#Clase Moto    
class Moto:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
    def mostrar_detalles(self):
         return f"La Moto es: {self.marca}, \nModelo: {self.modelo}, \nYear: {self.year}"
    def encender(self):
         return f"La {self.marca}, {self.modelo} esta arrancando"

#Main
#Invocar las clase Coche
mi_coche = Coche("Toyota", "Yaris", "2017")
print(mi_coche.describir())
print(mi_coche.arrancar())

#Invocar la clase Moto
mi_moto = Moto("Honda", "Sivic", "2023")
mi_moto2 = Moto("Ducatti", "Multiestraba", "2024")
print(mi_moto.mostrar_detalles())
print(mi_moto2.encender())



    
    
