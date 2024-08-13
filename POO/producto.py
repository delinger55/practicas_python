class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        return f"El producto es: {self.nombre} \nPrecio: {self.precio}, \nCantidad: {self.cantidad}"
    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Se han agregado: {cantidad} unidades de {self.nombre}, la cantidad actual es: {self.cantidad}")
    
    def vender(self, cantidad):
        if cantidad > self.cantidad:
            print(f"No tengo suficiente stock de {self.nombre}, solo hay {self.cantidad}")
        else:
            self.cantidad -= cantidad
            print(f"Se ha vendido {cantidad} del producto {self.nombre} y quedan en stock {self.cantidad}")

#Main
nombre_producto1=input("Ingresa el nombre del producto 1: ")
precio_producto1= int(input("Ingresa el precio del producto 1 : "))
cantidad_producto1 = int(input("Ingresa la cantidad del producto 1: "))

producto1 = Producto(nombre_producto1, precio_producto1, cantidad_producto1)
producto2 = Producto("Mesa", 200, 30)

#Mostrar los datos productos
print(producto1.mostrar())
print(producto2.mostrar())

#Agregamos 10 y mostramos el producto de la laptop
cantidadAgregar= int(input("Cantidad de productos que deseas agregar: "))
producto1.agregar_stock(cantidadAgregar)
print(producto1.mostrar())

#Vender 15 unidades y mostrar el producto2
producto2.vender(15)
print(producto2.mostrar())

#Vender 40 unidades y mostrar el producto1
producto1.vender(40)
print(producto1.mostrar())