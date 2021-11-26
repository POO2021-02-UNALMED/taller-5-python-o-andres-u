from Animal import Animal


class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearIguana(cls):
        pass

    @classmethod
    def crearSerpiente(cls):
        pass
