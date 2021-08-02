# Getter e Setter para corrigir erro de transformar string em float

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower()


    # Getter - pega o valor
    @property
    def preco(self):
        return self._preco

    # Setter - configura o valor
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('CAMISA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)