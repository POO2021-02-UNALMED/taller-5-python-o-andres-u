from Animal import Animal


class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls):
        pass

    @classmethod
    def crearSalamandra(cls):
        pass
