#operador and
a = int(input("Ingresa un valor"))
b= int (input("Ingresa otro valor"))
resultado= (a>5) and (b<30)
print(resultado)

#operador or
x = 5
y= 15
resultado2 = (x>10) or (y<20)
print(resultado2)

#operador not
edad = 17
#verificar si edad NO es mayor o igual a 18
resultado3 = not (edad >=18)
print(resultado3)

#Operación usando diferentes operadores
w= 5
v= 15
t= 25
resultado4 = (v<10) and (w<20) or (t>20)
print(resultado4)

#and con boolean
var1 = True
var2 =False

comparacion = var1 and var2
print(comparacion)

comparacion2 = var1 or var2
print(comparacion2)

comparacion3= not var1
print(comparacion3)