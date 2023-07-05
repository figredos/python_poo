# Demonstração de agregação de classes

# Criando a classe Carrinho que poderá receber um ou mais produtos
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([produto.preco for produto in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)


# Criando a classe produtos, que vai ser instanciada e colocada em agregação com a classe Carrinho
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Instanciando as classes
carrinho = Carrinho()
p1, p2 = Produtos('Caneta', 1.20), Produtos('Camiseta', 20)

# Fazendo a agregação
carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()
