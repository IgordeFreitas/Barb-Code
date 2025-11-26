# Seu controller/postBarbeiro.py (Corrigido)
from config.dbConfig import getConnection
from model.atendimento.post import post

def cadastrarAtendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico):
    connection = None
    try:
        connection = getConnection()
        
        post(connection, data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico)
        connection.commit() 
        
        return {"mensagem": "Atendimento cadastrado com sucesso!", "status": 201}

    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar atendimento: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()