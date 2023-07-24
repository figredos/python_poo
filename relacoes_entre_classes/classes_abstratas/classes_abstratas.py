# Importando a classe abc
from abc import ABC, abstractmethod


# Criando a classe abstrata 'Log'
class Log(ABC):
    # Método abstrato, não tem funcionalidade quando instanciado, mas força classes que herdam a implementá-lo
    @abstractmethod
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    # Método concreto, possui funcionalidade direta
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    # Método concreto, possui funcionalidade direta
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__}')
