"""
Outras linguagens de programação:
    public: aberto a instancias e classes
    protected: somente a classe e classes filhas (herença)
    private: somente a classe
"""

class BancoDeDados:
    def __init__(self):
        #self._dados = {}
        self.__dados = {}

    # para ser chamado sem underline
    @property
    def dados(self):
        return self.__dados

    """
    _private: variavel com 1 underline na frente é um --privado fraco--, não
      não aparece como opção quando é chamado na instancia, tenho que digitar,
      dá erro em todos os outros métodos, mas consigo mudar o valor da variavel,
      indica a outros devs que não é para ser acessado
      
    __ private: -- privado mais forte: também indica a outro desenvolvedor que não é para ser acessado,
                   mas não dá erro nos outros métodos, pq ele cria um atributo em separado para a instância
                   e preserva o atributo da classe
    """

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BancoDeDados()
bd.inserir_clientes(1, 'Amanda')
bd.inserir_clientes(2, 'Jorge')
bd.inserir_clientes(3, 'Ana')
bd.apaga_cliente(2)
#bd.lista_clientes()
bd.__dados = 'uma outra coisa'
print(bd.__dados) #cria outro atributo
#bd.lista_clientes()
print(bd._BancoDeDados__dados) # atributo real da classe
print(bd.dados) # criei um getter para acessar valor
print(bd.__dados)
#bd.dados = 'criei outra coisa' não consigo mudar o atributo
#print(bd.dados)
