class Cuenta:
    def  __init__(self, titular, saldo=0):
        self._titular = titular #atributo protegido _titular
        self._saldo = saldo #atributo protegido _saldo
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        if cantidad < 0:
            print("El cantidad no puede ser negativa o cero")
        else:
            self._saldo = cantidad
            
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se ha depositado ${cantidad} y su nuevo seldo es ${self._saldo}")
        else:
            print("La cantidad a depositar debe ser positiva")
        
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self.saldo -= cantidad   
            print(f"Se ha retirado la ${cantidad}. Su nuevo saldo es: ${self._saldo}") 
        else:
            print("Fondos insuficientes")
                