from abc import ABC, abstractmethod
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

#Clase hija que procesa pago para tarjeta de credito    
class PagoTarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando un pago de la cantidad ${cantidad} con tarjeta de credito")
        
    def ValidarNumeroTarjeta(self, num_tarjeta):
        print(f"Validando numero de tarjeta: {num_tarjeta}")
        
#Clase hija que procesa pagos con paypal
class PagoPaypal(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando un pago con paypal de la cantidad ${cantidad}")
        
    def validarConexionApi(self):
        print(f"Validando conexion con Api")
        
class PagoCriptomeneda(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando un pago con Criptomonedas de la cantidad ${cantidad}")
        
def realizar_pago(metodo_pago, cantidad):
    metodo_pago.procesar_pago(cantidad)

#Main
pago1 = PagoTarjetaCredito()
pago2 = PagoPaypal()
pago3 = PagoCriptomeneda()
pago1.ValidarNumeroTarjeta("3765585")

realizar_pago(pago1, 100)
realizar_pago(pago2, 500)
realizar_pago(pago3, 700)
                   