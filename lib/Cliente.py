from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, email, senha, telefone):
        super().__init__(nome, email, senha, telefone)