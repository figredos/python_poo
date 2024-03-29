# DATACLASSES

## O QUE SÃO

Dataclasses são uma espécie de template de classes, uma vez que servem para criar classes de forma simplificada. A criação de uma dataclasse inclui em si alguns métodos mágicos, como '\__init__', '\__repr__' e '\__eq__'. Para criar uma dataclasse, é necessário primeiramente, fazer a importação do módulo dataclasses, em seguida, decorar a classe desejada com a função '@dataclass'. Em resumo, dataclasses são syntax sugar para criar classes normais. É possível fazer com que a dataclasse não crie um dos métodos citados acima automaticamente, simplesmente passando um argumento para o decorador de classe (Ex.: @dataclass(init=False), fazendo com que o método \__init__ não seja definido pela dataclasse).

## DEFININDO ATRIBUTOS

Para a definição de atributos dentro de uma dataclass, é necessário, dentro do escopo da classe, nomear o atributo seguido por ':' e pelo seu tipo (str, int, float, bool, ...).

## \__post_init__

O método \__post_init__ é das particularidades de uma dataclass. Nada mais é do que uma forma de exeutar código após a inicialização da classe, se tornando especialmente útil, quando o inicializador da classe (\__init__) não é criado pelo dev diretamente, mas sim, feito pela dataclasse.

## CONFIGURAÇÕES DO DECORADOR '@dataclass'

Assim como citado acima, existem uma série de configurações que podem ser passadas para o decorador '@dataclass' de forma a alterar a criação da classe. Alguns desses são:

- init= : Caso False, não cria automaticamente o método \__init__ (default: True). Outros métodos como '\__repr__' e '\__eq__' podem ser alterados de forma similar.
  
- frozen= : Caso True, impede a adição de novos atributos (default: False)
  
- order= : Caso True, possibilita a ordenação dos objetos da classe, com base no primeiro atributo (default: False)

## FUNÇÕES 'asdict' E 'astuple'

O módulo dataclass possui também funções como 'asdict', que transformam um objeto de classe em dicionário e 'astuple', que transforma um objeto de classe em tupla.

## FUNÇÃO 'field' E 'fields'

É possível fazer a atribuição de valores a atributos de dataclasses. Quando declarados os argumentos, simplesmente após seu tipo atribuir um valor padrão ao atributo. O único problema, é que isso é apenas possível para tipos imutáveis, coisas como listas não podem ser adicionadas com atribuição simples, para isso é usada a função field. Com essa função, é possível não só atribuir a qualquer tipo de dado um valor padrão, mas também possibilita a criação de atributos com tipos mutáveis, como listas. A função fields por sua vez, mostra os metadados de um objeto, possibilitando a visualização de uma série de configurações.