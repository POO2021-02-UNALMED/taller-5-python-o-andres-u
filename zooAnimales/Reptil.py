from Animal import Animal


class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        iguana = Reptil(colorEscamas="verde", largoCola=3, habitat="humedal", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(iguana)
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        serpiente = Reptil(colorEscamas="blanco", largoCola=1, habitat="jungla", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(serpiente)
        return serpiente

