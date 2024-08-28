import json

#Leer archivo
def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data
    
#Escribir en el archivo Json
def write_json(filename, jsdata):
    with open(filename, "w") as file:
        data = json.dump(jsdata, file, indent=4)
        
#Agregar producto
def add_product(data, product):
    data["products"].append(product)
    
#Actualizar la cantidad de productos existentes
def update_product(data, product_id, new_quantity):
    for product in data["products"]:
        if product["id"] == product_id:
            product["quantity"] = new_quantity
            break 
        
#Eliminar un producto
def remove_product(data, product_id):
    data["products"] = [product for product in data["products"] if product["id"] != product_id] 
    
#Mostrar productos
def show_products(data):
    print("Lista de productos:")
    for product in data["products"]:
        print(f"ID: {product['id']}, Precio: {product["price"]} .Nombre: {product["name"]}, Cantidad: {product["quantity"]}") 

#Main
filename = "practicas_python/files/json/products.json" 
data = read_json(filename)
show_products(data)

update_product(data, 2, 30)
show_products(data)

remove_product(data, 1)
show_products(data)
write_json(filename, data)

new_product = {"id": 4, "name": "Taza", "price": 5.5, "quantity": 4}
add_product(data, new_product)
write_json(filename, data)
show_products(data)

