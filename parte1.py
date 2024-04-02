import random

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def generar_nombre_usuario(nombre, apellido, año_nacimiento):
    return nombre.capitalize() + apellido.capitalize() + str(año_nacimiento)

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    
    while True:
        intento = int(input("Intenta adivinar el número (entre 1 y 100): "))
        intentos += 1
        
        if intento == numero_aleatorio:
            print("¡Felicidades! Has adivinado el número en", intentos, "intentos.")
            break
        elif intento < numero_aleatorio:
            print("El número es mayor. Inténtalo de nuevo.")
        else:
            print("El número es menor. Inténtalo de nuevo.")

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def calcular_factorial_while(numero):
    factorial = 1
    i = 1
    while i <= numero:
        factorial *= i
        i += 1
    return factorial

def contar_vocales(frase):
    vocales = 'aeiouAEIOU'
    contador = 0
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

def crear_lista_compra():
    lista_compra = []
    while True:
        item = input("Ingrese un elemento para agregar a la lista de compras (o 'fin' para terminar): ")
        if item.lower() == 'fin':
            break
        else:
            lista_compra.append(item)
    return lista_compra

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

def crear_diccionario_sinonimos():
    diccionario_sinonimos = {}
    while True:
        palabra = input("Ingrese una palabra: ")
        if palabra.lower() == 'fin':
            break
        else:
            sinonimos = input("Ingrese sinónimos separados por comas: ").split(',')
            diccionario_sinonimos[palabra] = sinonimos
    return diccionario_sinonimos

def mostrar_menu():
    print("1. Conversor de Temperatura")
    print("2. Calculadora de IMC")
    print("3. Generador de Nombre de Usuario")
    print("4. Adivina el Número")
    print("5. Calculadora de Factorial (con for)")
    print("6. Calculadora de Factorial (con while)")
    print("7. Contador de Vocales")
    print("8. Lista de la Compra")
    print("9. Eliminación de Duplicados")
    print("10. Diccionario de Sinónimos")
    print("11. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            temperatura = float(input("Ingresa la temperatura: "))
            unidad_origen = input("¿La temperatura está en Celsius o Fahrenheit? (C/F): ").upper()
            
            if unidad_origen == 'C':
                resultado = celsius_a_fahrenheit(temperatura)
                print("La temperatura en Fahrenheit es:", resultado)
            elif unidad_origen == 'F':
                resultado = fahrenheit_a_celsius(temperatura)
                print("La temperatura en Celsius es:", resultado)
            else:
                print("Unidad no válida. Por favor, ingresa 'C' o 'F'.")
        elif opcion == '2':
            peso = float(input("Ingresa tu peso en kg: "))
            altura = float(input("Ingresa tu altura en metros: "))
            imc = calcular_imc(peso, altura)
            print("Tu Índice de Masa Corporal (IMC) es:", imc)
        elif opcion == '3':
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            año_nacimiento = input("Ingresa tu año de nacimiento: ")
            nombre_usuario = generar_nombre_usuario(nombre, apellido, año_nacimiento)
            print("Tu nombre de usuario es:", nombre_usuario)
        elif opcion == '4':
            adivinar_numero()
        elif opcion == '5':
            numero = int(input("Ingresa un número para calcular su factorial: "))
            factorial = calcular_factorial(numero)
            print("El factorial de", numero, "es:", factorial)
        elif opcion == '6':
            numero = int(input("Ingresa un número para calcular su factorial: "))
            factorial = calcular_factorial_while(numero)
            print("El factorial de", numero, "es:", factorial)
        elif opcion == '7':
            frase = input("Ingresa una frase para contar las vocales: ")
            cantidad_vocales = contar_vocales(frase)
            print("La cantidad de vocales en la frase es:", cantidad_vocales)
        elif opcion == '8':
            print("Creando lista de compras...")
            lista_compra = crear_lista_compra()
            print("Lista de compras:", lista_compra)
        elif opcion == '9':
            lista_numeros = input("Ingrese una lista de números separados por comas: ").split(',')
            lista_sin_duplicados = eliminar_duplicados(lista_numeros)
            print("Lista sin duplicados:", lista_sin_duplicados)
        elif opcion == '10':
            print("Creando diccionario de sinónimos...")
            diccionario_sinonimos = crear_diccionario_sinonimos()
            print("Diccionario de sinónimos:", diccionario_sinonimos)
        elif opcion == '11':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
