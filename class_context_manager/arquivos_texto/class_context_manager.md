# Class Context Manager

## O QUE SÃO

Classes de context manager são uma forma de criar gerenciadores de contexto, possibilitando também, a implementação dos próprios protocolos, conforme for necessário. A implementação desses protocolos é possibilitada pelo uso de alguns *dunder* methods que o python usa, o chamado "duck typing". O nome "duck typing" vem da natureza de como o python analisa essas classes usadas como context manager, "Se vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato". A frase anterior é simplesmente uma forma de mostrar que o "duck typing" é um conceito de tipagem dinâmica onde o python não está interessado no tipo do objeto, mas sim se existem métodos no objeto para que ele funcione de forma adequada. Os métodos que devem ser implementados, são o '__enter__' e o '__exit__'.

## EXCEÇÃO EM CLASSE CONTEXT MANAGER

O método '__exit__' recebe a classe da exceção, a exceção e o traceback

Obs.: Traceback em python é um pequeno relatório contendo as chamadas de função feitas no código em um determinado momento, como visto quando algum erro é gerado no código.

## contextlib.contextmanager

Dentro do pacote 'contextlib', existe uma função decoradora, que fornece ao dev uma outra forma de criar um context manager. Após a importação da função 'contextmanager', a ideia é criar uma funçao geradora que vai receber o decorador. Feito isso, o processo é simples, criar um gerador de contexto dentro da função que gera o arquivo. Convém criar tal gerente de contexto dentro de um bloco 'try-except', com o intuito de sempre fechar um arquivo
e tratar os possíveis erros levantados.
