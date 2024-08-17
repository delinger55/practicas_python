from materialBiblioteca import MaterialBiblioteca

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, annio_publicacion, num_edicion):
        super().__init__(titulo, autor, annio_publicacion)
        self.num_edicion = num_edicion
        
    def informacion(self):
        print(f"Revista: {self.titulo}, autor: {self.autor}, año publicacion: {self._annio_publicacion}, numero de edicion: {self.num_edicion}")