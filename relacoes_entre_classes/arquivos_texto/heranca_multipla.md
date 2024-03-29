# HERANÇA MÚLTIPLA

## O QUE É

Herança múltipla é um tipo de relação entre classes que possibilita classes filhas herdarem de mais de uma classe pai. O python é uma das linguagens de programação que possui implementação de herança múltipla, contudo isso é a exceção, tendo em vista que grande parte das linguagens de programação não possui essa ferramenta. De forma simples, a herança múltipla se da quando uma classe herda de mais de uma só classe.

Ex.: Herança Simples:

    Animal -> Mamífero -> Humano -> Pessoa -> Cliente

    Herança múltipla:
    Log -> FileLog
    Animal -> Mamífero -> Humano -> Pessoa -> Cliente
    Cliente(Pessoa, FileLog)

É possível, e importante para um bom entendimento do código, usar o método da classe mro(), ou __mro__() que
imprime a ordem de resolução de métodos.

## PROBLEMA DO DIAMANTE

O problema do diamante é o nome dado a um problema gerado através do uso de herança múltipla onde duas classes B e C herdam de uma classe A e D herda de B e C, dentro da classe A existe um método sobrescrito em B e C, mas não em D. O problema do diamante surge no questionamento de onde a classe D deve herdar o método (method resolution order, mro). O nome "problema do diamante", ou como é carinhosamente apelidado, "Deadly Diamond of death", é dado pelo formato do diagrama formado pelo problema como demonstrado abaixo:

                              A
                             / \
                            B   C
                             \ /
                              D

## C3 SUPERCLASS LINEARIZATION

É a forma com a qual o python gerencia o problema do diamante. Se trata de uma ordem de "preferência" entre qual a ordem das classes deve ser executada. Esse [link](https://en.wikipedia.org/wiki/C3_linearization) demonstra e elabora mais no assunto em questão. 