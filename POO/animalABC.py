from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def comer(self):
        return "Comiendo" 
    
class Dog(Animal):
    def sound(self):
        return "Gau, gau"
    def comer(self):
        return "Comiendo" 
    
class Cat(Animal):
    def sound(self):
        return "Miauu"  
    
class Pig(Animal):
    def comer(self):
        return "Comiendo"    
    
#main
perro = Dog()
gato = Cat() 
#cerdo = Pig()

print(gato.sound())    
print(perro.sound()) 
print(f"El perro está: {perro.comer()}")
#print(cerdo())