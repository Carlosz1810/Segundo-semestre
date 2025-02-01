import os

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un archivo Python en la consola."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    if not os.path.exists(ruta_script_absoluta):
        print(f"El archivo {ruta_script} no se encontró.")
        return
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """Muestra un menú para seleccionar y visualizar los archivos del curso."""
    ruta_base = os.path.abspath(os.path.dirname(__file__))

    opciones = {
        '1': 'Semana 2/Semana 2.py',
        '2': 'Semana 3/Programación Orientada a Objetos (POO).py',
        '3': 'Semana 3/Programación Tradicional.py',
        '4': 'Semana 4/Conceptos de Programación Orientada a Objetos (POO).py',
        '5': 'Semana 5/Tipos de datos, Identificadores.py',
        '6': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'Semana 7/Constructores y Destructores.py'
    }

    while True:
        print("\n*** Menú Principal - Carlos Medina's Dashboard ***")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
