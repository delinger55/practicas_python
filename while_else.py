passwords = ["ABC12345", "passwordSegu1", "hola", "holamundo"]
for password in passwords:
    if len(password) < 8:
        print(f"el password: {password} es demasiado corto")
        break
else:
    print("Todos los password tiene la longitud requerida") 
  
  
    
   