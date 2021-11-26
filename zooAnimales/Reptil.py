from Animal import Animal


class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls):
        pass

    @classmethod
    def crearSerpiente(cls):
        pass
