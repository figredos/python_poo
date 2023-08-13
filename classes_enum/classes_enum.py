# Importando o pacote enum
import enum


# Criando um enum
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# Criando uma classe enum
class Direcoes(enum.Enum):
    # Definindo as enumerações, e atribuindo seus valores automaticamente com a função 'enum.auto()'
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


# Imprimindo as enumerações e seus valores
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


# Definindo a função mover
def mover(direcao: Direcoes) -> None:
    # Checando se o argumento recebido é parte da classe 'Direcoes'
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


# Usando a função com argumentos da classe enum 'Direcoes'
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('lado')
