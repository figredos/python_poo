# Métodos em instâncias de classes Python
class Carro:
    # Declarando o método __init__
    def __init__(self, nome):
        self.nome = nome

    # Criando um método da classe carro
    def acelerar(self):
        return f'{self.nome} está acelerando...'


# Instanciando 'Carro' em um objeto chamado fusca
fusca = Carro('Fusca')

print(fusca.nome)  # Imprimindo o atributo nome do objeto carro

print(fusca.acelerar())  # Executando o método acelerar

# Instanciando 'Carro' em um objeto chamado celta
celta = Carro('Celta')

print(celta.nome)  # Imprimindo o atributo nome do objeto carro

print(celta.acelerar())  # Executando o método acelerar
