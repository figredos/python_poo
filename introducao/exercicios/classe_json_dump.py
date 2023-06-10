# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON

# Importando o pacote json
import json


# Criando a classe Pessoa, com atributos nome, sobrenome e idade
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


# Instanciando a classe pessoa
pessoa_1 = Pessoa('Giulia', 'Fellet', 25)
pessoa_2 = Pessoa('Matheus', 'Fusaro', 25)
pessoa_3 = Pessoa('Giulio', 'Filet', 25)
pessoas = [vars(pessoa_1), vars(pessoa_2), vars(pessoa_3)]

# Context Manager para criar e abrir no modo escrita o arquivo json
with open('classe.json', 'w') as arquivo:
    # Usando a função dump do pacote json, transferimos os dados da instância pessoa_1 para o arquivo json
    json.dump(pessoas, arquivo,
              ensure_ascii=False,  # Mantém o texto da forma que está, mesmo se um caractere não estiver na tabela ASCII
              indent=2  # Criando uma indentação entre os itens do arquivo
              )
