from Animal import Animal


class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        len(cls._listado)

    def movimiento(self):
        return "flying"

    @staticmethod
    def crearHalcon():
        pass

    @staticmethod
    def crearAguila():
        pass
