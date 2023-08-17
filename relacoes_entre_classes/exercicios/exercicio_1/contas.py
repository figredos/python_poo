"""
Classes Conta (abstrata), ContaCorrente, e ContaPoupança

O arquivo contém 3 classes, a classe Conta é abstrata e força a criação do método sacar em todas as que herdam dela, no
caso são a Classe ContaPoupança e a classe ContaCorrente. Cada uma tem funções similares, com a grande diferença sendo o
limite da ContaCorrente sendo maior que o saldo disponível na mesma. Tornando o método sacar um exemplo de polimorfismo.
"""

# Importando a Classe ABC e a função abstractmethod
from abc import ABC, abstractmethod


# Criando a classe Conta
class Conta(ABC):
    # Definindo o método init
    def __init__(self, agencia: int, numero_conta: int, limite: int, saldo: int = 0, autenticada: bool = False) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self._limite = limite
        self._saldo = saldo
        self._autenticada = autenticada

    # Definindo o método depositar
    def depositar(self, valor: int) -> None:
        if not self._autenticada:
            print('A conta ainda não foi autenticada')
            return

        self._saldo += valor

        print(f'Valor de R${valor} depositado com sucesso')

    # Fazendo abstração do método sacar
    @abstractmethod
    def sacar(self, valor: int) -> None: ...

    # Definindo o getter do valor do saldo
    @property
    def saldo(self) -> str:
        return f'O saldo atual é de {self._saldo}'


# Criando a classe 'ContaPoupanca'
class ContaPoupanca(Conta):
    # Definindo o método abstrato sacar
    def sacar(self, valor: int) -> None:
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        print(f'Valor de R${valor} foi sacado da conta de número {self.numero_conta} com sucesso!')
        self._saldo -= valor


# Criando a classe 'ContaCorrente'
class ContaCorrente(Conta):
    # Defindo o init da classe, que possui o atributo 'limite_extra'
    def __init__(self, agencia: int,
                 numero_conta: int,
                 limite: int,
                 limite_extra: int = 100,
                 saldo: int = 0,
                 autenticada: bool = False,
                 ):
        super().__init__(agencia, numero_conta, limite, saldo, autenticada)
        self._limite_extra = limite_extra

    # Definindo o método abstrato 'sacar'
    def sacar(self, valor: int) -> None:
        if not self._autenticada:
            print('A conta ainda não foi autenticada')
            return
        if self._saldo + self._limite_extra < valor:
            print('Saldo insuficiente')
            return
        print(f'Valor de R${valor} foi sacado da conta de número {self.numero_conta} com sucesso!')
        self._saldo -= valor

        if self._saldo < 0:
            self._limite_extra -= self._saldo
            self._saldo = 0
