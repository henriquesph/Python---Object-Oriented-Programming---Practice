from pessoa import Pessoa

#p1 = Pessoa()
#p2 = Pessoa()

"""
p1.nome = 'Luiz'
p2.nome = 'João'

print(p1.nome)
print(p2.nome)

p1.falar()
p2.falar()
"""

"""
p1 = Pessoa('henrique',30)
print(p1.nome)
print(p1.idade)
print(p1.outro_metodo())
"""

#metodo de instancia
p1 = Pessoa('henrique',30,False) # criei um objeto da instancia(classe) Pessoa com atributos
p1.comer('laranja')
p1.parar_de_comer()
p1.falar()
p1.comer('abacaxi')
p1.falar()
p1.parar_de_comer()
p1.falar()

#metodo de classe
print(Pessoa.ano_atual)
print(p1.ano_atual)
p1.ano_nasc()
p2 = Pessoa.por_ano_de_nasc('ana',1982) #usando o método de classe
print(p2.nome,p2.idade)
print(p2.ano_nasc())
