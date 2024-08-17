from libro import Libro
from periodico import Periodico
from revista import Revista

def main():
    libro1 = Libro("Los miserables", "Victor Hugo", 1934, 654)
    print(f"Nombre libro: {libro1.titulo}")
    print(f"Autor: {libro1.autor}")
    print(f"Año publicacion: {libro1.annio_publicacion}")
    print(f"Numero de paginas: {libro1.num_paginas}")
    print("\n")
    
    periodico1 = Periodico("La tercera", "Said", 2023, "12/12/2023")
    print(f"Nombre periodico: {periodico1.titulo}")
    print(f"Fue creado por: {periodico1.autor}")
    print(f"año publicacion: {periodico1.annio_publicacion}")
    print(f"Fecha especifica periodico: {periodico1.fecha_periodico}")
    print("\n")
    
    revista1 = Revista("Barrabases", "Guido Vallejos", 1967, 120)
    print(f"Nombre revista: {revista1.titulo}")
    print(f"Autor: {revista1.autor}")
    print(f"Año publicacion: {revista1.annio_publicacion}")
    print(f"Numero de edicion: {revista1.num_edicion}")
    
  
if __name__ == "__main__":
    main()    