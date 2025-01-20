# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        # Atributos de la clase base, encapsulados como propiedades
        self._marca = marca
        self._modelo = modelo
        self._anio = self._validar_anio(anio)

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = self._validar_anio(anio)

    def _validar_anio(self, anio):
        """Método auxiliar para validar el año de fabricación"""
        if anio > 1885:  # El primer automóvil fue inventado en 1886
            return anio
        else:
            raise ValueError("El año no es válido para un vehículo.")

    def mover(self):
        """Método de comportamiento común para todas las clases derivadas"""
        return "El vehículo se mueve."

# Clase derivada: Carro (hereda de Vehiculo)
class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self._puertas = puertas

    @property
    def puertas(self):
        return self._puertas

    @puertas.setter
    def puertas(self, puertas):
        self._puertas = puertas

    def mover(self):
        return f"El carro {self.marca} {self.modelo} con {self.puertas} puertas, está conduciendo."

# Clase derivada: Moto (hereda de Vehiculo)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def mover(self):
        return f"La moto {self.marca} {self.modelo} de tipo {self.tipo}, está circulando."

# Función para validar que el año sea válido (en caso de no usar setter directamente)
def validar_anio():
    while True:
        try:
            anio = int(input("Ingresa el año del vehículo: "))
            return anio
        except ValueError:
            print("Por favor, ingresa un año válido.")

# Función principal para interactuar con el usuario
def main():
    print("Bienvenido al programa de vehículos.\n")

    # Se asegura de que el tipo de vehículo sea válido
    while True:
        tipo_vehiculo = input("¿Qué tipo de vehículo deseas crear? (Carro/Moto): ").strip().lower()
        if tipo_vehiculo in ["carro", "moto"]:
            break
        else:
            print("Opción no válida. Por favor elige 'Carro' o 'Moto'.\n")

    marca = input("Ingresa la marca del vehículo: ").strip()
    modelo = input("Ingresa el modelo del vehículo: ").strip()
    anio = validar_anio()

    # Crear el vehículo correspondiente según la elección del usuario
    if tipo_vehiculo == "carro":
        while True:
            try:
                puertas = int(input("Ingresa el número de puertas del carro: ").strip())
                break
            except ValueError:
                print("Por favor, ingresa un número válido para el número de puertas.")
        vehiculo = Carro(marca, modelo, anio, puertas)
    elif tipo_vehiculo == "moto":
        tipo = input("Ingresa el tipo de moto (por ejemplo, deportiva, niked, cross, etc): ").strip()
        vehiculo = Moto(marca, modelo, anio, tipo)

    # Muestra la información del vehículo creado
    print("\nInformación del vehículo creado:")
    print(f"Marca: {vehiculo.marca}")
    print(f"Modelo: {vehiculo.modelo}")
    print(f"Año: {vehiculo.anio}")

    if isinstance(vehiculo, Carro):
        print(f"Número de puertas: {vehiculo.puertas}")
    elif isinstance(vehiculo, Moto):
        print(f"Tipo de moto: {vehiculo.tipo}")

    # Mostrar cómo se mueve el vehículo
    print(f"Movimiento: {vehiculo.mover()}")

# Llamar a la función principal para que el programa inicie
if __name__ == "__main__":
    main()
