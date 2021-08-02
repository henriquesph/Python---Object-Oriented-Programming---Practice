"""
Associação - objetos sendo associados a outros mas sem relação de
dependencia, quando um objeto é excluido o outro ainda continua existindo
"""

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class Maquina_de_esquever:
    def escrever(self):
        print('Maquina está escrevendo...')


escritor = Escritor('Aroldo')
#print(e.nome)

caneta = Caneta('Bic')
#print(c.marca)

maquina = Maquina_de_esquever()
#print(m)

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

#escritor.ferramenta = caneta
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()