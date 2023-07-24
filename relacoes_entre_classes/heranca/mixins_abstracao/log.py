# Fazendo importação de bibliotecas
from pathlib import Path

# Descobrindo o caminho parente do arquivo 'log.py' e criando o caminho 'log.txt'
LOG_FILE = Path(__file__).parent / 'log.txt'


# Criando a classe abstrata 'Log'
class Log:
    # Método abstrato, não tem funcionalidade quando instanciado, mas força classes que herdam a implementa-lo
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    # Método concreto, possui funcionalidade direta
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    # Método concreto, possui funcionalidade direta
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


# Criando a classe Mixin 'LogFileMixin' que herda de 'Log' e registra os logs em um .txt
class LogFileMixin(Log):
    # Criando o método '_log' como "exigido" pela classe da qual herda
    def _log(self, msg):
        # Criando uma mensagem formatada que informa o nome da classe na qual é executada
        msg_formatada = f'{msg} {self.__class__.__name__}'

        print(f'Salvando no log: {msg_formatada}')

        # Salvando o log no arquivo cujo caminho foi salvo previamente
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


# Criando a classe Mixin 'LogPrintMixin' que herda de 'Log' e imprime os logs no console
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


# Fazendo testes e instanciando
if __name__ == '__main__':
    log_p = LogPrintMixin()
    log_p.log_error('qualquer coisa')
    log_p.log_success('Deu bom familia')
    log_f = LogFileMixin()
    log_f.log_error('qualquer coisa')
    log_f.log_success('Deu bom familia')
