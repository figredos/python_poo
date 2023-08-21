# Importando a função namedtuple e a classe NamedTuple
from collections import namedtuple
from typing import NamedTuple


# Criando uma função NamedTuple
class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Criando objeto namedtuple
carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['VALOR', 'NAIPE'])

# Instanciando a tupla e a classe
as_espadas = carta('A', 'ouros')
as_espadas_1 = Carta('A', 'ouros')

# Ambas as formas obtêm o mesmo resultado
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)

# Imprimindo o dicionário gerado pelo objeto
print(as_espadas._asdict())

# Mostrando que os objetos são iguais
print(as_espadas._asdict() == as_espadas_1._asdict())

