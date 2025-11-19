from config.dbConfig import getConnection
from model.cliente.post import post

def cadastrarCliente(nome, email, senha, telefone):
    connection = None
    try:
        connection = getConnection()
        
        post(connection, nome, email, senha, telefone)
        connection.commit() 
        
        return {"mensagem": "Cliente cadastrado com sucesso!", "status": 201}

    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar cliente: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()