# Criando a classe 'Ponto'
class Ponto:
    # Definindo o método init
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # Definindo o método str, que retorna uma string representando o objeto
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Definindo o método repr, que retorna uma string contendo informações mais técnicas sobre o objeto
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        # O retorno possui '!r' pois pe desejado o retorno 'repr' do atributo e questão
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


# Instanciando a classe 'Ponto'
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

# Imprimindo os dados em str e repr dos objetos 'p1' e 'p2'
print(p1)
print(repr(p2))
print(p1)