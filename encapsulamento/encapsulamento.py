# Criando uma classe
class Encapsulamento:
    def __init__(self):
        self.public = 'Esse atributo é público'
        self._protected = 'Esse atributo é protegido'
        self.__privado = 'Esse atributo é privado'

    def metodo_publico(self):
        print(self.__privado)
        print(self._protected)
        print(self.public)
        return 'metodo publico'

    def _metodo_protected(self):
        print(self.__privado)
        print(self._protected)
        print(self.public)
        return 'metodo protegido'

    def __metodo_private(self):
        print(self.__privado)
        print(self._protected)
        print(self.public)
        return 'metodo privado'