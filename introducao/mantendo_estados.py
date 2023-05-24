# Mantendo estados dentro da classe

# Criando classe 'Camera'
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando    # Filmando é um estado que por padrão é Falso

    # Criando método filmar
    def filmar(self):
        # Checa se filmando é verdadeiro
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True    # Caso filmando seja falso, seu estado é mudado

    # Criando método 'parar_filmar', que muda o estado de 'filmando'
    def parar_filmar(self):
        # Checa se filmando é falso
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False   # Caso filmando seja falso, seu estado é mudado

    # Criando método fotografar
    def fotografar(self):
        # Checa se filmando é verdadeiro
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


# Instânciando a classe 'Camera' e testando os métodos
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()