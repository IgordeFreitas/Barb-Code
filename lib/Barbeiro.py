from lib.Pessoa import Pessoa

class Barbeiro(Pessoa):
    def __init__(self, nome, email, senha, telefone):
        super().__init__(nome, email, senha, telefone)
        self.cpf = 0
        self.id = 0

    def getCpf(self):
        return self.cpf
        
    def setCpf(self, novoCpf):
        self.cpf = novoCpf
    
    def getId(self):
        return self.id
    
    def setId(self, novoId):
        self.id = novoId