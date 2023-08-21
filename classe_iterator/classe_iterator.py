# Importando a classe 'Sequence'
from collections.abc import Sequence
from typing import Self

# Criando uma classe para funcionar como lista e implementando os métodos necessários
class MyList(Sequence):
    # Definindo o init
    def __init__(self):
        self._data = {}  # Atributo que recebe os dados
        self._index = 0  # Contador para o índice
        self._next_index = 0  # Contador para o próximo índice

    # Definindo o método 'append', que adiciona dados
    def append(self, *values: any) -> None:
        for value in values:
            self._data[self._index] = value
            self._index += 1

    # Definindo o método '__len__', que retorna o tamanho da lista
    def __len__(self) -> int:
        return self._index

    # Definindo o método '__getitem__' que retorna o item do índice indicado
    def __getitem__(self, index: int) -> any:
        return self._data[index]

    # Definindo o método '__setitem__' que altera o item do índice indicado com o valor recebido
    def __setitem__(self, index: int, value: any) -> None:
        self._data[index] = value

    # Definindo o método '__iter__'
    def __iter__(self) -> Self:
        return self

    # Definindo o método '__next__' que entrega próximo item para o iterador
    def __next__(self) -> any:
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1

        return value


# Instanciando a classe
if __name__ == '__main__':
    lista = MyList()
    lista.append('Matheus', 'Fellet')
    lista.append('Giulia')

    for item in lista:
        print(item)
