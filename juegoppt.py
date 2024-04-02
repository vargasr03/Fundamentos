import random

def obtener_eleccion_usuario():
    while True:
        eleccion = input("Elige piedra, papel o tijeras: ").lower()
        if eleccion in ['piedra', 'papel', 'tijeras']:
            return eleccion
        else:
            print("Elección no válida. Por favor, elige piedra, papel o tijeras.")

def obtener_eleccion_computadora():
    return random.choice(['piedra', 'papel', 'tijeras'])

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        return "Usuario"
    else:
        return "Computadora"

def jugar_juego_sencillo():
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()
    
    print("Tu elección:", eleccion_usuario)
    print("La elección de la computadora:", eleccion_computadora)
    
    ganador = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print("El ganador es:", ganador)

def jugar_juego_con_contador():
    contador_usuario = 0
    contador_computadora = 0
    
    while contador_usuario < 3 and contador_computadora < 3:
        eleccion_usuario = obtener_eleccion_usuario()
        eleccion_computadora = obtener_eleccion_computadora()
        
        print("Tu elección:", eleccion_usuario)
        print("La elección de la computadora:", eleccion_computadora)
        
        ganador = determinar_ganador(eleccion_usuario, eleccion_computadora)
        print("El ganador es:", ganador)
        
        if ganador == "Usuario":
            contador_usuario += 1
        elif ganador == "Computadora":
            contador_computadora += 1
        
        print("Contador Usuario:", contador_usuario)
        print("Contador Computadora:", contador_computadora)
        
    if contador_usuario == 3:
        print("¡Has ganado después de 3 derrotas!")
    else:
        print("¡La computadora ha ganado después de 3 derrotas!")

def mostrar_menu():
    print("\nMENU")
    print("1. Jugar Juego Sencillo")
    print("2. Jugar Juego con Contador de Derrotas")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            jugar_juego_sencillo()
        elif opcion == '2':
            jugar_juego_con_contador()
        elif opcion == '3':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
