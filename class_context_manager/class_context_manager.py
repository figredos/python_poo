# Demonstrando a equivalência ao que será feito com a classe
# with open('arquivo_context_manager.txt', 'w') as arquivo:

# Criando a classe Context Manager
class MyContextManager:
    # Criando o método init, que recebe o caminho do arquivo e o modo de manipulação do arquivo
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    # Criando o método '__enter__'
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo)
        return self._arquivo

    # Criando o método '__exit__', que recebe a classe de exceção, a exceção e o traceback
    def __exit__(self, class_exception_, exception_, traceback_):
        print('ARQUIVO FECHANDO')
        self._arquivo.close()


# Instanciando a classe
with MyContextManager('arquivos_texto/arquivo_context_manager.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

    print('WITH', arquivo)
