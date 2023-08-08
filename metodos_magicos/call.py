# Criando a classe 'CallMe'
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # Definindo o método '__call__', possibilitando a chamada dos objetos da classe como função
    def __call__(self, nome):
        print(f'{nome} está chamando, {self.phone}')


# Instanciando a classe
call_1 = CallMe('32166549')

# Fazendo o 'call' do objeto da classe
call_1('Giulia')