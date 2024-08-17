""""
El polimorfismo es una forma en la que diferentes cosas pueden comportarse de manera similar 
cuando hacemos algo con ellas. Aunque cada cosa es diferente, pueden "responder" de manera 
similar a una misma acción.

Supongamos que estamos en una tienda de juguetes. Queremos que cada juguete haga su sonido. 
No importa si es un tambor, una trompeta o una muñeca, cada uno tiene su forma de responder 
cuando decimos "¡Haz un sonido!".

"""

class Juguete:
    def hacer_sonido(self):
        pass  # Este método será definido en cada tipo de juguete

class Tambor(Juguete):
    def hacer_sonido(self):
        return "¡Boom boom!"

class Trompeta(Juguete):
    def hacer_sonido(self):
        return "¡Tu-tuu!"

class Muñeca(Juguete):
    def hacer_sonido(self):
        return "¡Hola!"

def jugar_con_juguete(juguete):
    print(juguete.hacer_sonido())

# Crear instancias de diferentes juguetes
mi_tambor = Tambor()
mi_trompeta = Trompeta()
mi_muñeca = Muñeca()

# Jugar con cada juguete
jugar_con_juguete(mi_tambor)  # "¡Boom boom!"
jugar_con_juguete(mi_trompeta)  # "¡Tu-tuu!"
jugar_con_juguete(mi_muñeca)  # "¡Hola!"



