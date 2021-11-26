from Animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        caballo = Mamifero(pelaje=True, patas=4, habitat="pradera", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(caballo)
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        leon = Mamifero(pelaje=True, patas=4, habitat="pradera", nombre=nombre, edad=edad, genero=genero)
        cls._listado.append(leon)
        return leon
