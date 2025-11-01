class Pessoa():
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
    
    def getNome(self):
        return self.nome
    
    def setNome(self, novoNome):
        self.nome = novoNome

    def getEmail(self):
        return self.email
    
    def setEmail(self, novoEmail):
        self.email = novoEmail

    def getSenha(self):
        return self.senha
    
    def setSenha(self, novaSenha):
        self.senha = novaSenha

    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, novoTelefone):
        self.telefone = novoTelefone