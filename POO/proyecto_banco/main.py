from cuenta_ahorro import CuentaAhorro

def main():
    cuenta1 = CuentaAhorro("Roberto Hernandez", 1000)
    print(f"El nombre del titular es: {cuenta1.titular}")
    print(f"El saldo es: ${cuenta1.saldo}")
    print(f"La tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.tasa_interes = 0.5
    cuenta1.depositar(50)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"El saldo es: ${cuenta1.saldo}")
    
    cuenta2 = CuentaAhorro("Cirstina", 20, 0.04)
    print(f"El nombre del titular es: {cuenta2.titular}")
    print(f"El saldo es: ${cuenta2.saldo}")
    print(f"La tasa de interes es: ${cuenta2.tasa_interes * 100}%")
    
    
if __name__ == "__main__":
    main()