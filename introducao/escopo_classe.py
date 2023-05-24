# Escopos de classes

# Criando classe 'Animal'
class Animal:
    # Criando o método init
    def __init__(self, nome):
        # Criando atributo 'nome'
        self.nome = nome

        # Criando uma variável que só pode ser acessada de dentro do método init
        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maça'))
