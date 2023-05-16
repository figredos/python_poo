# Classes são uma forma de criar objetos em python
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


pessoa_1 = Pessoa('Matheus', 'Fellet')
print(pessoa_1.nome)
print(pessoa_1.sobrenome)

pessoa_2 = Pessoa('Giulia', 'Fusaro')
print(pessoa_2.nome)
print(pessoa_2.sobrenome)
