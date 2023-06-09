# Exercicio - Carregue dados JSON na classe

# Importando o pacote json e a classe pessoa, usada no arquivo 'classe_json_dump.py'
import json
from classe_json_dump import Pessoa

# Context Manager para abrir no modo leitura o arquivo json
with open('classe.json', 'r') as arquivo:
    # Usando a função load do pacote json para carregar os dados contidos nele e colocá-los na variável dados
    dados = json.load(arquivo)

# Desempacotando o dicionário dados na variável pessoa_1, instanciando a classe Pessoa
pessoa_1 = Pessoa(**dados)

# Usando a função vars para checar se os dados foram importados corretamente.
print(vars(pessoa_1))