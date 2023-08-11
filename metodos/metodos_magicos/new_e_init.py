# Criando a classe 'A'
class A:
    # Definindo o método '__new__', que cria uma instância da classe
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        # Criando a instância importando o método '__new__' da super classe 'object'
        instancia = super().__new__(cls)
        print('Depois')
        return instancia

    # Definindo o método init
    def __init__(self, x):
        self.x = x
        print(self)

    # Definindo o método repr
    def __repr__(self):
        return'A()'


# Instanciando a classe 'A'
a = A(1)
