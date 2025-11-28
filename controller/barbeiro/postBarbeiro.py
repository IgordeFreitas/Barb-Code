# Seu controller/postBarbeiro.py (Corrigido)
from config.dbConfig import getConnection
from model.barbeiro.post import post
from utils.validarCPF import validarCPF
from utils.validarNome import validarNome
def cadastrarBarbeiro(nome, cpf, email, senha, telefone):
    connection = None
    try:
        connection = getConnection()
        
        validacao = validarCPF(cpf) and validarNome(nome)

        if validacao:
            post(connection, nome, cpf, email, senha, telefone)
            connection.commit() 
        
            return {"mensagem": "Barbeiro cadastrado com sucesso!", "status": 201}
        else:
            return {"erro": "Ao cadastrar os dados do barbeiro"}
        
    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar barbeiro: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()