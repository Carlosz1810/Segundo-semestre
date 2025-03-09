# Clase Libro: Representa un libro con título, autor, categoría y ISBN
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario: Representa un usuario con nombre, ID y libros prestados
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def mostrar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(libro)
        else:
            print(f"{self.nombre} no tiene libros prestados.")


# Clase Biblioteca: Gestiona los libros y usuarios
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros
        self.usuarios = []  # Lista de usuarios

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros:
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def obtener_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def prestar_libro(self, id_usuario, isbn):
        usuario = self.obtener_usuario(id_usuario)
        libro = self.buscar_libros("isbn", isbn)
        if usuario and libro:
            usuario.prestar_libro(libro[0])
            print(f"Libro '{libro[0].titulo}' prestado a {usuario.nombre}.")
        else:
            print("No se pudo realizar el préstamo. Verifique el usuario o el ISBN.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.obtener_usuario(id_usuario)
        if usuario:
            usuario.devolver_libro(isbn)
            print(f"Libro con ISBN {isbn} devuelto por {usuario.nombre}.")
        else:
            print("Usuario no encontrado.")


# Funciones auxiliares
def mostrar_menu():
    print("\n=====  Sistema de Gestión de Biblioteca Digital  =====")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Eliminar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Buscar libro")
    print("7. Listar libros prestados")
    print("8. Salir")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)
            print(f"Usuario {nombre} registrado exitosamente.")

        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado a la biblioteca.")

        elif opcion == '3':
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")

        elif opcion == '4':
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '5':
            id_usuario = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '6':
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input(f"Ingrese el {criterio} a buscar: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            if resultados:
                print("\nLibros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print(f"No se encontraron libros con {criterio} '{valor}'.")

        elif opcion == '7':
            id_usuario = input("Ingrese el ID del usuario para listar sus libros prestados: ")
            usuario = biblioteca.obtener_usuario(id_usuario)
            if usuario:
                usuario.mostrar_libros_prestados()
            else:
                print("Usuario no encontrado.")

        elif opcion == '8':
            print("Gracias por usar el sistema de gestión de la biblioteca.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
