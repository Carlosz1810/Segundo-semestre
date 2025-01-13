# Programa sencillo que realiza cálculos de áreas y conversiones de unidades

import math


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2  # Fórmula para el área de un círculo


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return base * altura  # Fórmula para el área de un rectángulo


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return 0.5 * base * altura  # Fórmula para el área de un triángulo


# Función para convertir metros a kilómetros
def convertir_metros_a_kilometros(metros):
    """
    Convierte una cantidad de metros a kilómetros.

    Parámetros:
    metros (float): La cantidad de metros.

    Retorna:
    float: La cantidad convertida en kilómetros.
    """
    return metros / 1000  # Conversión de metros a kilómetros


# Función para convertir kilómetros a metros
def convertir_kilometros_a_metros(kilometros):
    """
    Convierte una cantidad de kilómetros a metros.

    Parámetros:
    kilometros (float): La cantidad de kilómetros.

    Retorna:
    float: La cantidad convertida en metros.
    """
    return kilometros * 1000  # Conversión de kilómetros a metros


# Función para obtener una entrada numérica del usuario
def obtener_entrada_numerica(mensaje):
    """
    Solicita una entrada numérica al usuario y maneja los errores si se ingresa un valor no válido.

    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario.

    Retorna:
    float: La entrada numérica proporcionada por el usuario.
    """
    while True:
        try:
            return float(input(mensaje))  # Solicita la entrada y la convierte a flotante
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")  # Mensaje de error si la entrada no es numérica


# Función principal que gestiona la interacción con el usuario
def main():
    """
    Función principal que permite al usuario elegir qué operación realizar.
    El usuario puede elegir calcular áreas de figuras o realizar conversiones de unidades.
    """
    print("¡Bienvenido al programa de cálculos y conversiones!")

    continuar = True
    while continuar:
        # Menú de opciones
        print("\nMenú de opciones:")
        print("1. Calcular área de una figura")
        print("2. Convertir unidades de medida")
        print("3. Salir del programa")

        # Obtener la opción seleccionada
        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == "1":
            # Submenú para calcular el área de una figura
            print("\nOpciones para calcular el área:")
            print("1. Área de un círculo")
            print("2. Área de un rectángulo")
            print("3. Área de un triángulo")

            figura = input("Elige una opción (1, 2 o 3): ")

            if figura == "1":
                radio = obtener_entrada_numerica("Introduce el radio del círculo: ")
                area = calcular_area_circulo(radio)
                print(f"El área del círculo es: {area:.2f} unidades cuadradas.")

            elif figura == "2":
                base = obtener_entrada_numerica("Introduce la base del rectángulo: ")
                altura = obtener_entrada_numerica("Introduce la altura del rectángulo: ")
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")

            elif figura == "3":
                base = obtener_entrada_numerica("Introduce la base del triángulo: ")
                altura = obtener_entrada_numerica("Introduce la altura del triángulo: ")
                area = calcular_area_triangulo(base, altura)
                print(f"El área del triángulo es: {area:.2f} unidades cuadradas.")

            else:
                print("Opción no válida. Volviendo al menú principal.")

        elif opcion == "2":
            # Submenú para convertir unidades
            print("\nOpciones para convertir unidades:")
            print("1. Convertir metros a kilómetros")
            print("2. Convertir kilómetros a metros")

            conversion = input("Elige una opción (1 o 2): ")

            if conversion == "1":
                metros = obtener_entrada_numerica("Introduce la cantidad de metros: ")
                kilometros = convertir_metros_a_kilometros(metros)
                print(f"{metros} metros son {kilometros:.2f} kilómetros.")

            elif conversion == "2":
                kilometros = obtener_entrada_numerica("Introduce la cantidad de kilómetros: ")
                metros = convertir_kilometros_a_metros(kilometros)
                print(f"{kilometros} kilómetros son {metros:.2f} metros.")

            else:
                print("Opción no válida. Volviendo al menú principal.")

        elif opcion == "3":
            # Salir del programa
            print("¡Hasta luego!")
            continuar = False  # Cambiar el valor de la variable para salir del bucle

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
