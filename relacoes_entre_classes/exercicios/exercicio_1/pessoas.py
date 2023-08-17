"""
Classes _Pessoa (abstrata) e Cliente

O arquivo contém duas classes, a Classe abstrata _Pessoa e a classe Cliente, que herda da classe _Pessoa. A Classe
_Pessoa não deve ser usada, apenas sua classe filha deve ser usada, a classe Cliente. A classe Cliente recebe argumentos
nome, idade e conta. O atributo 'conta' deve ser do tipo da classe 'Conta', onde é feita uma associação.
"""

# Importando a classe ABC e a função abstractmethod
from abc import ABC, abstractmethod
# Importando a classe 'Conta'
from contas import Conta


# Criando a classe abstrata '_Pessoa'
class _Pessoa(ABC):
    # Definindo o método init
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    # Definindo o método abstrato getter para o nome
    @property
    @abstractmethod
    def nome(self) -> str: ...

    # Definindo o método abstrato setter para o nome
    @nome.setter
    @abstractmethod
    def nome(self, nome: str) -> None: ...

    # Definindo o método abstrato getter para a idade
    @property
    @abstractmethod
    def idade(self) -> str: ...

    # Definindo o método abstrato setter para a idade
    @idade.setter
    @abstractmethod
    def idade(self, idade: int) -> None: ...


# Criando a classe 'Cliente', que herda da classe '_Pessoa'
class Cliente(_Pessoa):
    # Definindo o método init
    def __init__(self, nome: str, idade: int, conta: Conta) -> None:
        super().__init__(nome, idade)
        self.conta = conta

    # Definindo o método getter para o nome
    @property
    def nome(self) -> str:
        return self._nome

    # Definindo o método setter para o nome
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    # Definindo o método getter para a idade
    @property
    def idade(self) -> int:
        return self._idade

    # Definindo o método setter para a idade
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade
