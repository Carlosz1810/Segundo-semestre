import os

class Articulo:
    def __init__(self, nombre, stock, costo):
        self.nombre = nombre
        self.stock = stock
        self.costo = costo

    def __str__(self):
        return f"{self.nombre},{self.stock},{self.costo}"

    @staticmethod
    def from_string(data):
        nombre, stock, costo = data.strip().split(',')
        return Articulo(nombre, int(stock), float(costo))

class Almacen:
    ARCHIVO = "almacen.txt"

    def __init__(self):
        self.articulos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            open(self.ARCHIVO, 'w').close()
            return
        try:
            with open(self.ARCHIVO, "r") as archivo:
                self.articulos = {a.nombre: a for a in map(Articulo.from_string, archivo)}
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as archivo:
                archivo.writelines(f"{a}\n" for a in self.articulos.values())
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_articulo(self, nombre, stock, costo):
        if nombre in self.articulos:
            print("El artículo ya existe. Use la opción de actualización.")
        else:
            self.articulos[nombre] = Articulo(nombre, stock, costo)
            self.guardar_en_archivo()
            print("Artículo agregado correctamente.")

    def actualizar_articulo(self, nombre, stock, costo):
        if nombre in self.articulos:
            self.articulos[nombre].stock = stock
            self.articulos[nombre].costo = costo
            self.guardar_en_archivo()
            print("Artículo actualizado correctamente.")
        else:
            print("El artículo no existe.")

    def eliminar_articulo(self, nombre):
        if self.articulos.pop(nombre, None):
            self.guardar_en_archivo()
            print("Artículo eliminado correctamente.")
        else:
            print("El artículo no existe.")

    def mostrar_almacen(self):
        if not self.articulos:
            print("El almacén está vacío.")
        else:
            print("\nInventario del Almacén:")
            print("-" * 30)
            for articulo in self.articulos.values():
                print(f"Nombre: {articulo.nombre}, Stock: {articulo.stock}, Costo: {articulo.costo}")
            print("-" * 30)

if __name__ == "__main__":
    almacen = Almacen()
    while True:
        print("\n***** Gestión de Almacén *****")
        print("1. Agregar artículo")
        print("2. Actualizar artículo")
        print("3. Eliminar artículo")
        print("4. Mostrar almacén")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del artículo: ").strip()
            stock = int(input("Stock: "))
            costo = float(input("Costo: "))
            almacen.agregar_articulo(nombre, stock, costo)
        elif opcion == "2":
            nombre = input("Nombre del artículo: ").strip()
            stock = int(input("Nuevo stock: "))
            costo = float(input("Nuevo costo: "))
            almacen.actualizar_articulo(nombre, stock, costo)
        elif opcion == "3":
            nombre = input("Nombre del artículo a eliminar: ").strip()
            almacen.eliminar_articulo(nombre)
        elif opcion == "4":
            almacen.mostrar_almacen()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
