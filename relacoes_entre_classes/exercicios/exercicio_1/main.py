"""
main

Nesse arquivo são feitas as relações entre as classes de modo a criar uma conta, um cliente e um banco. E com isso
autenticar a conta e fazer um saque.
"""

# Importando as classes dos arquivos adjacentes
from contas import ContaCorrente, ContaPoupanca
from pessoas import Cliente
from banco import Banco

# Instanciando as classes 'ContaPoupança' e 'Cliente'
conta_corrente_1 = ContaPoupanca(000, 4242, 100)
cliente_1 = Cliente('Giulia', 20, conta_corrente_1)

# Tentando fazer um depósito
cliente_1.conta.depositar(100)

# Criando  as listas de clientes e contas do banco
clientes_banco = ['matheus', 'Giulia', 'Fellet']
contas_banco = [4242, 2436, 8787]

# Instanciando a classe 'Banco'
banco_1 = Banco(000, numero_contas=contas_banco, clientes=clientes_banco)

# Fazendo a autenticação da conta do 'cliente_1'
banco_1.autenticar(cliente_1)

# Tentando fazer o depósito novamente
cliente_1.conta.depositar(100)

# Tentando fazer um saque
cliente_1.conta.sacar(100)

# Imprimindo o saldo da conta
print(cliente_1.conta.saldo)
