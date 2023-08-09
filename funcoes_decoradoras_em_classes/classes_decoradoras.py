# Criando a classe 'Multiplicar'
class Multiplicar:
    # Definindo o init, que recebe um multiplicador
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    # Definindo o método call como uma função decoradora
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


# Decorando a função soma com a classe multiplicar, que por sua vez, recebe como argumento o número 2
@Multiplicar(2)
def soma(x, y):
    return x + y


# Usando a função
dois_mais_quatro = soma(2, 4)

# Imprimindo o resultado e o tipo do objeto
print('resultado: ', dois_mais_quatro, '\ntipo: ', type(dois_mais_quatro))