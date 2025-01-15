import random

def elegir_palabra():
    # Lista de palabras para el juego
    palabras = ["python", "desarrollador", "programacion", "ahorcado", "computadora"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def juego():
    print("Bienvenido al juego del Ahorcado!")
    
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6  # Número de intentos antes de perder
    letras_erradas = []

    while intentos > 0:
        print("\nPalabra actual: " + mostrar_tablero(palabra, letras_adivinadas))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras erradas: {' '.join(letras_erradas)}")

        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas or letra in letras_erradas:
            print("Ya has adivinado esa letra antes.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Buena elección!")
        else:
            letras_erradas.append(letra)
            intentos -= 1
            print(f"La letra {letra} no está en la palabra.")

        # Verificar si se ha ganado
        if all(letra in letras_adivinadas for letra in palabra):
            print("\n¡Felicidades, has ganado!")
            print(f"La palabra era: {palabra}")
            break

    if intentos == 0:
        print("\n¡Has perdido! Se te han agotado los intentos.")
        print(f"La palabra era: {palabra}")

# Ejecutar el juego
if __name__ == "__main__":
    juego()
