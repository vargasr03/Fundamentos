import random

def adivina_el_numero_usuario():
    print("\nBienvenido al Juego de Adivina el Número (Usuario)")
    print("La computadora pensará un número y tendrás que adivinarlo.")
    print("¡Buena suerte!")

    numero_aleatorio = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("\nIntenta adivinar el número (entre 1 y 100): "))
        intentos += 1

        if intento < numero_aleatorio:
            print("El número es demasiado bajo. ¡Inténtalo de nuevo!")
        elif intento > numero_aleatorio:
            print("El número es demasiado alto. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break

def adivina_el_numero_computadora():
    print("\nBienvenido al Juego de Adivina el Número (Computadora)")
    print("Piensa en un número entre 1 y 100, y la computadora intentará adivinarlo.")
    print("Presiona 's' si la suposición es correcta, 'm' si es demasiado alta, 'b' si es demasiado baja.")
    print("¡Comencemos!")

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intento = random.randint(limite_inferior, limite_superior)
        print("¿Es", intento, "?")
        respuesta = input("Respuesta (s/m/b): ").lower()

        if respuesta == 's':
            print(f"¡La computadora ha adivinado tu número en {intentos} intentos!")
            break
        elif respuesta == 'm':
            limite_superior = intento - 1
        elif respuesta == 'b':
            limite_inferior = intento + 1
        else:
            print("Respuesta no válida. Por favor, ingresa 's', 'm' o 'b'.")

def mostrar_menu():
    print("\nMENU")
    print("1. Adivina el Número (Usuario)")
    print("2. Adivina el Número (Computadora)")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            adivina_el_numero_usuario()
        elif opcion == '2':
            adivina_el_numero_computadora()
        elif opcion == '3':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
