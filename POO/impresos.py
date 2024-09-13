#Clase libro
class Book:
    #pass para declarar q una clase no haga nada
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
#Clase periodico
class Newspaper:
    def __init__(self, title):
        self.title = title
        
#Clase revista
class Revista:
    def __init__(self, title):
        self.title = title   
        
        
class Folleto:
    def __init__(self, year):
        self.year = year
                     
        
#Main
book1 = Book("Cien años de soledad", "Gabriel García Marquez")
book2 = Book("Código limpio", "Robert C. Martin")
periodico = Newspaper("El Universal")
periodico2 = Newspaper("La Tercera")
revista = Revista("Condorito")
revista2 = Revista("Conozca más")
folleto = Folleto(1999)
folleto2 = Folleto(2001)

#Invocando objetos de la clase book
print(book1)
print(book2.title)
print(book1.author)
print(book2.author)

#Invocando objetos de la clase Newspaper
print(periodico.title)
print(periodico2.title)

#Invocando objetos de la clase revista
print(f"Título revista: {revista.title}")
print(f"Título revista2: {revista2.title}")

#Invocando objetos de la clase folleto
print(f"Año publicación folleto: {folleto.year}")
print(f"Año publicación folleto2: {folleto2.year}")
