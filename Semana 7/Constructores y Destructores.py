import os


class RegistroActividades:
    """
    Clase para gestionar un archivo temporal con el registro de actividades físicas.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor de la clase. Crea un archivo temporal para registrar actividades físicas.
        :param nombre_archivo: Nombre del archivo temporal.
        """
        self.nombre_archivo = nombre_archivo
        print(f"Creando el archivo de registro de actividades: {self.nombre_archivo}")
        try:
            # Crear el archivo con un encabezado inicial
            with open(self.nombre_archivo, 'w') as archivo:
                archivo.write("Registro de Actividades Físicas\n")
                archivo.write("===============================\n")
        except OSError as e:
            print(f"Error al crear el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"Archivo {self.nombre_archivo} creado exitosamente.")

    def agregar_actividad(self, actividad, duracion):
        """
        Agrega una actividad física al registro.
        :param actividad: Nombre de la actividad (e.g., correr, caminar).
        :param duracion: Duración de la actividad en minutos.
        """
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                archivo.write(f"Actividad: {actividad}, Duración: {duracion} minutos\n")
        except OSError as e:
            print(f"Error al escribir en el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"Actividad agregada: {actividad} - {duracion} minutos")

    def leer_registro(self):
        """
        Muestra todas las actividades registradas.
        """
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            print(f"\nContenido del archivo {self.nombre_archivo}:\n{contenido}")
        except OSError as e:
            print(f"Error al leer el archivo {self.nombre_archivo}: {e}")

    def __del__(self):
        """
        Destructor de la clase. Elimina el archivo temporal con el registro de actividades.
        """
        if os.path.exists(self.nombre_archivo):
            try:
                os.remove(self.nombre_archivo)
                print(f"El archivo {self.nombre_archivo} ha sido eliminado.")
            except OSError as e:
                print(f"Error al eliminar el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"El archivo {self.nombre_archivo} ya no existe.")


if __name__ == "__main__":
    print("Bienvenido al programa de registro de actividades físicas.")

    # Solicitar al usuario el nombre del archivo de registro
    nombre_archivo = input("Ingrese el nombre del archivo para registrar actividades (Ejemplo: actividades.txt): ").strip()
    if not nombre_archivo:
        print("El nombre del archivo no puede estar vacío. Saliendo del programa.")
        exit(1)

    registro = RegistroActividades(nombre_archivo)

    # Menú interactivo
    while True:
        print("\nOpciones:")
        print("1. Agregar una actividad")
        print("2. Leer el registro de actividades")
        print("3. Salir (el archivo será eliminado)")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            actividad = input("Ingrese el nombre de la actividad (Ejemplo: caminar, correr): ").strip()
            try:
                duracion = int(input("Ingrese la duración en minutos: ").strip())
                if duracion > 0:
                    registro.agregar_actividad(actividad, duracion)
                else:
                    print("La duración debe ser un número positivo.")
            except ValueError:
                print("Debe ingresar un valor numérico para la duración.")
        elif opcion == "2":
            registro.leer_registro()
        elif opcion == "3":
            print("Saliendo del programa. El archivo será eliminado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    # El archivo se elimina automáticamente al salir del programa
