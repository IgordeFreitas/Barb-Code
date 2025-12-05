from config.dbConfig import getConnection
from model.barbeiroServico.post import post

def cadastrarBarbeiroServico(id_barbeiro, id_servico):
    connection = None
    try:
        connection = getConnection()
        
        post(connection, id_barbeiro, id_servico)
        connection.commit() 
        
        return {"mensagem": "Serviço do barbeiro cadastrado com sucesso!", "status": 201}

    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar serviço do barbeiro: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()