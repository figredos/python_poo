# Importando ABC e abstractmethod para criação de uma classe abstrata
from abc import ABC, abstractmethod


# Criando a classe abstrata 'Notificacao' importando da classe 'ABC'
class Notificacao(ABC):
    # Definindo o método 'init' com retorno 'None'
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    # Definindo o método abstrato 'enviar', com retorno bool (True ou False)
    @abstractmethod
    def enviar(self) -> bool: ...


# Criando a classe 'NotificacaoEmail' que herda da classe abstrata 'Notificacao'
class NotificacaoEmail(Notificacao):
    # Definindo o método abstrato, com retorno bool, que envia uma mensagem
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


# Criando a classe 'NotificacaoSMS' que herda da classe abstrata 'Notificacao'
class NotificacaoSMS(Notificacao):
    # Definindo o método abstrato, com retorno bool, que envia uma mensagem.
    # Tem a mesma assinatura do método enviar da classe 'NotificacaoEmail', porém função diferente
    # Por não ter alteração na assinatura, mas funções diferentes, esse é um exemplo de polimorfismo
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


# Definindo a função notificar, que recebe instancias da classe 'Notificacao'
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('notificação enviada')
        return

    print('notificação não enviada')


# Instanciando as classes e executando a função 'notificar, para demonstrar que possuem a mesma assinatura
notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando e-mail')
notificar(notificacao_sms)
