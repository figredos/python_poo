# Criando a classe pai, 'Pessoa'
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print((self.nome, self.sobrenome), self.__class__.__name__, sep=',da classe: ')


# Criando a classe filha 'Cliente'
class Cliente(Pessoa):
    ...


# Criando a classe filha 'Aluno'
class Aluno(Pessoa):
    ...


# Instanciando as classes filhas
c1 = Cliente('Matheus', 'Fellet')
a1 = Aluno('Giulia', 'Fellet')

# As classes 'Aluno' e 'Cliente' são extensões da classe 'Pessoa'
c1.falar_nome_classe()
a1.falar_nome_classe()
