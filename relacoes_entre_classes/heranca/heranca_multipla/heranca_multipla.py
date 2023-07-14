# Criando a classe A
class A:
    ...

    def qual_nome(self):
        print('A')


# Criando a classe B que herda da classe A
class B(A):
    ...

    def qual_nome(self):
        print('B')


# Criando a classe C que herda da classe A
class C(A):
    ...

    def qual_nome(self):
        print('C')


# Criando a classe D que herda da classe B e da classe C, criando a situação do problema do diamante
class D(B, C):
    ...

    # def qual_nome(self):
    #     print('D')


# Istanciando a classe D e executando o método "qual_nome()"
d = D()
d.qual_nome()

# Imprimindo a ordem de resolução de métodos
print(D.mro())