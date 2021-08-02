"""
COMPOSIÇÃO: Uma classe pertence a outra, se a classe principal for apagada
toda a outra classe também será apagada, nesse exemplo a classe endereço
pertence a classe cliente, se cliente for apagado, os objetos criados pela
classe endereço também serão - os edereços pertencem aos clientes.
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self): #coletor de lixo - garbage collector - não executa se for apagado antes
        print(f'O {self.nome} foi apagado')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'A {self.cidade}/{self.estado} foram apagados')

c1 = Cliente('arnaldo', 17)
c1.insere_endereco('belo horizonte', 'MG')

c2 = Cliente('joao', 20)
c2.insere_endereco('duque de caxias', 'RJ')

c3 = Cliente('ana', 30)
c3.insere_endereco('são joão', 'RJ')

print(c1.nome)
c1.lista_endereco()
del c1
print()

print(c2.nome)
c2.lista_endereco()
del c2
print()

print(c3.nome)
c3.lista_endereco()
del c3

print('#'*20)

