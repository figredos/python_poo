# Criando a classe de Exceção 'MeuError'
class MeuError(Exception):
    ...


# Criando a função 'levantar' que levanta um erro
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    raise exception_


# Bloco try, except demonstrando lançamento de exceções
try:
    levantar()
except (MeuError, Exception) as error:
    print(f'{error.__class__.__name__}: {error.args}')
