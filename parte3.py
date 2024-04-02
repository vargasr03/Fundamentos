def registrar_usuario(nombre, edad):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}, Edad: {edad}\n")

def leer_poema(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            poema = archivo.read()
            print(poema)
    except FileNotFoundError:
        print("El archivo no se encontró.")

def analizar_log(nombre_archivo, patron):
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            errores = [linea.strip() for linea in lineas if patron in linea]
            if errores:
                print("Se encontraron los siguientes errores:")
                for error in errores:
                    print(error)
            else:
                print("No se encontraron errores con el patrón especificado.")
    except FileNotFoundError:
        print("El archivo no se encontró.")

def mostrar_menu():
    print("\nMENU")
    print("1. Registrar Usuario")
    print("2. Leer Poema")
    print("3. Analizar Log")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Ingrese su nombre: ")
            edad = input("Ingrese su edad: ")
            registrar_usuario(nombre, edad)
            print("Usuario registrado con éxito.")
        elif opcion == '2':
            nombre_archivo = input("Ingrese el nombre del archivo de poema: ")
            leer_poema(nombre_archivo)
        elif opcion == '3':
            nombre_archivo = input("Ingrese el nombre del archivo de registro (log): ")
            patron = input("Ingrese el patrón a buscar: ")
            analizar_log(nombre_archivo, patron)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
