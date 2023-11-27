# HERANÇA SIMPLES

## O QUE É

Herança é um dos pontos-chave de programação orientada a objeto. A ideia principal é facilitar a programação por parte do programador, com a herança é possível reaproveitar código ou comportamento generalizado, sendo possível também especializar operações ou atributos. Uma possível forma de descrever os comportamentos de cada uma das relações entre classes, é a seguinte; Associação, usa; Agregação, tem; composição, é dono de; Herança, é um. Classes usadas em herança tem denominações específicas, sendo a classe principal (Ex.: Pessoa, como mostrado abaixo e no diagrama uml) chamada de super class, base class, parent class, e suas classes filhas (Ex.: Cliente, como mostrado abaixo e no diagrama uml) chamada de sub class, child class, derived class.

Ex.: A ideia da herança é facilitar a escrita de código para classes, portanto, é necessário fazer generalizações, nesse caso, pensaremos em Pessoa como uma generalização da classe Cliente. Cliente vai extender a classe Pessoa, significando que os atributos e métodos que devem ser aplicados para a classe pessoa, serão também aplicados em Clientes.

## SUPER

É uma ferramenta que possibilita evitar a sobreposição de métodos da classe. Toda classe que herda da outra se torna aquela classe, e vamos supor que exista na classe pai, um método de mesmo nome que o desejado criar na classe filha. Caso isso seja feito sem o uso da ferramenta super, o método que está na classe filha estará sobrescrevendo o método da classe pai, fazendo com que na classe filha, o único método relevante seja o que está contido nela. Isso é muito presente quando, por exemplo, se intende criar atributos próprios da classe filha sem que os métodos da classe pai sejam sobrescritos. Para resolver esse problema, usamos o comando super(). É possível usar super em classes filhas para adicionar função a métodos e atributos da classe pai. Isso se estende ao método init, sobrescrito caso for adicionado sem o uso de super em uma classe filha. Para criar o método init em uma classe filha sem sobrescrever o da classe pai, é necessário usar a seguinte linha de comando:

~~~python
def __init__(self, atributo, outra_coisa):
    super().__init__(atributo)
    self.outra_coisa = outra_coisa
~~~

O código acima define o atributo 'atributo' na classe pai usando o comando super(), e em seguida é definido o init da classe filha.