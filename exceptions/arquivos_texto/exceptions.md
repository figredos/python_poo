# EXCEPTIONS

## O QUE SÃO

Exceptions são mensagens de erros que acontecem durante a execução de um programa. Sua função é basicamente impedir que o programa quebre. Usar exceções em python é importante, pois são uma forma conveniente de tratar erros e condições especiais de um determinado programa, quando existe um código propenso a gerar erros. Para criar uma exceção em python, é necessário criar uma classe que herda de 'Exception'. Por convenção é necessário acrescentar ao final do nome da exceção, a palavra 'Error', uma vez que aquela classe é usada para indicar e levantar erros.

## NOTAS DAS EXCEPTIONS

A partir do python 3.11, se tornou possível adicionar notas às exceções. Usando uma exceção, seguida pelo comando '.add_note()', com a nota desejada dentro dos parênteses, uma vez que o erro for levantado, aquela mensagem será impressa, podendo facilitar a compreensão do código por outros devs.
