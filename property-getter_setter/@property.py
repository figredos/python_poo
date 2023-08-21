# Criando a classe 'Caneta'
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # Método get_cor é um getter hard coded
    def get_cor(self):
        print('GET COR')
        return self.cor_tinta

    # Usando o decorador '@property' para exercer a função de getter, fazendo com que o método 'cor' aja como atributo
    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        print('PROPERTY')
        return self.cor_tinta


# Instanciando a classe
caneta = Caneta('Azul')

# Usando métodos getters, sendo o primeiro hard coded e o segundo usando o decorador '@property'
print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)