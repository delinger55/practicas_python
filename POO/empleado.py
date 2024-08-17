class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre #publico
        self._departamento = None # protegido
        self.__salario = salario # privado
        
    @property
    def salario(self): #método get (obtener)
        return self.__salario   

    @salario.setter  
    def salario(self, nuevo_salario): #método set (asignar)
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Salario debe ser positivo")
            
    def _asignar_departamento(self, departamento):    
        self.departamento = departamento  
        
    def _calcular_bonus(self):
        return self.__salario * 0.1      
    
#Main
empleado = Empleado("Roberto", 200)
print(empleado.nombre) #Acceso directo a un atributo público  

empleado.salario = 550 #uso de setter   
print(empleado.salario) #uso de getter 
empleado._asignar_departamento("Ventas") #uso método protegido

#print(empleado.__salario)
#empleado._calcular_bonus()
        
                