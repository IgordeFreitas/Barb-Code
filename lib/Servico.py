class Servico():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome (self):
        return self.nome
    
    def setNome(self, novoNome):
        self.nome = novoNome

    def getPreco(self):
        return self.preco

    def setPreco(self, novoPreco):
        self.preco = novoPreco