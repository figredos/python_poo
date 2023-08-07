# Importando do módulo 'contextlib' a função 'contextmanager', para criar e usar gerenciadores de contexto em funções.
from contextlib import contextmanager


# Criando o gerador de contexto, decorado pela função 'contextmanager'
@contextmanager
def my_context_manager(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo)
        yield arquivo
    except Exception as e:
        print('Ocorreu o erro: ', e)
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()


with my_context_manager('arquivos_texto/arquivo_contextlib.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
