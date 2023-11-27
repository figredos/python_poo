# MIXINS

## O QUE É

Mixins são classes que contém uma série de métodos e atributos de adicionar funcionalidade para classes, são forma uma boa forma de poupar código. Não são consideradas classes-base, pois, apesar de serem adicionadas usando herança, são mais uma forma de adicionar funcionalidade sem serem incluídas na árvore de herança da classe.

## COMO IMPLEMENTAR

Para implementar um mixin, é apenas questão de criar uma classe que estende funcionalidade de uma classe, criando atributos ou métodos que ao serem adicionados em outras classes por meio de herança simples ou múltipla, acresce em funcionalidade, sem necessariamente entrar na árvore de herança dessa árvore. Um exemplo funcional, é a adição de uma classe que faz registros (logs) de execuções de métodos dentro de classes. Outro exemplo seria o seguinte, considere que existam 3 classes que descrevem animais, a classe 'Cavalo', a 'Aguia' e a 'Borboleta'. As 3 classes herdam da classe pai, 'FormaDeVida', considere também a classe Mixin, 'VoadorMixin', herdada apenas pelos animais voadores. Todos os animais são formas de vida, mas apenas alguns tem a função adicional de voar.
