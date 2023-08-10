# Definindo a função 'meu_repr', que implementa o método '__repr__'
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


# Criando a classe 'Meta', que é uma metaclasse, sendo responsável por criar outras classes
class Meta(type):
    # Definindo o método '__new__', que cria e retorna a classe criada
    def __new__(mcs, name, bases, dct):
        # Imprimindo quando o método '__new__' é executado para entendimento da ordem de execuções de métodos
        print('__new__ DA METACLASSE')
        # Criando a classe
        cls = super().__new__(mcs, name, bases, dct)
        # Criando o atributo 'attr', que todas as classes e instâncias que herdarem ou forem criadas terão
        cls.attr = 1234
        # Criando na classe o método '__repr__'
        cls.__repr__ = meu_repr

        # Fazendo a checagem da implementação de um método, como em uma classe abstrata
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('IMPLEMENTE O MÉTODO FALAR')

        # Fazendo o retorno da classe
        return cls

    # Definindo o método '__call__', que cria e retorna as instãncias da classe
    def __call__(cls, *args, **kwargs):
        # Imprimindo quando o método '__call__' é executado para entendimento da ordem de execuções de métodos
        print('__call__ DA METACLASSE')

        # Criando a instância da classe
        instancia = super().__call__(*args, **kwargs)

        # Fazendo a checagem da implementação de um método nas instâncias da classe
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('IMPLEMENTE O ATTR \'nome\'')

        # Retornando a instância da classe
        return instancia


# Criando a classe 'Pessoa', que tem como metaclasse 'Meta'
class Pessoa(metaclass=Meta):
    # Definindo a função '__new__', que cria e retorna a instância da classe
    def __new__(cls, *args, **kwargs):
        # Imprimindo quando o método '__call__' é executado para entendimento da ordem de execuções de métodos
        print('__new__ DA CLASSE')
        # Criando a instância da classe
        instancia = super().__new__(cls)
        # Retornando a instância da classe
        return instancia

    # Definindo o método inicializador '__init__'
    def __init__(self, nome):
        # Imprimindo quando o método '__init__' é executado para entendimento da ordem de execuções de métodos
        print('__init__ DA CLASSE')
        self.nome = nome

    # Definindo o método estático 'falar'
    @staticmethod
    def falar():
        print('FALANDO...')


# Instanciando a classe 'Pessoa'
p1 = Pessoa('Giulia')

# Imprimindo métodos e atributos da classe
print(p1.attr)
print(p1)
p1.falar()
