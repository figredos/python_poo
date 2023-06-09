# Importando pacotes
from datetime import datetime


# Criando a classe 'Pessoa'
class Pessoa:
    # Criando um atributo da classe
    ano_atual = datetime.now().year

    # Declarando o método init
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Criando o método 'get_ano_nascimento' que descobre o ano de nascimento com base na idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    """O método 'get_ano_nascimento' é ineficiente por calcular apenas a diferença absoluta entre a idade e o ano 
    atual"""


# Criando objetos da classe pessoa
pessoa_1 = Pessoa('João', 33)
pessoa_2 = Pessoa('Giulia', 20)

# Imprimindo o ano de nascimento obtido pelo método 'get_ano_nascimento'
print(pessoa_1.nome, pessoa_1.get_ano_nascimento())
print(pessoa_2.nome, pessoa_2.get_ano_nascimento())
