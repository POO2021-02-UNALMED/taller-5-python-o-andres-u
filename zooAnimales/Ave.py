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

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        halcon = Ave(colorPlumas="cafe glorioso", habitat="montanas", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(halcon)
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        aguila = Ave(colorPlumas="blanco y amarillo", habitat="montanas", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(aguila)
        return aguila
