class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarzonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return sum([len(animales) for animales in self._zonas])

    def getNombre(self):
        return self._nombre
