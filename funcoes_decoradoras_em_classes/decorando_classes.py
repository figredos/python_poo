# Definindo uma função geradora de '__repr__'
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


# Definindo uma função que adiciona o método '__repr__' em classes
def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


# Definindo um decorador para métodos
def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O nome do planeta é {self.nome}'


# Instanciando as classes
arsenal = Time('Arsenal')
fluminense = Time('Fluminense')

terra = Planeta('Terra')
marte = Planeta('Marte')

# Imprimindo as informações sobre os objetos
print(arsenal)
print(fluminense)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())
