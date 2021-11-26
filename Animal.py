class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    def movimiento(self):
        return "moving"

    def totalPorTipo(self):
        return "total"

    def __str__(self):
        return "string"
