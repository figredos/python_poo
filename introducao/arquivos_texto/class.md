# CLASS

## O QUE É

Classes ão moldes para criar objetos. São uma estrutura que gera objetos (instâncias) que podem ter seus próprios atributos e métodos. Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações. Por convenção usamos PascalCase para nomes de classes (primeiras letras das palavras devem ser maiúsculas).

## NOTAÇÃO

Quando se refere ao nome de uma certa classe, é usada a notação CamelCase, fazendo referência às corcundas do animal. As letras iniciais das palavras que compõe o nome da classe em python devem ser em letra maiúscula, de acordo com a notação CamelCase.

## SELF

É uma referência à própria classe. Com seu uso é possível instanciar o objeto e acessar métodos, variáveis e atributos da classe em questão. O nome self não é obrigatório, só é usado por convenção, podendo ser chamado de qualquer nome, a posição ser o primeiro parâmetro é a única parte absolutamente necessária.

## \__init__()

É um método responsável pela inicialização de uma classe. Dentro dele serão declarados os possíveis atributos da classe em questão. Toda vez que uma classe for usada, a primeira coisa feita é a execução do método init. Esse método sempre retorna 'None'.

## O QUE SÃO MÉTODOS

Assim como o '__init__', existem outros métodos que podem ser criados e usados dentro de classes, sejam esses os chamados métodos mágicos (com uma função definida previamente, como '__init__', ou por exemplo, '__iter__', sendo um método feito para iterar um objeto), ou simples funções dentro do objeto com algum intuito ao serem executadas. Para criar qualquer método é necessário somente criá-lo como qualquer função, usar 'def' seguido pelo nome da função, recebendo entre parênteses parâmetros. Por padrão, todo método receberá como argumento, a própria classe referenciada em 'self'.

## ESCOPO DE CLASSE

Classes, como qualquer estrutura em python possue escopo próprio, tanto para a classe em si como para os métodos nela contidos.

## MANTENDO ESTADOS EM CLASSES

Uma grande utilidade de classes em python, é que seus estados são mantidos, ou seja, caso algum de seus atributos sejam alterados, eles se mantém assim até que sejam novamente alterados.

## ATRIBUTOS DE CLASSE

São uma forma de atributos que podem ser utilizados, sendo colocados diretamente dentro daclasse, fora do init. Assim fazendo que não sejam um atributo da instância, mas sim atributos da classe em si. Isso se estende à alteração desse atributo, uma vez que um atributo de classe for mudado, ele muda para todas as instâncias dessa classe, podendo gerar alterações indesejadas.

## ATRIBUTOS DE INSTÂNCIA

São os atributos presentes na classe, dentro do método init. São os dados inseridos sobre a própria instância, todos os que possuem self.

## \__dict__ E vars()

Quando uma classe é instanciada, e aos seus atributos são agregados valores, usando o método __dict__, é possível visualizar todos os atributos e valores em formato de dicionário com os atributos assumindo valor de chave e os valores dos atributos assumindo valores correspondentes a essas chaves. A função vars() faz exatamente a chamada do método __dict__ dentro da classe.

Ao as funções __dict__ e vars(), é possível, por exemplo transferir dados para arquivos json e vice-versa. Pode ser feito usando um Context Manager e o pacote json e suas ferramentas.