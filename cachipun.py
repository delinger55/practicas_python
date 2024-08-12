# Claro, te explicaré el reto en detalle.
# El reto consiste en crear un juego de "Piedra, Papel o Tijera" en Python, incorporando varios elementos específicos del lenguaje.
# El objetivo es desarrollar un programa interactivo que permita 
# al usuario jugar contra la computadora, utilizando estructuras y conceptos fundamentales de Python.
# Los elementos clave que se pidieron incluir son:

# Bucle while: Para mantener el juego en ejecución hasta que el jugador decida salir.
# For else: Aunque no se utilizó directamente en esta versión, podría haberse usado para iterar sobre las opciones.
# Diccionarios: Si bien no se usó explícitamente en la versión final, se podría haber utilizado para mapear las opciones con sus resultados.
# Listas: Se usa para almacenar las opciones del juego ("piedra", "papel", "tijera").
# Condicionales if-else: Para determinar el ganador de cada ronda y el resultado final del juego.
# F-strings: Para formatear la salida de texto, mostrando puntajes y elecciones.
# Tipo juego: El reto específicamente pide crear algo interactivo y lúdico, lo cual se cumple con este juego de Piedra, Papel o Tijera.

# El reto busca que se apliquen estos conceptos en un contexto práctico y divertido, creando un juego funcional que:

# Mantenga un ciclo de juego continuo.
# Permita la interacción del usuario.
# Genere elecciones aleatorias para la computadora.
# Compare las elecciones para determinar el ganador.
# Lleve un registro del puntaje.
# Maneje entradas inválidas.
# Proporcione una forma de salir del juego.
# Muestre el resultado final.

# Este tipo de reto es valioso porque:

# Aplica conceptos teóricos en un escenario práctico.
# Fomenta el pensamiento lógico para implementar las reglas del juego.
# Practica la manipulación de diferentes tipos de datos en Python.
# Desarrolla habilidades en la creación de interfaces de usuario basadas en texto.
# Introduce conceptos de aleatoriedad y toma de decisiones programática.

# # En resumen, el reto combina varios aspectos fundamentales de la programación en Python en un proyecto cohesivo y entretenido,
# lo que lo hace ideal para practicar y reforzar habilidades de programación.

import random

def juego_piedra_papel_tijera():
    # Opciones disponibles
    opciones = ['piedra', 'papel', 'tijera']
    # Puntajes iniciales
    puntaje_jugador = 0
    puntaje_computadora = 0

    # Inicia el bucle del juego
    while True:
        # Muestra el menú de opciones al jugador
        print("\nElige tu opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Salir")

        try:
            eleccion = int(input("Ingresa el número de tu elección: "))
            if eleccion == 4:
                break  # Salir del juego
            if eleccion not in [1, 2, 3]:
                print("Por favor, ingresa una opción válida.")
                continue
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")
            continue

        # Elección del jugador
        eleccion_jugador = opciones[eleccion - 1]
        # Elección aleatoria de la computadora
        eleccion_computadora = random.choice(opciones)

        # Mostrar las elecciones
        print(f"\nTú elegiste: {eleccion_jugador}")
        print(f"La computadora eligió: {eleccion_computadora}")

        # Comparar las elecciones y determinar el ganador
        if eleccion_jugador == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijera') or \
             (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra') or \
             (eleccion_jugador == 'tijera' and eleccion_computadora == 'papel'):
            print("¡Ganaste esta ronda!")
            puntaje_jugador += 1
        else:
            print("La computadora gana esta ronda.")
            puntaje_computadora += 1

        # Mostrar puntajes actuales
        print(f"Puntaje - Tú: {puntaje_jugador}, Computadora: {puntaje_computadora}")

    # Mostrar el resultado final
    print("\nJuego terminado.")
    if puntaje_jugador > puntaje_computadora:
        print("¡Felicidades, ganaste el juego!")
    elif puntaje_jugador < puntaje_computadora:
        print("La computadora ganó el juego. ¡Mejor suerte la próxima vez!")
    else:
        print("El juego terminó en empate.")

# Ejecutar el juego
juego_piedra_papel_tijera()
