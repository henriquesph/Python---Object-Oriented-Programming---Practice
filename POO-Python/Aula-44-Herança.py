"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

class Pessoa: # Super Classe - Classe filha
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está Falando')

class Cliente(Pessoa): # Subclasse
    def comprar(self):
        print(f'O {self.nome} está comprando')

class Aluno(Pessoa): # Subclasse
    def estudar(self):
        print(f'O {self.nome} está estudando')

p1 = Pessoa('henrique', 30)
c1 = Cliente('joao', 50)
a3 = Aluno('ana', 16)

p1.falar()
c1.falar()
a3.estudar()
c1.comprar()