# Métodos de classe

class Pessoa:
    ano = 2023  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # Decorador '@classmethod' faz com que um método seja chamado diretamente da classe.
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod  # Usando o decorador para usar uma função que retorna a classe em si de forma simplificada
    def criar_pessoa_50_anos(cls, nome):
        return cls(nome, 50)

    def metodo_simples(self):
        print('Hey')


# Criando instância da classe Pessoa
pessoa_1 = Pessoa('João', 15)

# Atributos de instância vs atributos de classe
print(pessoa_1.nome)
print(Pessoa.ano)

# Métodos de instância vs Métodos de classe
# Não é possível executar o 'metodo_simples' sem usar a instância 'pessoa_1'
Pessoa.metodo_simples(pessoa_1)

# Usando classmethod, isso se torna possível, pois o objeto do método não é a instância, mas a classe em si
Pessoa.metodo_de_classe()

# Usando um factory
p2 = Pessoa.criar_pessoa_50_anos('Chico')
print(p2.__dict__)