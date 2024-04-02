import random
import string

def generar_contrasena(longitud, incluir_mayusculas, usar_caracteres_especiales):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def solicitar_confirmacion():
    while True:
        respuesta = input("¿La contraseña generada es adecuada? (s/n): ").lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

def main():
    print("¡Bienvenido al Generador de Contraseñas!")
    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
    incluir_mayusculas = input("¿Desea incluir mayúsculas en la contraseña? (s/n): ").lower() == 's'
    usar_caracteres_especiales = input("¿Desea usar caracteres especiales en la contraseña? (s/n): ").lower() == 's'

    while True:
        contrasena = generar_contrasena(longitud, incluir_mayusculas, usar_caracteres_especiales)
        print("Tu nueva contraseña es:", contrasena)

        if solicitar_confirmacion():
            print("¡Contraseña generada con éxito!")
            break
        else:
            print("Generando una nueva contraseña...")

if __name__ == "__main__":
    main()
