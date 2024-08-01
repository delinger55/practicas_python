# Título: Sistema de Puntuación Interactivo para un Juego de Niveles

# Descripción:
# Desarrolla un sistema de puntuación interactivo para un juego de niveles utilizando Python.
# El sistema debe cumplir con los siguientes requisitos:

# 1. Utiliza un diccionario para almacenar los jugadores y sus puntuaciones.

# 2. Implementa una lista de niveles (Fácil, Medio, Difícil, Experto)
# y sus correspondientes puntuaciones.

# 3. Recibe información de la consola para simular una ronda de juego:
#    - Pide al usuario que ingrese el nombre del jugador actual.
#    - Solicita el nivel completado por el jugador.
#    - Pregunta por el tiempo que tardó en completar el nivel.

# 4. Valida la entrada del usuario:
#    - Verifica que el jugador exista en el diccionario de jugadores.
#    - Asegúrate de que el nivel ingresado sea válido.
#    - Comprueba que el tiempo ingresado sea un número positivo.

# 5. Actualiza la puntuación del jugador basándote en el nivel completado.

# 6. Incluye un sistema de bonificación: 
# si un jugador completa un nivel Difícil o Experto en 30 segundos o menos, 
# recibe puntos extra.

# 7. Determina el líder actual del juego.
# En caso de empate, muestra todos los jugadores empatados.

# 8. Muestra las puntuaciones actuales de todos los jugadores.

# Restricciones:
# - Utiliza estructuras if-else para la lógica condicional.
# - Emplea operadores lógicos cuando sea necesario.
# - Usa listas y diccionarios para almacenar y manipular datos.
# - Utiliza input() para recibir información del usuario.

# # Lista de niveles con sus respectivos puntos
# niveles = ["Fácil", "Medio", "Difícil", "Experto"]
# puntos_por_nivel = [10, 20, 30, 50]
""" 
print(f"\nHay un empate entre {' y '.join(lideres)} con {puntuacion_maxima} puntos cada uno.")
"""

jugadores = {}

jugadores = {
    "Raúl", 0,
    "María", 0,
    "Pablo", 0
}

#Lista de niveles
niveles = ["Fácil", "Medio", "Dificil", "Experto"]
print(niveles)
niveles_puntos = [10, 20, 30 ,40]

jugador= input("Ingrese el nombre del jugador: ")
if jugador == "Raúl" or "María" or "Pablo":
    print("pasa al siguiente paso")
else:
    print("Ingrese un nombre correcto")    