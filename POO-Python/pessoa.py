from random import randint

"""
class Pessoa:
    def falar(self):
        print('a pessoa está falando...')
"""

class Pessoa: # criação de classe
    """
    uma função dentro de uma classe é um método que molda o
    comportamento de uma classe

    self: é o objeto criado no arquivo principal (p1 ou qualquer outro objeto a ser criado)
    os outros argumentos são atributos
    """

    ano_atual = 2021 #funciona em toda a classe, para ser chamada precisa do self

    def __init__(self, nome, idade, comendo=False, falando=False): #init(construtor)
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def outro_metodo(self):
        self.nome = 'jose'
        print(self.nome)

    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        self.comendo = False
        print(f'{self.nome} parou de comer')

    def falar(self):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        print(f'{self.nome} está falando sobre o assunto')

    def ano_nasc(self):
        nasc = self.ano_atual - self.idade # nasc não precisou de self pq é uma variável do método
        print(f'{self.nome} nasceu em {nasc}')

    @classmethod #decorador - ele cria um objeto baseado nos parametros enviados
    def por_ano_de_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 99999)
        return rand
