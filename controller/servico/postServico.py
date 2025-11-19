from config.dbConfig import getConnection
from model.servico.post import post

def cadastrarServico(nome, preco):
    connection = None
    try:
        connection = getConnection()
        
        post(connection, nome, preco)
        connection.commit() 
        
        return {"mensagem": "Serviço cadastrado com sucesso!", "status": 201}

    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar serviço: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()