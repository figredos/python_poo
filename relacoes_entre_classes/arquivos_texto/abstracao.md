# ABSTRAÇÃO

## O QUE É

Abstração é um dos pilares da poo juntamente do encapsulamento e da herança. Através do processo da abstração um programador "esconde" tudo que não seja dado relevante sobre um objeto com objetivo de reduzir a complexidade da classe e aumentar sua eficiência.

## ABSTRAÇÃO EM PYTHON

Abstração em python é feito através do uso de métodos e classes abstratas. As chamadas ABCs são usadas como contratos para a definição de outras classes. Elas podem forçar outras classes a criarem métodos concretos, podendo também conte-los. '@abstractmethods' são métodos que não têm corpo. As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instanciadas diretamente. Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethods). Uma classe abstrata em python tem sua metaclasse (metaclasse é uma classe que cria classes) sendo 'ABCMeta'. É possível criar '@property', '@setter', '@classmethod', '@staticmethod' e
'@method' como abstratos, para isso é necessário apenas usar '@abstractmethod' como decorador mais interno. 

OBS.: Foo - Bar são palavras usadas como placeholder para palavras que podem mudar durante a programação.
