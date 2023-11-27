# CLASSES DECORADORAS

## O QUE SÃO

Classes decoradoras são uma outra forma de decorar objetos em python. Funcionam de forma muito similar à funções decoradoras, uma vez que seu funcionamento deve mais ao método call, do que ao seu tipo 'class'.

## COMO IMPLEMENTAR

Para implementar uma classe decoradora, como citado anteriormente, é necessário criar o método '__call__' na classe (o método call é aquele que possibilita a chamada de um objeto ou uma classe como uma função, usando parênteses) e definí-lo como uma função decoradora. Feito isso é necessário apenas decorar usando 'syntax sugar' o objeto intendido e usa-lo normalmente.
