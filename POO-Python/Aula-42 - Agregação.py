"""
Agregação: Uma classe pode existir, mas para ele funcionar
precisa de outra classe, no exemplo de baixo, a Classe carrinho de
compras existe, mas para ele fazer qualquer método precisa da classe
produto
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

p1 = Produto('camisa', 50)
p2 = Produto('tenis', 100)
p3 = Produto('calça', 150)

#print(p1.nome, p1.valor)
carrinho = CarrinhoDeCompras()
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()
print(carrinho.soma_total())
