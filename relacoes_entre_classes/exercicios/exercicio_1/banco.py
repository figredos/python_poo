"""
Classe Banco

A classe banco faz o uso da Agregação com o objeto da classe Conta (seja essa ContaCorrente ou ContaPoupança), com
objetos da classe Cliente. Faz isso para fazer a autenticação de uma certa conta, de um certo cliente, liberando o
método de saque de dentro das contas.
"""

# Importando a classe Cliente
from pessoas import Cliente


# Criando a classe Banco
class Banco:
    # Definindo o método init
    def __init__(self, agencia, clientes: list, numero_contas: list):
        self._agencia = agencia
        self._clientes = clientes
        self._numero_contas = numero_contas

    # Definindo o método autenticar
    def autenticar(self, cliente: Cliente):
        # Checando se o cliente pertence ao banco
        if cliente.nome in self._clientes:
            print(f'Cliente {cliente.nome} encontrado, buscando conta...')

            # Checando se a conta pertence ao banco
            if cliente.conta.numero_conta in self._numero_contas and cliente.conta.agencia == self._agencia:
                print('Conta encontrada, autenticação realizada com sucesso!')
                cliente.conta._autenticada = True
                return

            print(f'Conta {cliente.conta.numero_conta} não foi encontrada, autenticação falhou!')
            return

        print(f'Cliente {cliente.nome} não foi encontrado, autenticação falhou!')
        return
