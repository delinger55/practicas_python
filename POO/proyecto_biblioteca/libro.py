from materialBiblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, annio_publicacion, num_paginas):
        super().__init__(titulo, autor, annio_publicacion)
        self.num_paginas = num_paginas
        
    def informacion(self):
        print(f"Libro: {self.titulo}, autor: {self.autor}, año publicacion: {self._annio_publicacion}, número de paginas: {self.num_paginas}")