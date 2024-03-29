# METACLASSES

## O QUE SÃO

Metaclasses em python são basicamente o tipo das classes. Como qualquer outra coisa em python, classes também são objetos, e como qualquer objeto, possuem um tipo (1:int, 'oi':str, True:bool, []:list, ():tuple... etc.), e o de classes é 'metaclass'. Mais específicamente, o tipo de uma classe em python é 'type', o mesmo type usado para saber o tipo de outros objetos. 'type' é uma metaclasse que cria outras classes, ou seja, toda classe em python é uma instância de 'type', da mesma forma que objetos da classe criada são instâncias dela.

"Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar. Se você quer saber se precisa delas, não precisa, as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de uma explicação sobre o porquê."
\- Tim Peters (CPython Core Developer)

## DETALHAMENTO DA CRIAÇÃO DE CLASSES EM PYTHON

Ao criar uma classe em python, ocorrem por padrão as seguintes coisas:

- \__new__ da metaclass é chamado e cria a nova classe

- \__call__ da metaclass é chamado com os argumentos

  - \__new__ da class com os argumentos (cria a instância)

  - \__init__ da class com os argumentos

- \__call__ da metaclass termina a execução

## MÉTODOS IMPORTANTES DA METACLASS

1. \__new__(mcs, name, bases, dct) (cria a classe)
A assinatura do método __new__ de metaclasses é diferente de classes simples, recebendo primeiramente a metaclasse, seu nome, as heranças em tupla, e o dict da classe.

    O método '__new__' de uma metaclasse é aquele que cria e retorna a classe em si. Dentro do seu escopo, após a
    criação de uma classe, é possível realizar uma série de implementações de protocolos, seja criação de métodos,
    criação de atributos, ou até mesmo, pode ser usada para fazer levantamentos de erros quando certos métodos não
    são criados (abstração).

2. \__call__(cls, *args, **kwargs) (cria e inicializa a instância)
A assinatura do método __call__ de metaclasses, assim como o método __new__ também se diferencia de classes simples, recebendo, ao invés de self, a classe, e argumentos não nomeados e nomeados.

    O método '__call__' de uma metaclasse é aquele que cria e retorna a instância de uma classe. Dentro do seu esco-
    po, após a criação de uma classe, é possível realizar uma série de implementações de protocolos, assim como no
    método '__new__', com sua grande diferença, sendo o 'local' onde esses protocolos podem ser implementados, uma
    vez que o método '__new__' não tem acesso à instância da classe criada, mas apenas a classe em si. Com acesso à
    instância, torna-se possível agir como uma classe abstrata para a criação de atributos, por exemplo.