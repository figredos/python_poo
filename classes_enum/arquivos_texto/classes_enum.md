# Classes Enum

## O QUE SÃO

Enumerações na programação são usadas em ocAsiões onde temos um determinado número de coisas. Enums têm membros e seus valores são constantes. Enums em python são um conjunto de nomes simbólicos (membros) ligados a valores únicos, podem ser iterados para retornar seus membros canônicos na ordem de definição. 'enum.Enum', é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enums não são classes normais em python). Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.

## OBTENDO DADOS COM ENUM

Para obter dados em uma classe enum, existem algumas formas:

~~~python
membro = Classe(valor), Classe['chave']
chave = Classe.chave.nome
valor = Classe.chave.valor
~~~