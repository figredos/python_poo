class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Criando o método '__repr__' da classe
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    # Criando o método '__add__', possibilitando usar o operador '+' nos objetos da classe
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    # Criando o método '__gt__', possibilitando o uso do operador '>' da classe
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


# Instanciando a classe 'Ponto'
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

# Usando o método '__add__', que funciona como um object factory
p3 = p1 + p2

# Imprimindo os dados dos objetos acima
print(p1)
print(p2)
print(p3)
print(p2 > p3)