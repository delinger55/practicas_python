#DuckTyping 
class Pato:
    def volar(self):
        print("El pato vuela")
    def nadar(self):
        print("El pato nada")
        
class Persona:
    def volar(self):
        print("La persona vuela en avión") 
    def nadar(self):
        print("La persona nada en la piscina") 
    
    
class Pez:
    def volar(self):
        print("El pez vuela mientras salta") 
    def nadar(self):
        print("El pez nada en el mar")       
        
def hacer_volar_y_nadar(objecto):
    objecto.volar()
    objecto.nadar()

lucas = Pato()   
Roberto = Persona()
nemo = Pez()

hacer_volar_y_nadar(lucas) 
hacer_volar_y_nadar(Roberto)  
hacer_volar_y_nadar(nemo)  
