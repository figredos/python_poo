# Criando a classe
class Classe:
    @staticmethod  # Usando o decorador '@staticmethod' para criar um método estático
    def funcao_que_esta_na_classe(*args, **kwargs):  # Função que recebe n argumentos e os imprime, junto à frase abaixo
        print('Esse é um exemplo de método estático', args, kwargs)


def funcao_normal(*args, **kwargs):  # Criando fora da classe, uma função que faz a mesma coisa do método estático
    print('Esse é um exemplo de função normal', args, kwargs)


# Comparando o método estático com a função normal
c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao_normal(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao_normal(nomeado=1)
# Todas as funcionalidades da função são iguais às do método estático, menos a chamada ser dentro da função.
