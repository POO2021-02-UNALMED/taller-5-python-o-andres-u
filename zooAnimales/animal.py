import zooAnimales


class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def movimiento(self):
        return "moving"

    def totalPorTipo(self):
        return f'''
            Mamiferos: ${zooAnimales.Mamifero.cantidadMamiferos()}
            Aves: ${zooAnimales.Ave.cantidadAves()}
            Reptiles: ${zooAnimales.Reptil.cantidadReptiles()}
            Anfibios: ${zooAnimales.Anfibio.cantidadAnfibios()}
        '''

    def __str__(self):
        message = f"Mi nombre es ${self._nombre}, tengo una edad de ${self._edad}, habito en ${self._habitat} y mi genero es ${self._genero}"
        if self._zona:
            return f"${message}, la zona en la que me ubico es {self._zona.getNombre()}, en el ${self._zona.getZoo().getNombre()}"
        else:
            return message
