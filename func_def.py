#Métodos
def sin_retorno():
    print("Esta función no tiene retorno")

#a,b son parametros    
def retorno_unico(a, b): #retorno unico a,b parametros
    return a + b

def retorno_multiple(a, b, c):# a,b,c parametros
    return a, b, c

#Main
#Invocar sin retorno
sin_retorno() 

#Invocar retorno único
y = 5
x = 20
retorno2 = retorno_unico(x,y) #a, b argumentos
print(f"El retorno unico: {retorno2}") 
retorno3 = retorno_unico(90, 100)
print(f"El retorno unico: {retorno3}") 

#Invocar retorno multiple
x, y, z = retorno_multiple(7, 8, 9)#aquí a,b,c son argumentos
print(f"El retorno multiple es: {x}, {y}, {z}")
