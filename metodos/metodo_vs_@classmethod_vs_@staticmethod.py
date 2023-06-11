class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # Métodos de instância setter em hard code
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.user = password

    # Método de classe para facilitar a criação de contas com usuários e senha
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    # Método estático para imprimir uma mensagem
    @staticmethod
    def log(msg):
        print('LOG:', msg)


# Função simples que faz a mesma coisa que o método estático
def connection_log(msg):
    print('LOG:', msg)
