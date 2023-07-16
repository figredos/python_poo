# Importando a classe 'LogPrintMixin'
from log import LogPrintMixin


# Criando classe 'Eletronico'
class Eletronico:
    # Definindo método init
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    # Definindo método ligar
    def ligar(self):
        if not self._ligado:
            self._ligado = True

    # Definindo método desligar
    def desligar(self):
        if self._ligado:
            self._ligado = False


# Criando classe 'Smartphone' que herda de 'Eletronico' e de 'LogPrintMixin'
class Smartphone(Eletronico, LogPrintMixin):
    # Criando método ligar, adicionando funcionalidade
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    # Criando método desligar, adicionando funcionalidade
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_success(msg)
