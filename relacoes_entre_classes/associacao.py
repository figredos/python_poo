# Demonstrando associação de classes

# Criando a classe escritor
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    # Definindo getter e setter do parâmetro ferramenta
    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


# Criando a classe FerramentaDeEscrever
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    # Definindo o método escrever
    def escrever(self):
        return f'{self.nome} está escrevendo'


# Instanciando as classes
escritor = Escritor('Matheus')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina de Escrever')

# Fazendo a associação de classes, onde o parâmetro ferramenta da classe Escritor é uma classe por si só
escritor.ferramenta = caneta

# Demonstrando que ambos os comandos abaixo possuem a mesma função e saida
print(caneta.escrever())
print(escritor.ferramenta.escrever())

# Fazendo novamente a associação entre as classes, com outra instância 'maquina_de_escrever' ao invés de 'caneta'
escritor.ferramenta = maquina_de_escrever

# Mais uma vez demonstrando que as duas funções abaixo possuem a mesma função e saida
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
