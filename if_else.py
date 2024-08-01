x= int(input("ingrese un numero: "))
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5") 
    
    
y = int(input("Ingrese otro numero Y: "))   
if y < 10: 
    print("Y es menor que 10")  
elif y == 10:
    print("Y es igual a 10")
elif y < 20:
    print("Y es mayor que 10, pero menor que 20")
else:
    print("Y 20 o mayor")
    
#Ejemplo con edad
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Debes tener al menos 18 años para registrarte")
elif 18 <= edad <= 120:
    print("Registro exitoso")    
else:
    print("Edad no válida, por favor ingresa una edad correcta")