# Criando o atributo caneta
class Caneta:
    # Criando o init e usando o setter como atributo
    def __init__(self, cor, cor_tampa):
        # Atributo protegido
        self.cor = cor
        self.cor_tampa = cor_tampa

    # Getter em hard code, do jeito não pythonico, fazendo com que, para imprimir o nome da cor salva, seja necessário
    # usar o método, ao invés de apenas usar o nome
    def get_cor(self):
        return self._cor

    # Usando o syntax sugar '@property' para criar um getter de nome 'cor'
    @property
    def cor(self):
        return self._cor

    # Usando o syntax sugar '@cor.setter' para criar um setter, responsável por definir a cor do objeto caneta
    @cor.setter
    def cor(self, valor):
        if valor == 'rosa':
            print('Valor inválido!')
        self._cor = valor

    # Usando o syntax sugar '@property' para criar um getter de nome 'cor_tampa'
    @property
    def cor_tampa(self):
        return self._cor_tampa

    # Usando o syntax sugar '@cor_tampa.setter' para criar um setter, responsável por definir a cor da tampa do
    # objeto caneta
    @cor_tampa.setter
    def cor_tampa(self, valor):
        if valor != self._cor:
            print('A tampa da caneta está com a cor errada!')
            self._cor_tampa = valor


if __name__ == '__main__':
    caneta = Caneta('azul', 'vermelha')
    print(caneta.cor_tampa)
    print(caneta.cor)
