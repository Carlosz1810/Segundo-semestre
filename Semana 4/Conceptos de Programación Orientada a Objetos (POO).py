class Bicicleta:
    def __init__(self, id_bicicleta, tipo, precio, disponible=True):
        """
        Inicializa una bicicleta con un ID, tipo, precio y disponibilidad.
        :param id_bicicleta: ID de la bicicleta.
        :param tipo: tipo de bicicleta (por ejemplo, "urbana", "de montaña").
        :param precio: precio por hora del alquiler de la bicicleta.
        :param disponible: disponibilidad de la bicicleta (por defecto True).
        """
        self.id_bicicleta = id_bicicleta
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def mostrar_info(self):
        """ Muestra la información de la bicicleta """
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Bicicleta {self.id_bicicleta} ({self.tipo}) - {disponibilidad}, Precio: ${self.precio} por hora."

    def alquilar(self):
        """ Marca la bicicleta como alquilada (no disponible) """
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        """ Devuelve la bicicleta, marcándola como disponible """
        if not self.disponible:
            self.disponible = True
            return True
        return False


class Cliente:
    def __init__(self, nombre):
        """
        Inicializa un cliente con su nombre y una lista de alquileres.
        :param nombre: nombre del cliente.
        """
        self.nombre = nombre
        self.alquileres = []

    def alquilar_bicicleta(self, bicicleta):
        """ Intenta alquilar una bicicleta """
        if bicicleta.alquilar():
            self.alquileres.append(bicicleta)
            return f"Alquiler realizado para la bicicleta {bicicleta.id_bicicleta}."
        else:
            return f"La bicicleta {bicicleta.id_bicicleta} no está disponible."

    def devolver_bicicleta(self, bicicleta):
        """ Devuelve una bicicleta alquilada """
        if bicicleta in self.alquileres and bicicleta.devolver():
            self.alquileres.remove(bicicleta)
            return f"Bicicleta {bicicleta.id_bicicleta} devuelta."
        return f"No tienes alquiler de la bicicleta {bicicleta.id_bicicleta}."

    def ver_alquileres(self):
        """ Muestra todas las bicicletas alquiladas por el cliente """
        if not self.alquileres:
            return "No tienes alquileres activos."
        return "\n".join([f"Bicicleta {bicicleta.id_bicicleta} ({bicicleta.tipo})" for bicicleta in self.alquileres])


class Tienda:
    def __init__(self, nombre):
        """
        Inicializa la tienda con su nombre y una lista de bicicletas.
        :param nombre: nombre de la tienda.
        """
        self.nombre = nombre
        self.bicicletas = []

    def agregar_bicicleta(self, bicicleta):
        """ Agrega una bicicleta a la tienda """
        self.bicicletas.append(bicicleta)

    def mostrar_bicicletas_disponibles(self):
        """ Muestra todas las bicicletas disponibles en la tienda """
        bicicletas_disponibles = [bicicleta.mostrar_info() for bicicleta in self.bicicletas if bicicleta.disponible]
        return "\n".join(bicicletas_disponibles) if bicicletas_disponibles else "No hay bicicletas disponibles."

    def encontrar_bicicleta_por_numero(self, numero):
        """ Busca una bicicleta disponible por número (ID) """
        for bicicleta in self.bicicletas:
            if bicicleta.id_bicicleta == numero and bicicleta.disponible:
                return bicicleta
        return None


def mostrar_menu():
    print("\n---- Menú de Opciones ----")
    print("1. Ver bicicletas disponibles")
    print("2. Alquilar una bicicleta")
    print("3. Devolver una bicicleta")
    print("4. Ver mis alquileres")
    print("5. Salir")


def interactuar_con_usuario(cliente, tienda):
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            print("\nBicicletas disponibles en la tienda:")
            print(tienda.mostrar_bicicletas_disponibles())

        elif opcion == "2":
            print("\nSelecciona el número de la bicicleta que deseas alquilar:")
            # Mostrar todas las bicicletas disponibles con su número
            for i, bicicleta in enumerate(tienda.bicicletas, 1):
                if bicicleta.disponible:
                    print(f"{i}. {bicicleta.tipo} - ID: {bicicleta.id_bicicleta}, Precio: ${bicicleta.precio}/hora")

            try:
                seleccion = int(input("Ingresa el número de la bicicleta que deseas alquilar: "))
                bicicleta = tienda.encontrar_bicicleta_por_numero(seleccion)

                if bicicleta:
                    print(cliente.alquilar_bicicleta(bicicleta))
                else:
                    print("Opción no válida o la bicicleta no está disponible.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "3":
            if not cliente.alquileres:
                print("\nNo tienes alquileres para devolver.")
            else:
                print("\nTus alquileres actuales:")
                print(cliente.ver_alquileres())

                try:
                    id_bicicleta = int(input("Ingresa el ID de la bicicleta que deseas devolver: "))
                    bicicleta_a_devolver = None
                    for bicicleta in cliente.alquileres:
                        if bicicleta.id_bicicleta == id_bicicleta:
                            bicicleta_a_devolver = bicicleta
                            break

                    if bicicleta_a_devolver:
                        print(cliente.devolver_bicicleta(bicicleta_a_devolver))
                    else:
                        print("No tienes un alquiler con ese ID de bicicleta.")
                except ValueError:
                    print("Por favor, ingresa un ID válido.")

        elif opcion == "4":
            print("\nTus alquileres actuales:")
            print(cliente.ver_alquileres())

        elif opcion == "5":
            print("Gracias por utilizar nuestro sistema de alquiler de bicicletas. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 5.")


# Crear la tienda y algunas bicicletas
tienda = Tienda("Tienda de Bicicletas Speedbiker")
tienda.agregar_bicicleta(Bicicleta(1, "Urbana", 10))
tienda.agregar_bicicleta(Bicicleta(2, "De montaña", 15))
tienda.agregar_bicicleta(Bicicleta(3, "De carretera", 20))

# Crear un cliente
nombre_cliente = input("¡Bienvenido a la Tienda de Bicicletas Speedbiker! ¿Cómo te llamas? ")
cliente = Cliente(nombre_cliente)

# Iniciar la interacción con el usuario
interactuar_con_usuario(cliente, tienda)
