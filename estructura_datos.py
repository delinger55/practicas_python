#Lista(list)
frutas = ["Tunas", "Guanabana", "Maracuya"]
numeroPrimos = [3, 5, 7, 11]
print(type(frutas))
print(type(numeroPrimos))
print(frutas[0])
print(numeroPrimos[2])

#cambiar la primera fruta
frutas[0] ="Mango"
print(frutas)

#Agragar una fruta
frutas.append("Lichi")
print(frutas)

numeroPrimos.append(13)
print(numeroPrimos)

#tuplas
dimensiones = (1920, 1080)
coordenadas = (10,20)
print(type(dimensiones))
print(type(coordenadas))

puntos = (10, 20)
#puntos[1] = 30 #no se puede asignar a tupla un nuevo valor

#conjuntos
colores = {"rojo", "verde", "blanco"}
numero_unicos = {1, 2, 3, 4, 5}
print(type(colores))

numero_unicos.add(6)#metodo para agregar a conjunto
print(numero_unicos)
colores.remove("blanco")#metodo para remover
print(colores)

print(len(numero_unicos))
print(len(colores))

#diccionario (dict)
personas = {"nombre":"Ana", "edad":30, "ciudad":"Angol"}
precios = {"manzana":12, "platano":5, "cerezas":2.5}
print(type(personas))
print(type(precios))
print(personas["nombre"])
print(precios["manzana"])

personas["edad"] = 31 #modificar un valor
print(personas)
personas["ocupacion"] = "Programador"
print(personas)