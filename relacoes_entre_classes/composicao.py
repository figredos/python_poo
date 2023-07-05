# Demonstando o uso de composição de classes

# Criando a classe Cliente
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # O método mágico del é o chamado Garbage collector, que limpa a memória uma vez que os objetos não são mais usados.
    def __del__(self):
        print('APAGANDO, ', self.nome)


# Criando a classe Endereço
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO, ', self.rua, self.numero)


# Instanciando as classes
cliente_1 = Cliente('Matheus')
cliente_1.inserir_endereco('Av Brasil', 54)
cliente_1.inserir_endereco('Rua B', 6745)

# Fazendo uma associação
endereco_externo = Endereco('Av saudade', 12345)
cliente_1.inserir_endereco_externo(endereco_externo)

cliente_1.listar_enderecos()

# Deletando
del cliente_1

# Mostrando que o endereco_externo é independente da classe, enquanto os outros foram deletados
print(endereco_externo.rua, endereco_externo.numero)
print('AQUI TERMINA MEU CÓDIGO.')
