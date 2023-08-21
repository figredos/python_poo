# Importando o módulo 'dataclass'
from dataclasses import dataclass


# Criando uma classe usando o decorador '@dataclass'
@dataclass
class Pessoa:
    # Declarando os atributos do '__init__'
    nome: str
    idade: int
    sobrenome: str

    # Definindo um getter
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    # Definindo um setter
    @nome_completo.setter
    def nome_completo(self, valor: str):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


# Instanciando e testando o método '__eq__'
if __name__ == '__main__':
    p1 = Pessoa('Giu', 20, 'Fellet')
    p2 = Pessoa('Luiz', 30, 'filgueira')

    print(p1 == p2)
