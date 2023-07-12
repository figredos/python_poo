# Exercício com relação entre classes
# 1- Crie uma classe Carro (param: nome)
# 2- Crie uma classe Motor (param: nome)
# 3- Crie uma classe Fabricante (param: nome)
# 4- Faça a ligação Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5- Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# Criando a classe 'Motor'
class Motor:
    def __init__(self, nome):
        self._nome = nome

    # Definindo getter e setter
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_do_motor):
        self._nome = nome_do_motor


# Criando a classe 'Fabricante'
class Fabricante:
    def __init__(self, nome):
        self._nome = nome

    # Definindo getter e setter
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_do_fabricante):
        self._nome = nome_do_fabricante


# Criando a classe 'Carro'
class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._fabricante = None
        self._motor = None

    # Definindo getter e setter para o fabricante
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, nome_do_fabricante):
        self._fabricante = nome_do_fabricante

    # Definindo getter e setter para o motor
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, nome_do_motor):
        self._motor = nome_do_motor

    # Definindo getter e setter para o nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_do_carro):
        self._nome = nome_do_carro

    def exibe_info(self):
        return [self._nome, self._motor.nome, self._fabricante.nome]


if __name__ == '__main__':
    # Criando as instâncias das classes
    fusca = Carro('fusca')
    motor = Motor('fusca 67')
    fabricante = Fabricante('Volskwagen')

    # Fazendo associação
    fusca.motor = motor
    fusca.fabricante = fabricante

    # Imprimindo as informações
    info = fusca.exibe_info()

    for i in info:
        print(i)
