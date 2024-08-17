from materialBiblioteca import MaterialBiblioteca

class Periodico(MaterialBiblioteca):
    def __init__(self, titulo, autor, annio_publicacion, fecha_periodico):
        super().__init__(titulo, autor, annio_publicacion)
        self.fecha_periodico = fecha_periodico
        
    def informacion(self):
        print(f"Periodico: {self.titulo}, fue creado por: {self.autor}, año publicacion: {self._annio_publicacion}, fecha especifica periodico: {self.fecha_periodico}")