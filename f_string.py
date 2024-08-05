#Ejemplos de uso de f-string
nombre = "Roberto"
edad = 38
print(f"Hola, {nombre}, tienes {edad} anios")

#ejemplo de suma f-string
precio1 = 78293
precio2 = 312
print(f"el total de tu compra es: {precio1 + precio2}")

#if dentro de un print
temperatura = 15
print(f"la temperatura esta {"alta" if temperatura > 25 else "baja"}")
