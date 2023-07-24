# Importando a classe ABC e abstractmethod
from abc import ABC, abstractmethod


# Criando a classe Abstrata 'AbstractFoo', herdando de ABC
class AbstractFoo(ABC):
    # Definindo o init
    def __init__(self, name):
        self._name = name

    # Criando um getter concreto
    @property
    def name(self):
        return self._name

    # Criando um setter abstrato
    @name.setter
    @abstractmethod
    def name(self, name):...


# Criando a classe 'Foo' que herda da classe abstrata acima
class Foo(AbstractFoo):
    # Definindo o init
    def __init__(self, name):
        super().__init__(name)
        # print('sou inútil')

    # Criando o método setter, como estipulado pela classe pai
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


# Instanciando e testando
foo = Foo('Bar')
print(foo.name)
