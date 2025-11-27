from config.dbConfig import getConnection
from model.agenda.post import post

def cadastrarAgenda(dataHora, status, idBarbeiro):
    connection = None
    try:
        connection = getConnection()
        
        post(connection, dataHora, status, idBarbeiro)
        connection.commit() 
        
        return {"mensagem": "Agenda cadastrado com sucesso!", "status": 201}

    except Exception as e:
        if connection:
            connection.rollback() 
        
        print(f"Erro ao cadastrar agenda: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()