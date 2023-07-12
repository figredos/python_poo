# Criando a classe 'MinhaString' que herda de str
class MinhaString(str):
    def upper(self):
        print('Chamou Upper')
        return super().upper()


# # Instanciando e executando método da classe 'MinhaString'
# string = MinhaString('Matheus')
# print(string.upper())


# Criando a classe pai 'A'
class A:
    atributo_a = 'valor a'

    # Definindo o init da classe 'A'
    def __init__(self, atributo):
        self.atributo = atributo

    # Definindo o método 'metodo' que imprime 'A'
    def metodo(self):
        print('A')


# Criando a classe 'B', que herda de 'A'
class B(A):
    atributo_b = 'valor b'

    # Definindo o init da classe B que herda o atributo 'atributo' da classe 'A'
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)  # Definindo o atributo 'atributo' da classe pai usando o comando super()
        self.outra_coisa = outra_coisa

    # Definindo o metodo 'metodo' da classe 'B' que herda o método de mesmo nome da classe 'A'
    def metodo(self):
        super().metodo()
        print('B')


# Criando a classe 'C', que herda de 'B'
class C(B):
    atributo_c = 'valor c'

    # Definindo o init da classe B que herda o atributo 'atributo' da classe 'A'
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)  # Definindo o atributo 'atributo' da classe pai usando o comando super()

    # Definindo o método 'metodo' da classe 'C' que herda o método de mesmo nome da classe 'B' e por consequência de 'A'
    def metodo(self):
        super().metodo()
        print('C')


# Instanciando a classe C
c = C('oi', 'ola')

# Imprimindo atributos da classe C
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

print(c.atributo, c.outra_coisa)
