def encontrar_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

def concatenar_ordenar_listas(lista1, lista2):
    lista_combinada = lista1 + lista2
    lista_combinada.sort()
    return lista_combinada

def invertir_tupla(tupla):
    tupla_invertida = tuple(reversed(tupla))
    return tupla_invertida

def contar_palabras(cadena):
    palabras = cadena.split()
    contador_palabras = {}
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1
    return contador_palabras

def union_interseccion_conjuntos(conjunto1, conjunto2):
    union = conjunto1.union(conjunto2)
    interseccion = conjunto1.intersection(conjunto2)
    return union, interseccion

def manejar_agenda_telefonica(agenda):
    while True:
        print("\nAGENDA TELEFÓNICA")
        print("1. Añadir número")
        print("2. Eliminar número")
        print("3. Buscar número")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número de teléfono: ")
            agenda[nombre] = numero
            print("Número añadido a la agenda.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto para eliminar su número: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Número eliminado de la agenda.")
            else:
                print("El contacto no está en la agenda.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto para buscar su número: ")
            if nombre in agenda:
                print("El número de", nombre, "es:", agenda[nombre])
            else:
                print("El contacto no está en la agenda.")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def convertir_divisas(cantidad, tasa_cambio):
    cantidad_convertida = cantidad * tasa_cambio
    return cantidad_convertida

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def mostrar_menu():
    print("\nMENU")
    print("1. Mayores y Menores")
    print("2. Concatenación y Ordenación de Listas")
    print("3. Inversión de Tupla")
    print("4. Contador de Palabras")
    print("5. Unión e Intersección de Conjuntos")
    print("6. Agenda Telefónica")
    print("7. Conversión de Divisas")
    print("8. Función Recursiva de Fibonacci")
    print("9. Salir")

def main():
    agenda_telefonica = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            lista_numeros = [int(num) for num in input("Ingrese una lista de números separados por espacio: ").split()]
            mayor, menor = encontrar_mayor_menor(lista_numeros)
            print("El número mayor es:", mayor)
            print("El número menor es:", menor)
        elif opcion == '2':
            lista1 = [int(num) for num in input("Ingrese la primera lista de números separados por espacio: ").split()]
            lista2 = [int(num) for num in input("Ingrese la segunda lista de números separados por espacio: ").split()]
            lista_concatenada_ordenada = concatenar_ordenar_listas(lista1, lista2)
            print("Lista combinada y ordenada:", lista_concatenada_ordenada)
        elif opcion == '3':
            tupla_original = tuple(input("Ingrese una tupla de elementos separados por espacio: ").split())
            tupla_invertida = invertir_tupla(tupla_original)
            print("Tupla invertida:", tupla_invertida)
        elif opcion == '4':
            texto = input("Ingrese una cadena de texto: ")
            contador_palabras_resultado = contar_palabras(texto)
            print("Contador de palabras:", contador_palabras_resultado)
        elif opcion == '5':
            conjunto1 = set(input("Ingrese el primer conjunto de elementos separados por espacio: ").split())
            conjunto2 = set(input("Ingrese el segundo conjunto de elementos separados por espacio: ").split())
            union, interseccion = union_interseccion_conjuntos(conjunto1, conjunto2)
            print("Unión de conjuntos:", union)
            print("Intersección de conjuntos:", interseccion)
        elif opcion == '6':
            manejar_agenda_telefonica(agenda_telefonica)
        elif opcion == '7':
            cantidad = float(input("Ingrese la cantidad de dinero a convertir: "))
            tasa_cambio = float(input("Ingrese la tasa de cambio: "))
            cantidad_convertida = convertir_divisas(cantidad, tasa_cambio)
            print("Cantidad convertida:", cantidad_convertida)
        elif opcion == '8':
            n = int(input("Ingrese el valor de n para calcular el número de Fibonacci: "))
            resultado = fibonacci_recursivo(n)
            print("El número de Fibonacci para n =", n, "es:", resultado)
        elif opcion == '9':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
